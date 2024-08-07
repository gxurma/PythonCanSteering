#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PyGui middleware
# this standing in the middle between the machine and Openpnp
# it can home the axes one by one
# interprete the g-code commands comming from openpnp,
# decide if the X2 axis has to be moved to reach to the other side of the table,
# and send the CAN bus commands to the appropriate drives

# from PyQt4 import QtCore, QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
# from PyQt4.uic import loadUi
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt

import sys
import csv

#from Gui import *
# import Gui
#talking to kvaser
from canlib import canlib
import time
#import random
import math

import os, struct, array
from fcntl import ioctl
# server socket
import socket
#regular expressions
import re
# sending and receiving queues
import queue
# to communicate to the Smothieware board via serial
import serial

import requests
import json

PRINTER = "http://10.0.111.50:8080/api/v1"
printer_axis_name = "TableSlots.TableSlots.TableSlotLeft.Axis"

printer_pos3_mm = 735.0
printer_pos2_mm = 300.0
printer_pos1_mm = 100.0
printer_pos0_mm = 0.0

printer_speed_mmps = 200.0



HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)


#ids:

idX = 0x16
idY = 0x1c
idZ = 0x39
idC = 0x18
idX2 = 0x4e

axes = [idX, idY, idZ, idC, idX2]

idTx = 0x300
idRx = 0x280

#position maximums and minimums of axes
maximum=[0,0,0,0,0]
minimum=[0,0,0,0,0]
maximumf=[.0,.0,.0,.0,.0]
minimumf=[.0,.0,.0,.0,.0]
# X: 200 count / mm
Xm = 200.0 #multiplikator
maximum[0] = 16300
minimum[0] = -16000
maximumf[0] = maximum[0]/Xm
minimumf[0] = minimum[0]/Xm

# Y: 200 count / mm
Ym = 200.0
maximum[1] = 22080
minimum[1] = -19260
maximumf[1] = maximum[1]/Ym
minimumf[1] = minimum[1]/Ym

# Z: 2000 count /mm
Zm = 2000.0
maximum[2] = 102000
minimum[2] = 0
maximumf[2] = maximum[2]/Zm
minimumf[2] = minimum[2]/Zm

# C: 2000 count / round
Cm = 11.388888889
maximum[3] = 10000
minimum[3] = -10000
minimumf[3] = minimum[3]/Cm
maximumf[3] = maximum[3]/Cm

# X2: 200 count / round
X2m = 66.66666666666666666666666
maximum[4] = 7500
minimum[4] = -4600
maximumf[4] = maximum[4]/X2m
minimumf[4] = minimum[4]/X2m

maxAcceleration = [100000, 100000, 100000, 50000, 50000]
maxDeceleration = maxAcceleration
smoothingFactor = 20
threshold = 5000


# This is the threding class. See beginning of PyGuiApp how to set up and use it or how to connect it to buttons and start it as a reaction
class GenericThread(QtCore.QThread):
	def __init__(self, function, *args, **kwargs):
		QtCore.QThread.__init__(self)
		self.function = function
		self.args = args
		self.kwargs = kwargs
	def __del__(self):
		self.wait()
	def run(self):
		self.function(*self.args,**self.kwargs)
		return


def cmp(a,b):
	return (a>b)-(a<b)


def v( a, n):
    a1=(a>>(8*n))&255
    return a1

class Color:
   Red = '\033[91m'
   red = '\033[31m'
   Green = '\033[92m'
   green = '\033[32m'
   Yellow = '\033[93m'
   yellow = '\033[33m'
   Blue = '\033[94m'
   blue = '\033[34m'
   Magenta = '\033[95m'
   magenta = '\033[35m'
   Cyan = '\033[96m'
   cyan = '\033[36m'
   Bold = '\033[1m'
   Underline = '\033[4m'
   end = '\033[0m'


class canMsg():
	def __init__(self,id, msg, dlc, flg, timestamp):
		self.id = id
		self.msg = msg
		self.dlc = dlc
		self.flg = flg
		self.timestamp = timestamp


# class PyGuiApp(QtGui.QMainWindow, Gui.Ui_MainWindow):
class PyGuiApp(QMainWindow):
	nachricht = pyqtSignal(canMsg)
	analyseSensor = pyqtSignal()
	def __init__(self):
		# Explaining super is out of the scope of this article
		# So please google it if you're not familar with it
		# Simple reason why we use it here is that it allows us to
		# access variables, methods etc in the design.py file
		super(self.__class__, self).__init__()
		# self.setupUi(self)  # This is defined in design.py file automatically
		loadUi("Gui.ui",self)

		for button in self.findChildren(QtWidgets.QAbstractButton):
			button.setFocusPolicy(QtCore.Qt.NoFocus)
		
		self.actionAbout.triggered.connect(self.aboutBox)
		self.pushButtonGoX0Y0.clicked.connect(self.goX0Y0)
		self.pushButtonGoZmax.clicked.connect(self.goZmax)
		self.pushButtonGoC0.clicked.connect(self.goC0)
		self.pushButtonGoX20.clicked.connect(lambda: self.goX2( printer_pos0_mm ))
		self.pushButtonGoX21.clicked.connect(lambda: self.goX2( printer_pos1_mm ))
		self.pushButtonGoX22.clicked.connect(lambda: self.goX2( printer_pos2_mm ))
		self.pushButtonGoX23.clicked.connect(lambda: self.goX2( printer_pos3_mm ))

		self.pushButtonGo.clicked.connect(self.betterGoTo)


		self.pushButtonMotorXAus.clicked.connect(lambda: self.MotorAus(idX, self.pushButtonMotorXAus.isChecked()))
		self.pushButtonMotorX2Aus.clicked.connect(lambda: self.MotorAus(idX2, self.pushButtonMotorX2Aus.isChecked()))
		self.pushButtonMotorYAus.clicked.connect(lambda: self.MotorAus(idY, self.pushButtonMotorYAus.isChecked()))
		self.pushButtonMotorZAus.clicked.connect(lambda: self.MotorAus(idZ, self.pushButtonMotorZAus.isChecked()))
		self.pushButtonMotorCAus.clicked.connect(lambda: self.MotorAus(idC, self.pushButtonMotorCAus.isChecked()))

		self.pushButtonInitX.clicked.connect(lambda: self.Init(idX))
		self.pushButtonInitX2.clicked.connect(lambda: self.Init(idX2))
		self.pushButtonInitY.clicked.connect(lambda: self.Init(idY))
		self.pushButtonInitZ.clicked.connect(lambda: self.Init(idZ))
		self.pushButtonInitC.clicked.connect(lambda: self.Init(idC))

		self.pushButtonToolTipVacRead.clicked.connect(self.requestSensValue)

		self.pushButtonNotStop.clicked.connect(self.NotStop)
		self.initCAN()
		self.startCANComm()

		self.oldx = 0
		self.oldy = 0
		self.oldz = 100000
		self.oldc = 0
		self.oldx2 = 0
		
		self.offsetX = 0
		self.offsetY = 0
		self.offsetZ = 0
		self.offsetC = 0
				
		# Eigener Lese Thread, um Blockieren des GUIs zum Lesen zu vermeiden.

		self.readThread = GenericThread(self.readMsg)
		self.nachricht.connect(self.analyseCANMsg)
		# self.connect( self, QtCore.SIGNAL("analyse(PyQt_PyObject)"), self.analyseCANMsg ) # Verbinde readMsg mit Analysefunktion
		self.readThread.start()
		# Eigener pos lese Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
		self.readPosThread = GenericThread(self.readPos)
		self.readPosThread.start()  # starte thread um Positionen zu lesen
		self.pushButtonReadPos.clicked.connect(self.readPosThread.start) #jedes mal wenn angeklickt wird, starte pos Thread

		#												HomeX(axe, velMode, homePosition, jogSpeed, searchSpeed, targetPos, targetSpeed):
		#homing threads setup
		self.homeXThread	= GenericThread(lambda:self.Home(idX,	1,		0,	4096,	-4096,		0,8192, self.pushButtonHomeX))
		self.homeX2Thread	= GenericThread(lambda:self.Home(idX2,	1,	-4000, -1792,	512,		0,8192, self.pushButtonHomeX2))
		self.homeYThread	= GenericThread(lambda:self.Home(idY,	1,		0,	4096,	-4096,		0,8192, self.pushButtonHomeY))
		self.homeZThread	= GenericThread(lambda:self.Home(idZ,	0, 100000,	2000,	-4096,	100000,8192, self.pushButtonHomeZ))
		self.homeCThread	= GenericThread(lambda:self.Home(idC,	0,	744,	0,		-4096,		0,8192, self.pushButtonHomeC))
		self.homeAllThread	= GenericThread(self.homeAll)
		self.pushButtonHomeX.clicked.connect(self.homeXThread.start)
		self.pushButtonHomeX2.clicked.connect(self.homeX2Thread.start)
		self.pushButtonHomeY.clicked.connect(self.homeYThread.start)
		self.pushButtonHomeZ.clicked.connect(self.homeZThread.start)
		self.pushButtonHomeC.clicked.connect(self.homeCThread.start)
		self.pushButtonHomeAll.clicked.connect(self.homeAllThread.start)

		# self.pushButtonToolTipVac.clicked.connect(lambda: self.SetActuator(self.pushButtonToolTipVac.isChecked(), "M800", "M801" ))
		# self.pushButtonToolChangerVac.clicked.connect(lambda: self.SetActuator(self.pushButtonToolChangerVac.isChecked(), "M803", "M802" ))
		# self.pushButtonLight.clicked.connect(lambda: self.SetActuator(self.pushButtonLight.isChecked(), "M808", "M809" ))
		# # self.pushButtonUplight.clicked.connect(lambda: self.SetActuator(self.pushButtonUplight.isChecked(), "M806", "M807" ))
		# self.pushButtonJetterDown.clicked.connect(lambda: self.SetActuator(self.pushButtonJetterDown.isChecked(), "M810", "M811" ))
		# self.pushButtonJet.clicked.connect(lambda: self.SetActuator(self.pushButtonJet.isChecked(), "M804", "M805" ))
		# self.pushButtonZClampOff.clicked.connect(lambda: self.SetActuator(self.pushButtonZClampOff.isChecked(), "M806", "M807" ))

		self.pushButtonToolTipVac.clicked.connect(lambda: self.SetActuator(self.pushButtonToolTipVac.isChecked(), "M800", "M801" ))
		self.pushButtonLight.clicked.connect(lambda: self.SetActuator(self.pushButtonLight.isChecked(), "M802", "M803" ))
		self.pushButtonJet.clicked.connect(lambda: self.SetActuator(self.pushButtonJet.isChecked(), "M804", "M805" ))
		self.pushButtonJetterDown.clicked.connect(lambda: self.SetActuator(self.pushButtonJetterDown.isChecked(), "M806", "M807" ))
		self.pushButtonZClampOff.clicked.connect(lambda: self.SetActuator(self.pushButtonZClampOff.isChecked(), "M808", "M809" ))
		self.pushButtonToolChangerVac.clicked.connect(lambda: self.SetActuator(self.pushButtonToolChangerVac.isChecked(), "M810", "M811" ))
		self.pushButtonDispens1.clicked.connect(lambda: self.SetActuator(self.pushButtonDispens1.isChecked(), "M812", "M813" ))
		self.pushButtonDispens2.clicked.connect(lambda: self.SetActuator(self.pushButtonDispens2.isChecked(), "M814", "M815" ))
		self.pushButtonDispensVac1.clicked.connect(lambda: self.SetActuator(self.pushButtonDispensVac1.isChecked(), "M816", "M817" ))
		self.pushButtonDispensVac2.clicked.connect(lambda: self.SetActuator(self.pushButtonDispensVac2.isChecked(), "M818", "M819" ))
		self.pushButtonWorkingVac.clicked.connect(lambda: self.SetActuator(self.pushButtonWorkingVac.isChecked(), "M820", "M821" ))
		self.pushButtonThermodeAn.clicked.connect(lambda: self.SetActuator(self.pushButtonThermodeAn.isChecked(),"M104 S%3d"%(self.spinBoxThermodeSoll.value()), "M104 S40"))  # Fake Ziel 15°C wenn aus
		self.pushButtonBettAn.clicked.connect(lambda: self.SetActuator(self.pushButtonBettAn.isChecked(),"M140 S%3d"%(self.spinBoxBettSoll.value()), "M140 S40")) # Fake Ziel 15°C wenn aus

		self.pushButtonCaptureCoordOffset.clicked.connect(self.CaptureOffset)
		self.pushButtonZeroCoordOffset.clicked.connect(self.ZeroOffset)
		self.pushButtonSetCoordOffset.clicked.connect(self.SetOffset)
		
		
		
		self.pushButtonSendResetCommand.clicked.connect(self.sendResetCommandToSmoothie)
		self.pushButtonSendGcode.clicked.connect(self.sendGcodeToServos)


		self.readTemperaturesThread = GenericThread(self.readTemperatures)
		self.readTemperaturesThread.start()
		self.pushButtonReadTemps.clicked.connect(self.readTemperaturesThread.start)

		self.pushButtonReadSwitches.clicked.connect(self.readSwitches)

		self.pushButtonDispens1Shot.clicked.connect(lambda: self.dispens1Shot(self.spinBoxDispensTime1.value()))
		self.pushButtonDispens2Shot.clicked.connect(lambda: self.dispens2Shot(self.spinBoxDispensTime2.value()))

		self.sendTcpQ = queue.Queue()  #from middleware to openpnp
		self.recTcpQ = queue.Queue()	#from openpnp to middleware
		self.sendSerQ = queue.Queue()  #from middleware to Smothie
		self.recSerQ = queue.Queue()	#from Smothie to middleware
		self.sendSensQ = queue.Queue()  #from middleware to Sensor
		self.recSensQ = queue.Queue()	#from Sensor to middleware
		

		self.startSocketListenerThread = GenericThread( self.startSocketListener)
		self.startSocketListenerThread.start()
		self.startSocketSenderThread = GenericThread( self.startSocketSender)

		self.motionQueueHandlerThread = GenericThread( self.motionQueueHandler )
		self.motionQueueHandlerThread.start()


		# Eigener Joystic Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
		self.initJoysticHW()
		self.joysticThread = GenericThread(self.handleJoystic)
		self.joysticModeThread = GenericThread(self.joysticMode)

		self.pushButtonJoysticMode.clicked.connect(self.joysticThread.start)
		self.pushButtonJoysticMode.clicked.connect(self.joysticModeThread.start)


		# self.status = [ready,ready,ready]
		self.axisSpeed = [0,0,0,0]
		self.axisOldSpeed = [0,0,0,0]
		#
		self.currentPos=[0,0,10,0,0]
		self.StatusReg =[0,0,0,0,0]
		self.MotionStatusReg =[0,0,0,0,0]
		self.VelErr = [0,0,0,0,0]

		#start and init serial communication
		print("trying serial port to smoothie")
		try:
			# self.sbus = serial.Serial('/dev/serial/by-id/usb-Uberclock_Smoothieboard_18FF9019AE1C8C2951EBAC3BF5001E43-if00',115200,timeout=0.100)
			self.sbus = serial.Serial('/dev/serial/by-id/usb-Uberclock_Smoothieboard_03FFA006AF2784085A4EDA47F50020C3-if00',115200,timeout=0.100)
		except:
			print("Smoothie existiert nicht! ich versuche es mit virtuellem serial port")
			try:
				self.sbus = serial.Serial('/dev/pts/2',115200,timeout=0.100)
			except:
				print("Virtueller port geht nicht. lassen wir es sein für heute...")
				exit()
		try:
			self.sbus2 = serial.Serial('/dev/serial/by-id/usb-Arduino__www.arduino.cc__0043_7533531343735131C1C1-if00',115200,timeout=0.100)
		except:
			print("Na, wen haste denn dein Sensorpanel verliehen?")
			exit()

		print('sbus=',self.sbus.name)
		print('sbus2=',self.sbus2.name)

		self.serialReaderThread = GenericThread( self.serialReader)
		self.serialReaderThread.start()


		# self.connect( self, QtCore.SIGNAL("analyseSensor"), self.analyseSensorData )
		self.analyseSensor.connect(self.analyseSensorData)

		self.serialSensorReaderThread = GenericThread( self.serialSensorReader)
		self.serialSensorReaderThread.start()

		self.serialSenderThread = GenericThread( self.serialSender)
		self.serialSenderThread.start()

		# self.serialTestThread = GenericThread( self.serialTest)
		# self.serialTestThread.start()

		self.xyStep = 0.001
		self.zStep = 0.001

		self.verticalSlider_StepsXY.valueChanged.connect(self.AdjustXYStep)
		self.verticalSlider_StepsZ.valueChanged.connect(self.AdjustZStep)

		self.doubleSpinBox_StepsXY.valueChanged.connect(self.SetXYStepValue)
		self.doubleSpinBox_StepsZ.valueChanged.connect(self.SetZStepValue)

		self.pushButton_XM.clicked.connect(lambda: self.ButtonMove(idX, -1))
		self.pushButton_XP.clicked.connect(lambda: self.ButtonMove(idX, 1))
		self.pushButton_YM.clicked.connect(lambda: self.ButtonMove(idY, -1))
		self.pushButton_YP.clicked.connect(lambda: self.ButtonMove(idY, 1))
		self.pushButton_ZM.clicked.connect(lambda: self.ButtonMove(idZ, -1))
		self.pushButton_ZP.clicked.connect(lambda: self.ButtonMove(idZ, 1))
		self.pushButton_CM.clicked.connect(lambda: self.ButtonMove(idC, -1))
		self.pushButton_CP.clicked.connect(lambda: self.ButtonMove(idC, 1))

		self.axisOldSpeed[0] = 0
		self.axisOldSpeed[1] = 0
		self.axisOldSpeed[2] = 0

		self.PosProgramThread = GenericThread(self.PosProgram)

		self.pushButton_Start.clicked.connect(self.StartPosProgram)

		self.pushButton_Pause.toggled.connect(self.PausePosProgram)
		self.pushButton_Stop.clicked.connect(self.StopPosProgram)

		self.DoGoPosThread = GenericThread(self.DoGoPos)
		self.pushButton_GoToPos.clicked.connect(self.DoGoPosThread.start)

		self.pushButton_Capture.clicked.connect(self.CapturePos)
		self.pushButton_ZeileP.clicked.connect(self.ZeileEinfugen)
		self.pushButton_ZeileM.clicked.connect(self.ZeileEntfernen)
		self.pushButton_Load.clicked.connect(self.PrgLaden)
		self.pushButton_Save.clicked.connect(self.PrgSpeichern)

		self.PrgRunning = False
		self.lastpath = '.'
		self.PrgPaused = False

		self.thermodeTemp = 0
		self.bettTemp = 0

	def keyPressEvent(self, event):
		if (event.key() == Qt.Key_Escape):
			print("Notstop!!! Escape")
			self.NotStop()
		elif (event.key() == Qt.Key_Space):
			print("Notstop!!! Space")
			self.NotStop()
		 		

	def SetOffset(self):

		self.offsetX = self.spinBoxOffsetX.value()
		self.offsetY = self.spinBoxOffsetY.value()
		self.offsetZ = self.spinBoxOffsetZ.value()
		self.offsetC = self.spinBoxOffsetC.value()
		print("offsets: ",self.offsetX, self.offsetY, self.offsetZ, self.offsetC)
					


	def ZeroOffset(self):
		self.offsetX = 0
		self.offsetY = 0
		self.offsetZ = 0
		self.offsetC = 0
		self.spinBoxOffsetX.setValue(0)
		self.spinBoxOffsetY.setValue(0)
		self.spinBoxOffsetZ.setValue(0)
		self.spinBoxOffsetC.setValue(0)


	def CaptureOffset(self):
		self.readPosOnce()
		time.sleep(0.2)
		self.captureOldPos()
		self.spinBoxOffsetX.setValue(self.oldx)
		self.spinBoxOffsetY.setValue(self.oldy)
		self.spinBoxOffsetZ.setValue(self.oldz-100000)
		self.spinBoxOffsetC.setValue(self.oldc)
		self.SetOffset()
	
		

	def sendResetCommandToSmoothie(self):
		command = self.plainTextEditResetCommand.toPlainText() + "\n"
		print("sending command to smoothie:\n",command)
		self.sendSerQ.put(command.encode("utf-8"))
		
	def sendGcodeToServos(self):
		command = self.plainTextEditGcode.toPlainText() + "\n"
		print("sending command to servos:\n",command)
#		self.analyseSocketData(command.encode("utf-8"))
		self.recTcpQ.put(command.encode("utf-8"))

	def dispens1Shot(self, duration):
		print("dispensshot1 for duration ", duration)
		self.SetActuator(True, "M812", "M813" )
		time.sleep(duration/1000)
		self.SetActuator(False, "M812", "M813" )

	def dispens2Shot(self, duration):
		print("dispensshot2 for duration ", duration)
		self.SetActuator(True, "M814", "M815" )
		time.sleep(duration/1000)
		self.SetActuator(False, "M814", "M815" )


	def readSwitches(self):
		data = "M119\n"
		self.sendSerQ.put(data.encode("utf-8"))

	def readTemperatures(self):
		while( not hasattr(self, "sendSerQ") ):
			time.sleep(1) #warten bis wir ein sendSerQ haben
		while (self.pushButtonReadTemps.isChecked()):
			data = "M105\nM141\n"
			self.sendSerQ.put(data.encode("utf-8"))
			time.sleep(0.25)


	def homeAll(self):
		self.pushButtonHomeZ.click()
		while self.pushButtonHomeZ.isChecked():
			print("waiting for z to finish ")
			time.sleep(1)
		self.pushButtonHomeX.click()
		#self.pushButtonHomeX2.setChecked(True)
		self.pushButtonHomeY.click()
		self.pushButtonHomeC.click()
		while self.pushButtonHomeX.isChecked() or self.pushButtonHomeY.isChecked() or self.pushButtonHomeC.isChecked():
			print("waiting for rest to finish ")
			time.sleep(1)


	def betterGoTo(self):
		self.readPosOnce()
		time.sleep(0.05) # war 0.2
		self.captureOldPos()
		self.goTo()

	def PosProgram(self) :
		self.PrgRunning = True
		for row in range(self.tableWidget_Positionen.rowCount()):
			if self.PrgRunning == False:
				break
			waiting = 0
			while self.PrgPaused == True :
				waiting = waiting + 1
				if waiting % 10 == 0 :
					print("waiting %05d"%(waiting/10), end="\r")
				time.sleep(0.05)
			else :
				print("Finished waiting")
			if self.PrgRunning : #Still running?
				self.tableWidget_Positionen.setCurrentCell(row,0)
				self.DoGoPos()
		self.PrgRunning = False

	def StartPosProgram(self) :
		if not self.PrgRunning:
			print("starte position program")
			self.PosProgramThread.start()
		else:
			print("Programm läuft schon!")


	def PausePosProgram(self, value) :
		# if self.pushButton_Pause.isChecked():
		if value:
			print("Pause position program")
			self.PrgPaused = True
		else:
			print("Resume position program")
			self.PrgPaused = False

	def StopPosProgram(self) :
		print("stop position program")
		self.PrgRunning = False
		self.StopAll()

	def DoGoPos(self) :
		row = self.tableWidget_Positionen.currentRow()
		if row == -1 : row = 0
		print("Going to position laut Zeile: ", row)
		X = float(self.tableWidget_Positionen.item(row,0).text())
		Y = float(self.tableWidget_Positionen.item(row,1).text())
		Z = float(self.tableWidget_Positionen.item(row,2).text())
		Speed = float(self.tableWidget_Positionen.item(row,3).text())
		Pause = float(self.tableWidget_Positionen.item(row,4).text())
		Dispenser = float(self.tableWidget_Positionen.item(row,5).text())

		data = "G1 Z%0.3f F%0.3f\nM400\n"%(Z,Speed)   # first move Z to avoid collision
		print(data)
#		self.analyseSocketData(data.encode("utf-8"))
		self.recTcpQ.put(data.encode("utf-8"))
		
		if Dispenser == 0 : # no dispensing
			data = "G1 X%0.3f Y%0.3f F%0.3f\nM400\n"%(X,Y,Speed)  #then move in XY
		if Dispenser == 1 : # dispensing 1
			data = "M812\nM802\nG1 X%0.3f Y%0.3f F%0.3f\nM400\nM813\nM803\n"%(X,Y,Speed)  #then move in XY
		if Dispenser == 2 : # dispensing 2
			data = "M814\nM802\nG1 X%0.3f Y%0.3f F%0.3f\nM400\nM815\nM803\n"%(X,Y,Speed)  #then move in XY
		print(data)
#		self.analyseSocketData(data.encode("utf-8"))
		self.recTcpQ.put(data.encode("utf-8"))
		
#		self.pushButtonJet.setChecked(False)
#		self.pushButtonDispens1.setChecked(False)
#		self.pushButtonDispens2.setChecked(False)

#		data = "M813\nM815\nM803\n"
#		print(data)
##		self.analyseSocketData(data.encode("utf-8"))
#		self.recTcpQ.put(data.encode("utf-8"))		

		if Pause == -1 :
			self.PrgPaused = True
			self.pushButton_Pause.setChecked(True)
		if Pause >= 2 :
			time.sleep(Pause/1000)


	def CapturePos(self) :
		row = self.tableWidget_Positionen.currentRow()
		print("capturing current position to current row: ", row)
		print(self.currentPos)
		if row > -1 :
			self.tableWidget_Positionen.setItem(row, 0, QtWidgets.QTableWidgetItem("%1.3f"%(self.currentPos[0]/Xm)))
			self.tableWidget_Positionen.setItem(row, 1, QtWidgets.QTableWidgetItem("%1.3f"%(self.currentPos[1]/Ym)))
			self.tableWidget_Positionen.setItem(row, 2, QtWidgets.QTableWidgetItem("%1.3f"%(self.currentPos[2]/Zm-50.0)))
			self.tableWidget_Positionen.setItem(row, 3, QtWidgets.QTableWidgetItem("2000"))
			self.tableWidget_Positionen.setItem(row, 4, QtWidgets.QTableWidgetItem("-1")) # default is we pause at every movement
			self.tableWidget_Positionen.setItem(row, 5, QtWidgets.QTableWidgetItem("0")) # default is we do not dispense
		else :
			print("wohin? wähle Zeile aus!")

	def ZeileEinfugen(self) :
		print("ZeileEinfügen in: ")
		if self.PrgRunning == False :
			row = self.tableWidget_Positionen.currentRow()
			rowcount = self.tableWidget_Positionen.rowCount()
			if row > -1 :
				print("Füge Zeile ein über Zeile", row)
				self.tableWidget_Positionen.insertRow(row)
			else :
				print("Füge Zeile ans Ende ein")
				self.tableWidget_Positionen.insertRow(rowcount)
		else:
			print("Nicht wenn grade BewegungsProgramm läuft!")

	def ZeileEntfernen(self) :
		print("ZeileEntfernen von")
		if self.PrgRunning == False :
			row = self.tableWidget_Positionen.currentRow()
			rowcount = self.tableWidget_Positionen.rowCount()
			if row > -1 :
				print("Entferne Zeile", row)
				self.tableWidget_Positionen.removeRow(row)
			else :
				print("Entferne letzte Zeile")
				self.tableWidget_Positionen.removeRow(rowcount-1)
		else:
			print("Nicht wenn grade BewegungsProgramm läuft!")


	def PrgSpeichern(self) :
		print("PrgSpeichern")
		saveFileName, extension = QtWidgets.QFileDialog.getSaveFileName(self, 'Save Speed Program',  self.lastpath ,'*.csv')
		print(saveFileName)
		if saveFileName:
			self.lastpath = os.path.dirname(saveFileName)
			with open(saveFileName,'w', newline='') as f:
				fieldnames = [ "X", "Y", "Z", "Speed","Pause","Dispensen"]
				writer = csv.DictWriter(f,fieldnames=fieldnames, delimiter='\t')
				writer.writeheader()
				for row in range(self.tableWidget_Positionen.rowCount()):
					writer.writerow({"X":self.tableWidget_Positionen.item(row,0).text(), "Y":self.tableWidget_Positionen.item(row,1).text(), "Z": self.tableWidget_Positionen.item(row,2).text(), "Speed": self.tableWidget_Positionen.item(row,3).text(), "Pause": self.tableWidget_Positionen.item(row,4).text(), "Dispensen": self.tableWidget_Positionen.item(row,5).text()})
				f.close()

	def PrgLaden(self) :
		print("PrgLaden")
		fileName , extension = QtWidgets.QFileDialog.getOpenFileName(self, 'Load Speed Program',  self.lastpath ,'*.csv')
		if fileName:
			self.lastpath = os.path.dirname(fileName)
			print (fileName)
			with open(fileName,'r', newline='') as f:
				programreader = csv.DictReader(f, delimiter='\t')
				self.tableWidget_Positionen.setRowCount(0)
				rowcount=0
				self.tableWidget_Positionen.setSortingEnabled(False)
				for row in programreader :
					print(row)
					print(row['X'], row['Y'], row['Z'], row['Speed'], row['Pause'], row['Dispensen'])
					self.tableWidget_Positionen.insertRow(rowcount)
					self.tableWidget_Positionen.setItem(rowcount, 0, QtWidgets.QTableWidgetItem(row['X']))
					self.tableWidget_Positionen.setItem(rowcount, 1, QtWidgets.QTableWidgetItem(row['Y']))
					self.tableWidget_Positionen.setItem(rowcount, 2, QtWidgets.QTableWidgetItem(row['Z']))
					self.tableWidget_Positionen.setItem(rowcount, 3, QtWidgets.QTableWidgetItem(row['Speed']))
					self.tableWidget_Positionen.setItem(rowcount, 4, QtWidgets.QTableWidgetItem(row['Pause']))
					self.tableWidget_Positionen.setItem(rowcount, 5, QtWidgets.QTableWidgetItem(row['Dispensen']))
					rowcount = rowcount + 1
				# self.tableWidget_Positionen.setRowCount(rowcount)
				self.tableWidget_Positionen.sortByColumn(-1, Qt.AscendingOrder)
				self.tableWidget_Positionen.setSortingEnabled(True)
			f.close()
		# print (self.parameters)




	def AdjustXYStep(self, value):
		table = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000]
		self.doubleSpinBox_StepsXY.setValue(0.001 * table[value])

	def AdjustZStep(self, value):
		table = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000,20000,50000,100000]
		self.doubleSpinBox_StepsZ.setValue(0.001 * table[value])

	def SetXYStepValue(self, value):
		self.xyStep = value
		print("new xystep value: ", self.xyStep )

	def SetZStepValue(self, value):
		self.zStep = value
		print("new zcstep value: ", self.zStep )

	def ButtonMove(self, axe, direction):
		if axe == idZ:
			Step = self.zStep * direction * Zm
			Speed = self.Vmaxsetf.value() / 1000 * Zm
		if axe == idC:
			Step = self.zStep * direction * Cm
			Speed = self.Vmaxsetf.value() / 1000 * Cm
		if axe == idX:
			Step = self.xyStep * direction * Xm
			Speed = self.Vmaxsetf.value() / 1000 * Xm
		if axe == idY:
			Step = self.xyStep * direction * Ym
			Speed = self.Vmaxsetf.value() / 1000 * Ym
		self.goRelPrepare(axe, int(Step), int(Speed))
		self.goDo(axe)

	def SetActuator(self,value,OnCommand,OffCommand):
		if value :
			data = OnCommand+"\n"
		else :
			data = OffCommand+"\n"
		self.sendSerQ.put(data.encode("utf-8"))

	def MotorAus(self, axe, isChecked):
		self.sendElmoMsgLong(axe, "MO",0, isChecked) #mo = 0 motor off

	def NotStop(self):
		self.sendElmoMsgLong(idX, "MO",0,0 ) # mo = 0 motor off
		self.sendElmoMsgLong(idX2,"MO",0,0 )
		self.sendElmoMsgLong(idY, "MO",0,0 )
		self.sendElmoMsgLong(idZ, "MO",0,0 )
		self.sendElmoMsgLong(idC, "MO",0,0 )

	def StopAll(self): # without loosing control stop all
		self.sendElmoMsgShort(idX, "ST",0 ) # STop
		self.sendElmoMsgShort(idX2,"ST",0 )
		self.sendElmoMsgShort(idY, "ST",0 )
		self.sendElmoMsgShort(idZ, "ST",0 )
		self.sendElmoMsgShort(idC, "ST",0 )

	def initJoysticHW(self):
		#Iterate over the joystick devices.
		print('Available devices:')

		for self.fn in os.listdir('/dev/input'):
			if self.fn.startswith('js'):
				print('  /dev/input/%s' % (self.fn))

		# We'll store the states here.
		self.axis_states = {}
		self.button_states = {}

		# These constants were borrowed from linux/input.h
		self.axis_names = {
			0x00 : 'x',
			0x01 : 'y',
			0x02 : 'z',
			0x03 : 'rx',
			0x04 : 'ry',
			0x05 : 'rz',
			0x06 : 'trottle',
			0x07 : 'rudder',
			0x08 : 'wheel',
			0x09 : 'gas',
			0x0a : 'brake',
			0x10 : 'hat0x',
			0x11 : 'hat0y',
			0x12 : 'hat1x',
			0x13 : 'hat1y',
			0x14 : 'hat2x',
			0x15 : 'hat2y',
			0x16 : 'hat3x',
			0x17 : 'hat3y',
			0x18 : 'pressure',
			0x19 : 'distance',
			0x1a : 'tilt_x',
			0x1b : 'tilt_y',
			0x1c : 'tool_width',
			0x20 : 'volume',
			0x28 : 'misc',
		}

		self.button_names = {
			0x120 : 'trigger',
			0x121 : 'thumb',
			0x122 : 'thumb2',
			0x123 : 'top',
			0x124 : 'top2',
			0x125 : 'pinkie',
			0x126 : 'base',
			0x127 : 'base2',
			0x128 : 'base3',
			0x129 : 'base4',
			0x12a : 'base5',
			0x12b : 'base6',
			0x12f : 'dead',
			0x130 : 'a',
			0x131 : 'b',
			0x132 : 'c',
			0x133 : 'x',
			0x134 : 'y',
			0x135 : 'z',
			0x136 : 'tl',
			0x137 : 'tr',
			0x138 : 'tl2',
			0x139 : 'tr2',
			0x13a : 'select',
			0x13b : 'start',
			0x13c : 'mode',
			0x13d : 'thumbl',
			0x13e : 'thumbr',

			0x220 : 'dpad_up',
			0x221 : 'dpad_down',
			0x222 : 'dpad_left',
			0x223 : 'dpad_right',

			# XBox 360 controller uses these codes.
			0x2c0 : 'dpad_left',
			0x2c1 : 'dpad_right',
			0x2c2 : 'dpad_up',
			0x2c3 : 'dpad_down',
		}

		self.axis_map = []
		self.button_map = []

		# Open the joystick device.
		self.fn = '/dev/input/js0'
		print('Opening %s...' % self.fn)
		try:
			self.jsdev = open(self.fn, 'rb')

			# Get the device name.
			#buf = bytearray(63)
			buf = array.array('B', [0] * 64)
			ioctl(self.jsdev, 0x80006a13 + (0x10000 * len(buf)), buf) # JSIOCGNAME(len)
			self.js_name = buf.tostring()
			print('Device name: %s' % self.js_name)

			# Get number of axes and buttons.
			buf = array.array('B', [0])
			ioctl(self.jsdev, 0x80016a11, buf) # JSIOCGAXES
			self.num_axes = buf[0]

			buf = array.array('B', [0])
			ioctl(self.jsdev, 0x80016a12, buf) # JSIOCGBUTTONS
			self.num_buttons = buf[0]

			# Get the axis map.
			buf = array.array('B', [0] * 0x40)
			ioctl(self.jsdev, 0x80406a32, buf) # JSIOCGAXMAP

			for axis in buf[:self.num_axes]:
				axis_name = self.axis_names.get(axis, 'unknown(0x%02x)' % axis)
				self.axis_map.append(axis_name)
				self.axis_states[axis_name] = 0.0

			# Get the button map.
			buf = array.array('H', [0] * 200)
			ioctl(self.jsdev, 0x80406a34, buf) # JSIOCGBTNMAP

			for btn in buf[:self.num_buttons]:
				btn_name = self.button_names.get(btn, 'unknown(0x%03x)' % btn)
				self.button_map.append(btn_name)
				self.button_states[btn_name] = 0

			print ('%d axes found: %s' % (self.num_axes, ', '.join(self.axis_map)))
			print ('%d buttons found: %s' % (self.num_buttons, ', '.join(self.button_map)))
			self.joysticfound = True
		except:
			self.joysticfound = False
			print("No joystic found")

	# Main Joystic event loop
	def handleJoystic(self):
		while self.joysticfound and self.pushButtonJoysticMode.isChecked():
			evbuf = self.jsdev.read(8)
			if evbuf:
				timestamp, value, type, number = struct.unpack('IhBB', evbuf)

				if type & 0x80:
					 print ("(initial)",end="")

				if type & 0x01:
					button = self.button_map[number]
					if button:
						self.button_states[button] = value
						#if value:
						#	print ("%s pressed" % (button))
						#else:
						#	print ("%s released" % (button))

				if type & 0x02:
					axis = self.axis_map[number]
					fvalue = value# / 32767.0
					self.axis_states[axis] = fvalue #store value state
					#print("%s : %.6f" % (axis, fvalue),end="\r")
		print("Jostic mode off 1")

	def joysticMode(self):
		self.StopAll() #stop everything first.
		self.axisOldSpeed = [0,0,0,0]

		while self.joysticfound and self.pushButtonJoysticMode.isChecked() :

			self.axisSpeed[0] = self.axis_states['x'] #/ 32767
			self.axisSpeed[1] = -self.axis_states['y'] #/ 32767
			self.axisSpeed[2] = -self.axis_states['ry'] #/ 32767
			self.axisSpeed[3] = -self.axis_states['rx'] #/ 32767
			print(self.axisSpeed, end='')
			#for i in range(0,3):

			for i in range(0,4):
				Speed = self.axisSpeed[i]
				aSpeed = abs(Speed)
				if aSpeed < threshold :
					direction = 0
					Speed = 0
				elif Speed > threshold :
					Speed = Speed - threshold
					direction = 1
				elif Speed < -threshold:
					Speed = Speed + threshold
					direction = -1

				Speedset = int(self.Vmaxsetf.value() * abs(Speed) / (32767-threshold))
				print(" %d %d %d "%(Speed, Speedset, direction), end='')
				if Speed == 0 and self.axisOldSpeed[i] != 0 :
					self.sendElmoMsgShort(axes[i], "ST",0 )
				else:
					if direction > 0 :
						self.go(axes[i], maximum[i], Speedset)
					elif direction < 0 :
						self.go(axes[i], minimum[i], Speedset)

				self.axisOldSpeed[i] = Speed

			print(20*' ', end='\r')

			time.sleep(0.02) # wait 20ms
		print("")
		self.StopAll() #stop everything.
		self.readPosOnce()
		time.sleep(0.3)
		self.updateSetPos()

		print("Jostic mode off 2")


	def updateSetPos(self):
		self.X1set.setValue(self.currentPos[0])
		self.Yset.setValue(self.currentPos[1])
		self.Zset.setValue(self.currentPos[2])
		self.Cset.setValue(self.currentPos[3])
		self.X2set.setValue(self.currentPos[4])

	def readPosOnce(self) :
		self.sendElmoMsgShort(idX, "PX",0)# get pos
		self.sendElmoMsgShort(idX2,"PX",0)# get pos
		self.sendElmoMsgShort(idY, "PX",0)# get pos
		self.sendElmoMsgShort(idZ, "PX",0)# get pos
		self.sendElmoMsgShort(idC, "PX",0)# get pos
		time.sleep(0.015)
	
	def getX2Pos(self) :
	
		res = requests.get(f"{PRINTER}/components/TableSlots/TableSlots/TableSlotLeft/Axis")
		data = res.json()
		busy = data["busy"]
		inpos = data["inPosition"]
		pos = data["position"]
		print(f"{pos} mm busy: {busy} inpos: {inpos}",end="\r")
		self.lcdNumberDROPosX2f.display(pos)

	def readPos(self) :
		readcounter = 0
		while self.pushButtonReadPos.isChecked()	:
			self.readPosOnce()
			readcounter = readcounter + 1
			if (readcounter % 20) == 0 :  # um nicht so oft zu lesen
				self.getX2Pos()

	def analyseCANMsg(self,msg):
#		if self.pushButtonCanlog.isChecked() :
#			displayText = "%03x %02x %01d   :" % (msg.id, msg.flg, msg.dlc)
#			for j in range(0,msg.dlc) :
#				displayText = displayText + " %02x" % ( msg.msg[j] )
#			displayText = displayText + ":"
#			self.plainTextEditCanLog.appendPlainText(displayText)
			# print(displayText)
		if (msg.msg[0] == 0x50) and (msg.msg[1] == 0x58) : # PX = ?
			pos = msg.msg[4]+(msg.msg[5]<<8)+(msg.msg[6]<<16)+(msg.msg[7]<<24)
			if (pos & 0x80000000) :
				pos = -(0x100000000 - pos)  # wir sind negative Zahl!
			if msg.id == idRx+idX :
				#print("posX :", pos)
				self.lcdNumberDROPosX.display(pos)
				self.lcdNumberDROPosXf.display(pos / Xm)
				self.currentPos[0] = pos
				if self.pushButtonUseOffset.isChecked()	:	
					self.currentPos[0] = self.currentPos[0] -self.offsetX
			if msg.id == idRx+idY :
				#print("posY :", pos)
				self.lcdNumberDROPosY.display(pos)
				self.lcdNumberDROPosYf.display(pos / Ym)
				self.currentPos[1] = pos
				if self.pushButtonUseOffset.isChecked()	:	
					self.currentPos[1] = self.currentPos[1] -self.offsetY
			if msg.id == idRx+idZ :
				#print("posZ :", pos)
				self.lcdNumberDROPosZ.display(pos)
				self.lcdNumberDROPosZf.display(-50.0+pos / Zm)
				self.currentPos[2] = pos
				if self.pushButtonUseOffset.isChecked()	:	
					self.currentPos[2] = self.currentPos[2] -self.offsetZ
			if msg.id == idRx+idC :
				#print("posC :", pos)
				self.lcdNumberDROPosC.display(pos)
				self.lcdNumberDROPosCf.display(pos / Cm)
				self.currentPos[3] = pos
				if self.pushButtonUseOffset.isChecked()	:	
					self.currentPos[3] = self.currentPos[3] -self.offsetC
			if msg.id == idRx+idX2 :
				#print("posX :", pos)
				self.lcdNumberDROPosX2.display(pos)
				self.lcdNumberDROPosX2f.display(pos / X2m)
				self.currentPos[4] = pos
		if (msg.msg[0] == 0x56) and (msg.msg[1] == 0x45) : # VE = velocity error for boundary homing
			VelErr = msg.msg[4]+(msg.msg[5]<<8)+(msg.msg[6]<<16)+(msg.msg[7]<<24)
			if (VelErr & 0x80000000) :  # 64 bit negative numbers conversion to 32 bit
				VelErr = -(0x100000000 - VelErr)  # wir sind negative Zahl!
#			print("velocity error: ", VelErr)
			if msg.id == idRx+idX :
				self.VelErr[0] = VelErr
			if msg.id == idRx+idY :
				self.VelErr[1] = VelErr
			if msg.id == idRx+idZ :
				self.VelErr[2] = VelErr
			if msg.id == idRx+idC :
				self.VelErr[3] = VelErr
			if msg.id == idRx+idX2 :
				self.VelErr[4] = VelErr
		if (msg.msg[0] == 0x53) and (msg.msg[1] == 0x52) : # SR = Status register for homing
			StatusReg = msg.msg[4]+(msg.msg[5]<<8)+(msg.msg[6]<<16)+(msg.msg[7]<<24)
#			print("Status Register: " , bin(StatusReg))
			if msg.id == idRx+idX :
				self.StatusReg[0] = StatusReg
			if msg.id == idRx+idY :
				self.StatusReg[1] = StatusReg
			if msg.id == idRx+idZ :
				self.StatusReg[2] = StatusReg
			if msg.id == idRx+idC :
				self.StatusReg[3] = StatusReg
			if msg.id == idRx+idX2 :
				self.StatusReg[4] = StatusReg

		if (msg.msg[0] == 0x4D) and (msg.msg[1] == 0x53) : # MS = Motion Status
			motionStatus = msg.msg[4]+(msg.msg[5]<<8)+(msg.msg[6]<<16)+(msg.msg[7]<<24)
#			print("Motion Status: ", motionStatus, end="")
			for axe in axes:
				if msg.id == idRx+axe :
					self.MotionStatusReg[self.whichAxe(axe)] = motionStatus
#					print(axe,":", motionStatus, end="  ")
#			print(".")


	def readMsg(self):
		while True:
			try:
				idr, msgr, dlc, flg, timestamp = self.handle1.read(int(1))
				canmsg = canMsg(idr, msgr, dlc, flg, timestamp)
				# self.emit( QtCore.SIGNAL("analyse(PyQt_PyObject)"), canmsg )
				self.nachricht.emit(canmsg)
			except (canlib.canNoMsg) as ex:
				None
			except (canlib.canError) as ex:
				print (ex)

	def Init(self,axe):
		self.sendElmoMsgLong(axe, "MO", 0, 0 ) #mo = 0 motor off
		self.sendElmoMsgLong(axe, "PX", 0, 0 ) #px = 0 set PX
		self.sendElmoMsgLong(axe, "PY", 0, 0 ) #py = 0 set aux position
		self.sendElmoMsgLong(axe, "UM", 0, 5 ) #um = 5 (position mode)
		time.sleep(0.05)
		self.sendElmoMsgLong(axe, "AC",0,maxAcceleration[self.whichAxe(axe)] ) #ac = acceleration
		self.sendElmoMsgLong(axe, "DC",0,maxDeceleration[self.whichAxe(axe)] ) #dc = deceleration
		self.sendElmoMsgLong(axe, "SD",0,maxAcceleration[self.whichAxe(axe)] * 10 ) #sd = emergency stop deceleration
		self.sendElmoMsgLong(axe, "SF",0,smoothingFactor ) #sf = smoothing factor in ms...
		time.sleep(0.05)

	def whichAxe(self,axe):
		if axe == idX:
			return 0
		if axe == idY:
			return 1
		if axe == idZ:
			return 2
		if axe == idC:
			return 3
		if axe == idX2:
			return 4

	def Home(self, axe, velMode, homePosition, jogSpeed, searchSpeed, targetPos, targetSpeed, button):
		if velMode == 1:
			self.sendElmoMsgLong(axe, "MO", 0, 0) #mo = 0 motor off
			time.sleep(0.1)
			self.sendElmoMsgLong(axe, "UM", 0, 2) #um = 2 (velocity mode)
			time.sleep(0.1)
		# if velMode == 2:
			# self.sendElmoMsgLong(axe, "MO", 0, 0) #mo = 0 motor off
			# time.sleep(0.1)
			# self.sendElmoMsgLong(axe, "UM", 0, 3) #um = 3 (microstepping mode)
			# time.sleep(0.1)

		self.sendElmoMsgLong(axe, "MO", 0, 1) #mo = 1 motor on
		time.sleep(0.2)

		self.sendElmoMsgLong(axe, "HM", 2, homePosition)
		self.sendElmoMsgLong(axe, "HM", 3, 3)#hm[3] = 3 Configures the homing function to be triggered by the Index.
		self.sendElmoMsgLong(axe, "HM", 5, 0)#hm[5] = 0 The PX counter will be set to a predefined constant number HM[2]
		self.sendElmoMsgLong(axe, "HM", 4, 0)#HM[4] = 0 Stop motion after homing.

		if jogSpeed != 0:
			self.sendElmoMsgLong(axe, "JV", 0, jogSpeed)
			self.sendElmoMsgShort(axe,"BG", 0)
			time.sleep(0.2)

			ts = time.time()
			self.VelErr[self.whichAxe(axe)] = 0

			while (time.time()-ts) < 10 :
				self.sendElmoMsgShort(axe, "VE",0 ) #VE = ?
				# self.sendMsg(idTx+axe, (0x56,0x45,0,0 )) #VE = ?
				print ("velocity error :", abs(self.VelErr[self.whichAxe(axe)]), end="\r")
				if abs(self.VelErr[self.whichAxe(axe)]) >= jogSpeed :
					break

			self.sendElmoMsgShort(axe, "ST",0 ) #STop
		time.sleep(0.2)

		self.sendElmoMsgLong(axe, "HM", 1,1 ) #HM[1] = 1: arm homing
		self.sendElmoMsgLong(axe, "JV", 0, searchSpeed)
		self.sendElmoMsgShort(axe,"BG", 0)
		time.sleep(0.2)

		ts = time.time()
		self.StatusReg[self.whichAxe(axe)] = 0xffffffff # muß sein, damit ich auf Antworten warte
		while (time.time()-ts) < 10 :
			self.sendElmoMsgShort(axe,"SR", 0 ) #SR = ?
			print ("status: ", (self.StatusReg[self.whichAxe(axe)] & (1<<11))>>11, end="      \r")
			if not(self.StatusReg[self.whichAxe(axe)] & (1<<11)) : #checking if homing ready
				break

		self.sendElmoMsgShort(axe, "ST", 0 ) #STop
		time.sleep(0.2)

		if velMode :  #switch back to position mode
			self.sendElmoMsgLong(axe, "MO",0,0) #mo = 0 motor off
			time.sleep(0.2)
			self.sendElmoMsgLong(axe, "UM",0,5) #um = 5 (position mode)
			self.sendElmoMsgLong(axe, "MO",0,1) #mo = 1 motor on
			time.sleep(0.2)

		self.go(axe, targetPos, targetSpeed)

		button.setChecked(False)

	def goDo(self, axe):
		self.sendElmoMsgShort(axe, "BG",0 ) #BeGin

	def goPrepare(self, axe, target, speed):
		self.sendElmoMsgLong(axe, "PA",0,target) #pa = target set position goal to target
		self.sendElmoMsgLong(axe, "SP",0,speed ) #sp = speed set speed

	def goRelPrepare(self, axe, target, speed):
		self.sendElmoMsgLong(axe, "PR",0,target) #pr = target set relative position goal to target
		self.sendElmoMsgLong(axe, "SP",0,speed ) #sp = speed set speed

	def go(self, axe, target, speed):
		self.goPrepare(axe,target,speed)
		self.goDo(axe)

	def goX0Y0(self):
		self.go(idX, 0, 8192)
		self.go(idY, 0, 8192)

	def goZmax(self):
		self.go(idZ, 100000, 8192) # go to 100000 with speed 8192

	def goC0(self):
		self.go(idC, 0, 4096) # go to 0 with speed 4096

	def goX2(self, X2TargetPosition):
#		self.go(idX2, 7500, 4096) # go to 7500 with speed 4096
		data = {
			"Axis": printer_axis_name,
			"Position": X2TargetPosition,
			"Speed": printer_speed_mmps
		}
		print("Sending", json.dumps(data, indent=4, sort_keys=True))
		res = requests.post(f"{PRINTER}/functions/moveAxis", json=data)
		if res.status_code != 200:
			print(f"Statuscode: {res.status_code}")
		else:
		    print("Result", json.dumps(res.json(), indent=4, sort_keys=True))

		
		
		
	# go to a defined 5 dimension coordinate with the specified speed
	def goTo(self):
		
		x = self.X1set.value()
		y = self.Yset.value()
		z = self.Zset.value()
		c = self.Cset.value()
	#	x2 = self.X2set.value()

#		if self.pushButtonUseOffset.isChecked()	:
#			x = x + self.offsetX
#			y = y + self.offsetY
#			z = z + self.offsetZ
#			c = c + self.offsetC



		vmax = self.Vmaxset.value()
#		print(" target x: %d, y: %d, z: %d, c: %d, x2: %d, vmax: %d" % (x,y,z,c,x2,vmax))
		print(" target x: %d, y: %d, z: %d, c: %d, vmax: %d" % (x,y,z,c,vmax))		
#		if self.pushButtonUseOffset.isChecked()	:
#			dx = abs(self.oldx + self.offsetX - x)
#			dy = abs(self.oldy + self.offsetY - y)
#			dz = abs(self.oldz + self.offsetZ - z)
#			dc = abs(self.oldc + self.offsetC - c)
#			dx2 = abs(self.oldx2 - x2)

#		else:
		dx = abs(self.oldx - x)
		dy = abs(self.oldy - y)
		dz = abs(self.oldz - z)
		dc = abs(self.oldc - c)
#			dx2 = abs(self.oldx2 - x2)

#		distance = math.sqrt(dx*dx+dy*dy+dz*dz+dc*dc+dx2*dx2)
		distance = math.sqrt(dx*dx+dy*dy+dz*dz+dc*dc)		
		print("distance: ",distance, dx, dy, dz, dc)
		if distance == 0: # division by zero means no good. and we dont move.
			return
		vx = int(vmax * dx/distance)
		vy = int(vmax * dy/distance)
		vz = int(vmax * dz/distance)
		vc = int(vmax * dc/distance)
#		vx2 = int(vmax * dx2/distance)
#		if vx2 >= 12500 :
#			vx2 = 12500
#		print("speed: x: %d, y: %d, z: %d, c: %d, x2: %d" % (vx,vy,vz,vc,vx2))
		print("speed: x: %d, y: %d, z: %d, c: %d" % (vx,vy,vz,vc))
		#preparing takes some time to send
		
		if self.pushButtonUseOffset.isChecked()	:		
			if dx != 0 : self.goPrepare(idX, x + self.offsetX, vx)
			if dy != 0 : self.goPrepare(idY, y + self.offsetY, vy)
			if dz != 0 : self.goPrepare(idZ, z + self.offsetZ, vz)
			if dc != 0 : self.goPrepare(idC, c + self.offsetC, vc)
	#		if dx2 != 0 : self.goPrepare(idX2, x2, vx2)
		else:
			if dx != 0 : self.goPrepare(idX, x, vx)
			if dy != 0 : self.goPrepare(idY, y, vy)
			if dz != 0 : self.goPrepare(idZ, z, vz)
			if dc != 0 : self.goPrepare(idC, c, vc)
		

		# since we do not use synchronous start of movement, we try to start like this as synchronous as possible
		if dx != 0 : self.goDo(idX)
		if dy != 0 : self.goDo(idY)
		if dz != 0 : self.goDo(idZ)
		if dc != 0 : self.goDo(idC)
#		if dx2 != 0 :self.goDo(idX2)

#		if self.pushButtonUseOffset.isChecked()	:
		self.oldx	= x
		self.oldy	= y
		self.oldz	= z
		self.oldc	= c
#			self.oldx2	= x2
#		else:
#			self.oldx	= x - self.offsetX
#			self.oldy	= y - self.offsetY
#			self.oldz	= z - self.offsetZ
#			self.oldc	= c - self.offsetC
#			self.oldx2	= x2



	def aboutBox(self):
		QtWidgets.QMessageBox.about(self,"Über dieses Programm", '''
		Dies ist ein Programm zum Testen und Benutzen einer PnP Maschine mit Elmo Motion Cello Controllern und Smoothieware.
		Die Maschine besteht aus X, (X2), Y, Z, und C Achsen und sollte eigentlich mit OpenPnP zusammenarbeiten,um Pick and Place Aufgaben zu lösen.
		Dieses Programm basiert massiv auf manche Beispiele von Kvaser Canlib, Elmo Cello Motion und auch die Joystick sowie Socket Behandlung wurde nicht nur von mir erdacht.
		Da ich nicht mehr genau nachvollziehen kann wer wann was beigetragen hat, ist diese SW open source.
		Die verwendeten Codeteile sind auch frei im Internet verfügbar, die Rechte gehören dem jeweiligen Rechteinhaber, und sind auch Open Source.
		Canlib ist geistiges Eigentum von Kvaser.
		(C) 2018-2024 enGYneer by Martin Gyurkó
		''')

	def sendMsg(self, msgid, msg):
#		print( "%03x :" %(msgid), end="")
#		for j in range(len(msg)) :
#			print( " %02x" % ( msg[j] ), end="")
#		print( ". ")
		self.handle1.write_raw(msgid, msg)
		time.sleep(0.001)

	def sendElmoMsgShort(self, axeId, command, index):
	    # print ("%x %s %d" % (axeId, command, index))
	    b=bytearray(command,"ascii")
	    # print ("%x   %x %x %02x %02x" % (idTx+axeId, b[0],b[1], index, 0))
	    self.sendMsg (idTx+axeId,( b[0],b[1], index, 0))

	def sendElmoMsgLong(self, axeId, command, index, value):
	    # print ("%x %s %d %d" % (axeId, command, index, value))
	    b=bytearray(command,"ascii")
	    # print ("%x   %x %x %02x %02x %02x %02x %02x %02x" % (idTx+axeId, b[0],b[1], index, 0, v(value,0), v(value,1), v(value,2), v(value,3)))
	    self.sendMsg (idTx+axeId,( b[0],b[1], index, 0, v(value,0), v(value,1), v(value,2), v(value,3)))

	def initCAN(self):

		self.cl = canlib

		print("canlib version: " ,self.cl.dllversion())

		channel = 0
		self.handle1 = self.cl.openChannel(channel, canlib.canOPEN_ACCEPT_VIRTUAL)
		print( "Using channel: %s, EAN: %s" % (self.handle1.channel_data.channel_name, self.handle1.channel_data.card_upc_no))

		self.handle1.setBusOutputControl(canlib.canDRIVER_NORMAL)
		self.handle1.setBusParams(canlib.canBITRATE_1M)
		self.handle1.busOn()

	def startCANComm(self):
		self.sendMsg(0x00, (0x82,idX)) #Reset CAN comm
		# self.sendMsg(0x00, (0x82,idX2)) #Reset CAN comm
		self.sendMsg(0x00, (0x82,idY)) #Reset CAN comm
		self.sendMsg(0x00, (0x82,idZ)) #Reset CAN comm
		self.sendMsg(0x00, (0x82,idC)) #Reset CAN comm
		time.sleep(0.5)
		self.sendMsg(0x00, (0x01,idX)) #Start CAN Comm
		# self.sendMsg(0x00, (0x01,idX2)) #Start CAN Comm
		self.sendMsg(0x00, (0x01,idY)) #Start CAN Comm
		self.sendMsg(0x00, (0x01,idZ)) #Start CAN Comm
		self.sendMsg(0x00, (0x01,idC)) #Start CAN Comm

	def startSocketListener(self):
		print("starting socket listener...")
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((HOST, PORT))
			while True:
				print("started listening...")
				s.listen() #waits here till connected
				conn, addr = s.accept()
				self.conn = conn
				self.startSocketSenderThread.start() #we start sending data only as soon as we have a connection to openpnp
				with conn:
					print('Connected by', addr)
					while True:
						try:
							data = conn.recv(1024)
						except:
							print("He? closed connection?")
						if not data:
							print("got hangup message")
							self.NotStop()
							break
						print(data)
						# if self.pushButtonSocketlog.isChecked():
						# 	self.plainTextEditSocketLog.appendPlainText(str(data))
#						self.analyseSocketData(data)
						self.recTcpQ.put(data)
						# time.sleep(0.25)
						# conn.sendall(b'ok\r\n')
						# print(Color.Magenta+'wroteback ok to tcp'+Color.end)

	def startSocketSender(self):
		print("starting sender")
		#wait for connection from listener
		while (not self.conn):
			None
		#sending position data to openpnp
		print("started sending")
		while True :
			time.sleep(0.1)
			# if self.pushButtonReadPos.isChecked()	:
			# 	message = "<Idle,MPos:%02.3f,%02.3f,%02.3f,%02.3f>\n" %(self.currentPos[0]/Xm+self.currentPos[4]/X2m, self.currentPos[1]/Ym, self.currentPos[2]/Zm-50.0, self.currentPos[3]/Cm)
			# 	# message = "X:%02.3f Y:%02.3f Z:%02.3f C:%02.3f\n" %(self.currentPos[0]/Xm+self.currentPos[4]/X2m, self.currentPos[1]/Ym, self.currentPos[2]/Zm-50.0, self.currentPos[3]/Cm)
			# 	print(Color.Magenta+message+Color.end)
			# 	self.sendTcpQ.put(message)
			while not self.sendTcpQ.empty() :
				message = self.sendTcpQ.get()
				print("to openpnp:",message)
				self.conn.sendall(message.encode("utf-8"))
				#self.conn.flush()


	def analyseSocketData(self, data):
		if data:
			if data==b'\n':  # don't process if only the newline is sent
				return
			dlines=data.decode().split('\n')
			print(dlines)
			for d in dlines:
				if d !='':
					print(':'+d+':')
					d=d.split(';')[0]  # strip the comment, if any
					print(':'+d+':')
					if d[0]=='@':
						print(Color.yellow+d[1:]+Color.end)
						self.sendSerQ.put(d[1:].encode("ascii")+b'\n') # sending to smoothie
					else:
						print(Color.Green+d+Color.end)
						m = re.search("(M)([-0-9.]+)", d, re.I)
						g = re.search("(G)([-0-9.]+)", d, re.I)
						x = re.search('(X)([-0-9.]+)', d, re.I)
						y = re.search('(Y)([-0-9.]+)', d, re.I)
						z = re.search('(Z)([-0-9.]+)', d, re.I)
						c = re.search('(C)([-0-9.]+)', d, re.I)
						f = re.search('(F)([-0-9.]+)', d, re.I)
						# print(Color.Green+repr(g)+Color.end)
						if m:
							m = float(m[2])                  # get the number
							if m == 400 :
								print(Color.Green+'Wait!!!'+Color.end)
								# time.sleep(2) # simulate a movement delay
								moving = 999

								ts = time.time()
								while moving and ((time.time()-ts) < 30): # we dont want to wait endlessly
									for axe in axes :
										self.sendElmoMsgShort(axe,"MS", 0 ) #ask for the motion status of each axis
									time.sleep(0.005) # wait for processing of request
									moving = 0
									for i in range(0,5) :
										if self.MotionStatusReg[i] == 2 :
											moving = moving + 1
									print("moving: ", moving, end="\r")
									if not moving:
										print("")
										self.sendTcpQ.put("ok\r\n")
										print(Color.Magenta+'wroteback ok to tcpQueue'+Color.end)
										break
							elif m == 401 :   # get vacuum pressure
								print(Color.Green+'Vacuum?'+Color.end)
								self.requestSensValue()
							elif m == 114 :
								print(Color.Green+'Position?'+Color.end)
								self.readPosOnce()
								time.sleep(0.3)
								message = "ok X:%02.3f Y:%02.3f Z:%02.3f C:%02.3f\n" %(self.currentPos[0]/Xm+self.currentPos[4]/X2m, self.currentPos[1]/Ym, self.currentPos[2]/Zm-50.0, self.currentPos[3]/Cm)
								print(Color.Magenta+message+Color.end)
								self.sendTcpQ.put(message)
							else :
								print(Color.Green+'m'+Color.end , m)
								self.sendSerQ.put(d.encode("ascii")+b'\n')
								if m == 804 :
									self.pushButtonJet.setChecked(True)
								if m == 805 :
									self.pushButtonJet.setChecked(False)
								if m == 806 :
									self.pushButtonJetterDown.setChecked(True)
								if m == 807 :
									self.pushButtonJetterDown.setChecked(False)
								if m == 808 :
									self.pushButtonZClampOff.setChecked(True)
								if m == 809 :
									self.pushButtonZClampOff.setChecked(False)
								if m == 802 :
									self.pushButtonLight.setChecked(True)
								if m == 803 :
									self.pushButtonLight.setChecked(False)
								if m == 810 :
									self.pushButtonToolChangerVac.setChecked(True)
								if m == 811 :
									self.pushButtonToolChangerVac.setChecked(False)
								if m == 800 :
									self.pushButtonToolTipVac.setChecked(True)
								if m == 801 :
									self.pushButtonToolTipVac.setChecked(False)
								if m == 812 :
									self.pushButtonDispens1.setChecked(True)
								if m == 8121 :
									self.pushButtonDispens1Shot.click()
								if m == 813 :
									self.pushButtonDispens1.setChecked(False)
								if m == 814 :
									self.pushButtonDispens2.setChecked(True)
								if m == 8141 :
									self.pushButtonDispens2Shot.click()
								if m == 815 :
									self.pushButtonDispens2.setChecked(False)
								if m == 816 :
									self.pushButtonDispensVac1.setChecked(True)
								if m == 817 :
									self.pushButtonDispensVac1.setChecked(False)
								if m == 818 :
									self.pushButtonDispensVac2.setChecked(True)
								if m == 819 :
									self.pushButtonDispensVac2.setChecked(False)
								if m == 820 :
									self.pushButtonWorkingVac.setChecked(True)
								if m == 821 :
									self.pushButtonWorkingVac.setChecked(False)
								if m == 822 :
									self.goX2(	printer_pos2_mm )
								if m == 823 :
									self.goX2(	printer_pos1_mm )

							# return
						if g:
							g = float(g[2])
							if g == 28:
								print(Color.Green+'Init and Homing all axes'+Color.end)
								print(Color.Red+'No. just kidding. Would be too dangerous. You have to home Z yourself!'+Color.end)
								#self.homeAllThread.start()
							if (g == 0) or (g == 1) :
								if x:
									xVal = float(x[2])
									# print("x: ",xVal)
									# if (minimumf[0] <= xVal) and (xVal <= maximumf[0]) :
									# 	self.X1set.setValue(int(xVal*Xm))
									# 	self.X2set.setValue(0)
									# elif (xVal > maximumf[0]) :
									# 	self.X1set.setValue((xVal-maximumf[4])*Xm)
									# 	self.X2set.setValue(maximum[4])
									# else : #(xVal < minimumf[0]) :
									# 	self.X1set.setValue((xVal-minimumf[4])*Xm)
									# 	self.X2set.setValue(minimum[4])

									## self.X1set.setValue(int(float(x[2])*200.0+.5))		# constants are for conversion btw mm to step
###
									# if (minimumf[0] <= xVal) and (xVal <= maximumf[0]) :
										# self.X1set.setValue(int(xVal*Xm))
										# self.X2set.setValue(0)
									# elif (xVal > maximumf[0]) :
										# self.X1set.setValue(int(maximumf[0]*Xm))
										# self.X2set.setValue(0)
									# else : #(xVal < minimumf[0]) :
										# self.X1set.setValue(int(minimumf[0]*Xm))
										# self.X2set.setValue(0)

									self.X1set.setValue(int(xVal*Xm))

								if y:
									self.Yset.setValue(int(float(y[2])*Ym))
								if z:
									self.Zset.setValue(100000+int(float(z[2])*Zm)) #openpnp likes to think it starts at z=0
								if c:
									self.Cset.setValue(int(float(c[2])*Cm))	# 4100 steps / 360°
								if f:
									self.Vmaxset.setValue(int(float(f[2])*10.0))
								# do 5 dimensional movement
								if x or y or z or c :
									self.betterGoTo()
							self.sendTcpQ.put("ok\r\n")
							print(Color.Magenta+'wroteback ok to tcpQueue'+Color.end)

	def captureOldPos(self):
		self.oldx	= self.currentPos[0]
		self.oldy	= self.currentPos[1]
		self.oldz	= self.currentPos[2]
		self.oldc	= self.currentPos[3]
		self.oldx2	= self.currentPos[4]

	def analyseSensorData(self):
		while not self.recSensQ.empty() :
			data = self.recSensQ.get()
			print(data)
			p = re.search("(P. |P.)([-0-9.]+)", data, re.I)
			if p :
				pressure = float(p[2])
				print ("Pressure:",pressure)
				self.progressBarToolTipVacRead.setValue(pressure)

	def serialReader(self):
		while True:
			data = self.sbus.readline()  # Should be ready
			if data:
				print(Color.Blue+repr(data)+Color.end)
				self.sendTcpQ.put(data.decode('utf-8'))
				self.analyseSerialData(data)
			# time.sleep(0.05)

	def analyseSerialData(self,data):
		d = data.decode('utf-8')
		# print (d)
		m = re.search("(P1.24:)([-0-9.]+)", d, re.I)
		if m :
			m = int(m[2])
			print("jettertouch:",m, end="")
			self.checkBoxJetterTouch.setChecked(m)

		m = re.search("(P1.29:)([-0-9.]+)", d, re.I)
		if m :
			m = not int(m[2])
			print(" jetterUp:",m, end="")
			self.checkBoxJetterUp.setChecked(m)

		m = re.search("(P1.28:)([-0-9.]+)", d, re.I)
		if m :
			m = not int(m[2])
			print(" jetterDown:",m, end="")
			self.checkBoxJetterDown.setChecked(m)

		m = re.search("(P1.26:)([-0-9.]+)", d, re.I)
		if m :
			m = int(m[2])
			print(" Touch:",m)
			self.checkBoxTipTouch.setChecked(m)

		m = re.search("(P1.27:)([-0-9.]+)", d, re.I)
		if m :
			m = not int(m[2])
			print(" Zclamp back:",m)
			self.checkBoxZClampBack.setChecked(m)

		m = re.search("(P1.25:)([-0-9.]+)", d, re.I)
		if m :
			m = not int(m[2])
			print(" Zclamp front:",m)
			self.checkBoxZClampFront.setChecked(m)

		m = re.search("(T. |T.)([-0-9.]+)", d, re.I)
		if m :
			thermodeTemp = float(m[2])
			print ("thermodeTemp:",thermodeTemp)
			self.progressBarThermodeTemp.setValue(thermodeTemp)
			self.thermodeTemp = thermodeTemp

		m = re.search("(B. |B.)([-0-9.]+)", d, re.I)
		if m :
			bettTemp = float(m[2])
			print ("bettTemp:",bettTemp)
			self.progressBarBettTemp.setValue(bettTemp)
			self.bettTemp = bettTemp

	def serialSensorReader(self):
		while True:
			data = self.sbus2.readline()  # Should be ready
			# data = "" #self.sbus2.readline()  # Should be ready
			if data:
				print(Color.Cyan+repr(data)+Color.end)
				self.sendTcpQ.put(data.decode('utf-8')) #copy data to OpenPNP
				self.recSensQ.put(data.decode('utf-8')) #lets also use the sensed data here
				# self.emit( QtCore.SIGNAL("analyseSensor"))
				self.analyseSensor.emit()
			# time.sleep(0.05)


	def serialSender(self) :
		while True:
			while not self.sendSerQ.empty() :
				message = self.sendSerQ.get()
				print(Color.blue+repr(message)+Color.end)
				self.sbus.write(message)
			while not self.sendSensQ.empty() :
				message = self.sendSensQ.get()
				print(Color.cyan+repr(message)+Color.end)
				self.sbus2.write(message)
			self.sbus.flush()
			self.sbus2.flush()
			time.sleep(0.05)
	
	def motionQueueHandler(self):
		while True:
			while not self.recTcpQ.empty() :
				data = self.recTcpQ.get()
				print(Color.yellow+repr(data)+Color.end)
				self.analyseSocketData(data)
			time.sleep(0.01)

	def requestSensValue(self) :
		data = "P\n"
		self.sendSensQ.put(data.encode("utf-8"))


def main():
	app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
	form = PyGuiApp()  # We set the form to be our PyGuiApp (design)
	form.show()  # Show the form
	sys.exit(app.exec_())  # and execute the app and exit after it is finished

if __name__ == '__main__':  # if we're running file directly and not importing it
	main()  # run the main function
	
	
