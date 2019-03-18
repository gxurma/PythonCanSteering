# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
#from Gui import *
import Gui
import canlib
import time
import random
import math

import os, struct, array
from fcntl import ioctl

#ids:
idX = 0x16
idY = 0x1c
idZ = 0x39
idC = 0x18
idX2 = 78

idTx = 0x300
idRx = 0x280

max=[0,0,0,0,0]
# X: 200 count / mm
max[0] = 32768

# Y: 200 count / mm
max[1] = 41330

# Z: 2000 count /mm
max[2] = 100000

# C: 2000 count / round
max[3] = 100000

# X2: 200 count / round
max[4] = 10000


# sample time = 4*135 = 540µs
vMaxX = 300000 #  *1/2^16 counts/sample time
aMaxX = 20000
vMaxY = 300000
aMaxY = 20000
vMaxZ = 250000
aMaxZ = 20000
vMax = vMaxZ
aMax = aMaxZ

ready = 0
stopping = 1
moving = 2

fTabelle=[0.0001,0.0002,0.0003,0.0004,0.0005,0.0006,0.0007,0.0008,0.0009,0.0010,
                           0.002 ,0.005 ,0.010 ,0.015 ,0.020 ,0.025 ,0.030 ,0.050 ,0.055 ,0.060 ,
                           0.065 ,0.070 ,0.075 ,0.080 ,0.090 ,0.100 ,0.110 ,0.120 ,0.130 ,0.140 ,
                           0.160 ,0.190 ,0.220 ,0.250 ,0.280 ,0.320 ,0.360 ,0.380 ,0.400 ,0.420 ,
                           0.440 ,0.460 ,0.480 ,0.500 ,0.520 ,0.540 ,0.560 ,0.580 ,0.600 ,0.625 ,
                           0.650 ,0.675 ,0.700 ,0.725 ,0.750 ,0.775 ,0.800 ,0.825 ,0.850 ,0.875 ,
                           0.900 ,0.925 ,0.950 ,0.975 ,1.000
                          ]
def invFtabelle(f):
	for i in range(0,65):
		if abs(f) <= fTabelle[i]:
			if f < 0:
				return -i/64.0
			else :
				return i/64.0
	if f < 0:
		return -1.0
	else:
		return 1.0

def cmp(a,b):
	return (a>b)-(a<b)


class canMsg():
	def __init__(self,id, msg, dlc, flg, timestamp):
		self.id = id
		self.msg = msg
		self.dlc = dlc
		self.flg = flg
		self.timestamp = timestamp


class ExampleApp(QtGui.QMainWindow, Gui.Ui_MainWindow):
	def __init__(self):
		# Explaining super is out of the scope of this article
		# So please google it if you're not familar with it
		# Simple reason why we use it here is that it allows us to
		# access variables, methods etc in the design.py file
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
		self.actionAbout.triggered.connect(self.aboutBox)
		self.SliderPosX.valueChanged.connect(self.goXYZNow)
		self.SliderPosY.valueChanged.connect(self.goXYZNow)
		self.SliderPosZ.valueChanged.connect(self.goXYZNow)
		self.SliderMaxAcc.valueChanged.connect(self.AccChange)
		self.SliderMaxVel.valueChanged.connect(self.VelChange)
		self.pushButtonGoX0Y0.clicked.connect(self.goX0Y0)
		self.pushButtonGoZmax.clicked.connect(self.goZmax)
		self.pushButtonGoXmaxYmax.clicked.connect(self.goXmaxYmax)
		self.pushButtonGoX0Ymax.clicked.connect(self.goX0Ymax)
		self.pushButtonGoXmaxY0.clicked.connect(self.goXmaxY0)
		self.pushButtonGoXYZ.clicked.connect(self.goXYZNow)
		self.pushButtonGoC0.clicked.connect(self.goC0)
		self.pushButtonGoX20.clicked.connect(self.goX20)

		self.pushButtonSendXParams.clicked.connect(self.SendXParams)
		self.pushButtonSendYParams.clicked.connect(self.SendYParams)
		self.pushButtonSendZParams.clicked.connect(self.SendZParams)
		self.pushButtonXReglerAnAus.clicked.connect(self.XReglerAnAus)
		self.pushButtonYReglerAnAus.clicked.connect(self.YReglerAnAus)
		self.pushButtonZReglerAnAus.clicked.connect(self.ZReglerAnAus)
		
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

		self.pushButtonNotStop.clicked.connect(self.NotStop)
		self.initCAN()
		self.startCANComm()
		self.vMaxX = vMaxX
		self.aMaxX = aMaxX
		self.vMaxY = vMaxY
		self.aMaxY = aMaxY
		self.vMaxZ = vMaxZ
		self.aMaxZ = aMaxZ
		self.vMax = vMax
		self.aMax = aMax
		#self.AccOrVelChange()
		self.oldPosRandX = 0
		self.oldPosRandY = 0
		self.oldPosRandZ = 0
		self.PosX = 0
		self.PosY = 0
		self.PosZ = 100000

		# init status machine
		self.Status=dict(x='Stop',y='Stop',z='Stop')


		# Eigener Lese Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
		self.readThread = GenericThread(self.readMsg)
		self.connect( self, QtCore.SIGNAL("analyse(PyQt_PyObject)"), self.analyseCANMsg ) # Verbinde readMsg mit Analysefunktion
		self.readThread.start()
		# Eigener pos lese Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
		self.readPosThread = GenericThread(self.readPos)
		self.readPosThread.start()
		self.pushButtonReadPos.clicked.connect(self.readPosThread.start)


		#homing thread
		self.homeXThread = GenericThread(lambda:self.HomeX2(idX))
		self.homeX2Thread = GenericThread(lambda:self.HomeX2(idX2))
		self.homeYThread = GenericThread(lambda:self.HomeX2(idY))
		self.homeZThread = GenericThread(lambda:self.Home(idZ))
		self.homeCThread = GenericThread(lambda:self.Home(idC))
		self.pushButtonHomeX.clicked.connect(self.homeXThread.start)
		self.pushButtonHomeX2.clicked.connect(self.homeX2Thread.start)
		self.pushButtonHomeY.clicked.connect(self.homeYThread.start)
		self.pushButtonHomeZ.clicked.connect(self.homeZThread.start)
		self.pushButtonHomeC.clicked.connect(self.homeCThread.start)

		# Eigener Joystic Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
		self.initJoysticHW()
		self.joysticThread = GenericThread(self.handleJoystic)
		self.joysticModeThread = GenericThread(self.joysticMode)

		self.pushButtonJoysticMode.clicked.connect(self.joysticThread.start)
		self.pushButtonJoysticMode.clicked.connect(self.joysticModeThread.start)

		self.KreisThread = GenericThread(self.Kreis)
		self.pushButtonKreis.clicked.connect(self.KreisThread.start)
		self.LinieThread = GenericThread(self.Linie)
		self.pushButtonLinie.clicked.connect(self.LinieThread.start)

		self.PIDPosThread = GenericThread(self.PIDPos)
		self.pushButtonPIDReglerMitJoystick.clicked.connect(self.PIDPosThread.start)
		self.pushButtonPIDReglerMitJoystick.clicked.connect(self.joysticModeThread.start)

		self.status = [ready,ready,ready]
		self.axisSpeed = [0,0,0]
		self.axisOldSpeed = [0,0,0]

		print(fTabelle)

		self.currentPos=[0,0,0,0,0]
		self.StatusReg = 0
		self.VelErr = 0


	def MotorAus(self, axe, isChecked):
		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, isChecked,0,0,0  )) #mo = 0 motor off


	def PIDPos(self) : # regle position mit Hilfe von joystik Befehlen
		sumferror = [0,0,0]
		error = [0,0,0]
		oldferror = [0,0,0]
		sumferrorlimit = 10
		pos = [0,0,0]
		goal = [0,0,0]
		ferror = [0,0,0]
		output = [0,0,0]
		while self.pushButtonPIDReglerMitJoystick.isChecked():
			pos[0] = self.currentPos[0]
			pos[1] = self.currentPos[1]
			pos[2] = self.currentPos[2]
			goal[0] = 	self.horizontalSliderJPosX.value()
			goal[1] = 	self.horizontalSliderJPosY.value()
			goal[2] = 	self.horizontalSliderJPosZ.value()
			for i in range(0,3):
				error[i] = goal[i] - pos[i]
				ferror[i] = error[i] / 100000.0
				sumferror[i] += ferror[i] # integrierender Teil
				if sumferror[i] > sumferrorlimit:
						sumferror[i] = sumferrorlimit
				if sumferror[i] < (-sumferrorlimit):
						sumferror[i] = (-sumferrorlimit)
				output[i] = ferror[i] * self.horizontalSliderKPv.value()
				output[i] += sumferror[i] * self.horizontalSliderKIv.value()/100
				output[i] += (ferror[i]-oldferror[i]) * self.horizontalSliderKDv.value()
				if output[i] > 1.0 :
					output[i] = 1.0
				elif output[i] < -1.0 :
					output[i] = - 1.0
				#print(i, pos[i], goal[i], error[i], ferror[i], sumferror[i], (ferror[i]-oldferror[i]), output[i])
				oldferror[i] = ferror[i] # speicher für differenziellen teil
			self.axis_states['x'] = invFtabelle( output[0])
			self.axis_states['y'] = invFtabelle( output[1])
			self.axis_states['ry'] = invFtabelle( output[2])
			time.sleep(0.05)

	def Kreis(self):
		radius = self.horizontalSliderRadius.value()
		origX = self.horizontalSliderJPosX.value()
		origY = self.horizontalSliderJPosY.value()
		for i in range(0,361):
			fi = i*2*math.pi/360
			si = math.cos(fi)
			ci = math.sin(fi)
			x = origX + radius * si
			y = origY + radius * ci
			#print(i,fi, si, ci, x, y)
			#self.PosX = int(x)
			#self.PosY = int(y)
			#self.goXYZ()
			self.horizontalSliderJPosX.setValue(int(x))
			self.horizontalSliderJPosY.setValue(int(y))

			#while ((self.status[0] != ready) or (self.status[1] != ready) or (self.status[2] != ready)):
				#print(i,x,y, self.status)
			time.sleep(0.1)

	def Linie(self):
		origX = self.horizontalSliderJPosX.value()
		origY = self.horizontalSliderJPosY.value()
		origZ = self.horizontalSliderJPosZ.value()
		goalX = self.horizontalSliderJGoalX.value()
		goalY = self.horizontalSliderJGoalY.value()
		goalZ = self.horizontalSliderJGoalZ.value()
		speed = self.horizontalSliderRadius.value() #counts / s
		distX = goalX - origX
		distY = goalY - origY
		distZ = goalZ - origZ
		dist = math.sqrt(distX**2 + distY**2+ distZ**2)
		movtime = int(dist/speed * 10)
		print("distX, distY, distZ, dist, speed, movtime:",distX, distY,distZ, dist, speed, movtime)
		for i in range(0,(movtime+1)):
			x = origX + i * distX/movtime
			y = origY + i * distY/movtime
			z = origZ + i * distZ/movtime
			self.horizontalSliderJPosX.setValue(int(x))
			self.horizontalSliderJPosY.setValue(int(y))
			self.horizontalSliderJPosZ.setValue(int(z))
			time.sleep(0.1)

	def NotStop(self):
		msg = (0x4d,0x4f,0,0, 0,0,0,0  )  # mo = 0 motor off
		self.sendMsg(idTx+idX, msg )
		self.sendMsg(idTx+idX2, msg )
		self.sendMsg(idTx+idY, msg )
		self.sendMsg(idTx+idZ, msg )
		self.sendMsg(idTx+idC, msg )

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



	# Main Joystic event loop
	def handleJoystic(self):
		while self.pushButtonJoysticMode.isChecked():
			evbuf = self.jsdev.read(8)
			if evbuf:
				timestamp, value, type, number = struct.unpack('IhBB', evbuf)

				if type & 0x80:
					 print ("(initial)",end="")

				if type & 0x01:
					button = self.button_map[number]
					if button:
						self.button_states[button] = value
						if value:
							print ("%s pressed" % (button))
						else:
							print ("%s released" % (button))

				if type & 0x02:
					axis = self.axis_map[number]
					fvalue = value / 32767.0
					self.axis_states[axis] = fvalue #store value state
					#print("%s : %.6f" % (axis, fvalue))
		print("Jostic mode off 1")


	def joysticMode(self):
		self.NotStop() #stop everything first.
		self.AccChange()
		self.VelChange() # set all speed and acc params to set max value, we are referencing to that internally
		while self.pushButtonJoysticMode.isChecked() or self.pushButtonPIDReglerMitJoystick.isChecked():

			self.axisSpeed[0] = int(self.axis_states['x'] * 64.95)
			self.axisSpeed[1] = int(self.axis_states['y'] * 64.95)
			self.axisSpeed[2] = int(self.axis_states['ry'] * 64.95)
			print(self.axisSpeed)
			for i in range(0,3):
				direction=(self.axisSpeed[i]<0)
				speed = self.vMax * fTabelle[abs(self.axisSpeed[i])]
				dsmax = (((speed*speed*0.5)/self.aMax)/256) + 1000
				#print(i, self.axisSpeed[i],self.axisOldSpeed[i])
				if (direction and (self.currentPos[i] < dsmax)) or ((not direction) and (self.currentPos[i] > (max[i]-dsmax))):
					#print ("need to stop here", i, dsmax, self.currentPos[i])
					self.status[i] = stopping
					#self.sendMsg(i << 3 , (0x59, 0xa, 2, 0))
					self.sendMsg(i << 3 , (0x88, 0xa))
				elif (cmp(self.axisSpeed[i],0) != cmp(self.axisOldSpeed[i],0)) and (self.status[i] == moving):
					#print("direction change",i)
					self.status[i] = stopping
					self.sendMsg(i << 3 , (0x88, 0xa))
				elif (self.axisSpeed[i] != self.axisOldSpeed[i]) and (self.status[i] == moving):
					#print("changing speed",i,speed,direction)
					self.sendMsg(i << 3 , (0x59, 0xa, 2, abs(self.axisSpeed[i])))
				elif (self.status[i] == ready)and (self.axisSpeed[i]!= 0 ) : #and (self.currentPos[i] > dsmax) and (self.currentPos[i] < (max[i]-dsmax)):
					#print("starting",i)
					self.status[i] = moving
					self.sendMsg(i << 3 , (0x58, 0xa, direction))
					self.sendMsg(i << 3 , (0x59, 0xa, 2, abs(self.axisSpeed[i])))

			self.axisOldSpeed[0] = self.axisSpeed[0]
			self.axisOldSpeed[1] = self.axisSpeed[1]
			self.axisOldSpeed[2] = self.axisSpeed[2]

			time.sleep(0.05) # wait 50ms
		self.NotStop() #stop everything.
		print("Jostic mode off 2")

	def readPos(self) :
		while self.pushButtonReadPos.isChecked()	:
			msg = (0x50, 0x58, 0, 0) # PX
			self.sendMsg(idTx+idX, msg)# get pos
			self.sendMsg(idTx+idX2, msg)# get pos
			self.sendMsg(idTx+idY, msg)# get pos
			self.sendMsg(idTx+idZ, msg)# get pos
			self.sendMsg(idTx+idC, msg)# get pos
			time.sleep(0.2)


	def analyseCANMsg(self,msg):
		displayText = "%03x %02x %01d   :" % (msg.id, msg.flg, msg.dlc)
		for j in range(0,msg.dlc) :
			displayText = displayText + " %02x" % ( msg.msg[j] )
		displayText = displayText + ":"
		#self.addCANMsgToCANLog(displayText)
		#print(displayText)
		if (msg.msg[0] == 0x50) and (msg.msg[1] == 0x58) : # PX = ?
			pos = msg.msg[4]+(msg.msg[5]<<8)+(msg.msg[6]<<16)+(msg.msg[7]<<24)
			if (pos & 0x80000000) :
				pos = -(0x100000000 - pos)  # wir sind negative Zahl!
			if msg.id == idRx+idX :
				#print("posX :", pos)
				self.lcdNumberDROPosX.display(pos)
				self.currentPos[0] = pos
			if msg.id == idRx+idX2 :
				#print("posX :", pos)
				self.lcdNumberDROPosX2.display(pos)
				self.currentPos[4] = pos
			if msg.id == idRx+idY :
				#print("posY :", pos)
				self.lcdNumberDROPosY.display(pos)
				self.currentPos[1] = pos
			if msg.id == idRx+idZ :
				#print("posZ :", pos)
				self.lcdNumberDROPosZ.display(pos)
				self.currentPos[2] = pos
			if msg.id == idRx+idC :
				#print("posC :", pos)
				self.lcdNumberDROPosC.display(pos)
				self.currentPos[3] = pos
		if (msg.msg[0] == 0x56) and (msg.msg[1] == 0x45) : # VE = for homing
			self.VelErr = msg.msg[4]+(msg.msg[5]<<8)+(msg.msg[6]<<16)+(msg.msg[7]<<24)
			if (self.VelErr & 0x80000000) :
				self.VelErr = -(0x100000000 - self.VelErr)  # wir sind negative Zahl!
			print("velocity error: ", self.VelErr)
		if (msg.msg[0] == 0x53) and (msg.msg[1] == 0x52) : # SR = for homing
			self.StatusReg = msg.msg[4]+(msg.msg[5]<<8)+(msg.msg[6]<<16)+(msg.msg[7]<<24)
			print("Status Register: " , bin(self.StatusReg))

		#if (msg.msg[0] == 0xa0): # cmd OK oder Fehler gekommen
			#print("Cmd OK: ", msg.id)
			#self.sendMsg(msg.id-1, (0xa5,0x0a))#Cmd OK quittieren
			#self.status[(msg.id-1)>>3] = ready
		#if (msg.msg[0] == 0x88):
			#self.status[(msg.id-1)>>3] = ready


	def readMsg(self):
		while True:
			try:
				idr, msgr, dlc, flg, timestamp = self.handle1.read(int(1))
				canmsg = canMsg(idr, msgr, dlc, flg, timestamp)
				self.emit( QtCore.SIGNAL("analyse(PyQt_PyObject)"), canmsg )
			except (canlib.canNoMsg) as ex:
				None
			except (canlib.canError) as ex:
				print (ex)



	def Init(self,axe):

		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 0,0,0,0  )) #mo = 0 motor off
		self.sendMsg(idTx+axe, (0x50,0x58,0,0, 0,0,0,0  )) #px = 0 set PX
		self.sendMsg(idTx+axe, (0x50,0x59,0,0, 0,0,0,0  )) #py = 0 set aux position
		self.sendMsg(idTx+axe, (0x55,0x4d,0,0, 5,0,0,0  )) #um = 5 (position mode)
		#self.Home(axe)

	def HomeX2(self, axe):
		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 0,0,0,0  )) #mo = 0 motor off
		self.sendMsg(idTx+axe, (0x55,0x4d,0,0, 2,0,0,0  )) #um = 2 (velocity mode)
		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 1,0,0,0  )) #mo = 1 motor on
		
		if axe==idZ :
			self.sendMsg(idTx+axe, (0x48,0x4d,2,0, 0xA0,0x86,0x01,0x00  )) #hm[2] = 0x186A0 home position will be 100000
		elif axe==idX2 :
			self.sendMsg(idTx+axe, (0x48,0x4d,2,0, 0x60,0xf0,0xff,0xff  )) #hm[2] = 0x186A0 home position will be -4000
		else :
			self.sendMsg(idTx+axe, (0x48,0x4d,2,0, 0,0,0,0  )) #hm[2] = 0 home position will be 0
		# self.sendMsg(idTx+axe, (0x48,0x4d,2,0, 0x60,0xf0,0xff,0xff  )) #hm[2] = 0x186A0 home position will be -4000
		
		self.sendMsg(idTx+axe, (0x48,0x4d,3,0, 3,0,0,0  )) #hm[3] = 3 Configures the homing function to be triggered by the Index.
		self.sendMsg(idTx+axe, (0x48,0x4d,5,0, 0,0,0,0  )) #hm[5] = 0 The PX counter will be set to a predefined constant number HM[2]
		self.sendMsg(idTx+axe, (0x48,0x4d,4,0, 0,0,0,0  )) #HM[4] = 0 Stop motion after homing.

		if axe==idX2 :
			self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0xf9,0xff,0xff  )) #JV = -2049 Jog speed
			# self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0xfd,0xff,0xff  )) #JV = -512 Jog speed
		else: 
			self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0x10,0x00,0x00  )) #JV = 4096 Jog speed

		self.sendMsg(idTx+axe, (0x42,0x47,0,0 )) #BeGin
		ts = time.time()
		self.VelErr = 0

		#time.sleep(3)
		while (time.time()-ts) < 10 :
			self.sendMsg(idTx+axe, (0x56,0x45,0,0 )) #VE = ?
			print (abs(self.VelErr))
			if abs(self.VelErr) >= 1000 :
				break

		self.sendMsg(idTx+axe, (0x53,0x54,0,0 )) #STop

		self.sendMsg(idTx+axe, (0x48,0x4d,1,0, 1,0,0,0  )) #HM[1] = 1: arm homing

		if axe==idX2 :
			self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0x2,0x00,0x00  )) #JV = 512 Jog speed
			# self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0x1,0x00,0x00  )) #JV = 256 Jog speed
		else:
			self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0xf0,0xff,0xff  )) #JV = -4096 Jog speed

		self.sendMsg(idTx+axe, (0x42,0x47,0,0 )) #BeGin
		ts = time.time()
		self.StatusReg = 0xffffffff # muß sein, damit ich auf Antworten warte
		while (time.time()-ts) < 10 :
			self.sendMsg(idTx+axe, (0x53,0x52,0,0 )) #SR = ?
			print (self.StatusReg & (1<<11))
			if not(self.StatusReg & (1<<11)) :
				break

		self.sendMsg(idTx+axe, (0x53,0x54,0,0 )) #STop
		
		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 0,0,0,0  )) #mo = 0 motor off
		self.sendMsg(idTx+axe, (0x55,0x4d,0,0, 5,0,0,0  )) #um = 5 (position mode)
		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 1,0,0,0  )) #mo = 1 motor on
		
		if axe==idZ :
			self.sendMsg(idTx+axe, (0x50,0x41,0,0, 0xA0,0x86,0x01,0x00  )) #pa = 0 set position goal to 100000
		else:
			self.sendMsg(idTx+axe, (0x50,0x41,0,0, 0,0,0,0  )) #pa = 0 set position goal to 0
		self.sendMsg(idTx+axe, (0x53,0x50,0,0, 0x00,0x20,0,0  )) #sp = 8096 set speed

		self.sendMsg(idTx+axe, (0x42,0x47,0,0 )) #BeGin


	def Home(self, axe):

#		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 0,0,0,0  )) #mo = 0 motor off
#		self.sendMsg(idTx+axe, (0x55,0x4d,0,0, 2,0,0,0  )) #um = 2 (velocity mode)
		self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 1,0,0,0  )) #mo = 1 motor on
		if axe==idZ :
			self.sendMsg(idTx+axe, (0x48,0x4d,2,0, 0xA0,0x86,0x01,0x00  )) #hm[2] = 0x186A0 home position will be 100000
		elif axe==idX2 :
			self.sendMsg(idTx+axe, (0x48,0x4d,2,0, 0x60,0xf0,0xff,0xff  )) #hm[2] = 0x186A0 home position will be -4000
		else :
			self.sendMsg(idTx+axe, (0x48,0x4d,2,0, 0,0,0,0  )) #hm[2] = 0 home position will be 0
		self.sendMsg(idTx+axe, (0x48,0x4d,3,0, 3,0,0,0  )) #hm[3] = 3 Configures the homing function to be triggered by the Index.
		self.sendMsg(idTx+axe, (0x48,0x4d,5,0, 0,0,0,0  )) #hm[5] = 0 The PX counter will be set to a predefined constant number HM[2]
		self.sendMsg(idTx+axe, (0x48,0x4d,4,0, 0,0,0,0  )) #HM[4] = 0 Stop motion after homing.

		if axe != idC : # fahr nicht an Anschlag bei Theta Achse.

			if axe==idX2 :
				self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0xfd,0xff,0xff  )) #JV = -512 Jog speed
			else: 
				self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0x10,0x00,0x00  )) #JV = 4096 Jog speed
			self.sendMsg(idTx+axe, (0x42,0x47,0,0 )) #BeGin

			ts = time.time()
			self.VelErr = 0

			#time.sleep(3)
			while (time.time()-ts) < 10 :
				self.sendMsg(idTx+axe, (0x56,0x45,0,0 )) #VE = ?
				print (abs(self.VelErr))
				if axe==idX2 : 
					if abs(self.VelErr) >= 500 :
						break
				if abs(self.VelErr) >= 1000 :
					break

			self.sendMsg(idTx+axe, (0x53,0x54,0,0 )) #STop

		self.sendMsg(idTx+axe, (0x48,0x4d,1,0, 1,0,0,0  )) #HM[1] = 1: arm homing
		if axe==idX2 :
			self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0x1,0x00,0x00  )) #JV = 256 Jog speed
		else:
			self.sendMsg(idTx+axe, (0x4A,0x56,0,0, 0x00,0xf0,0xff,0xff  )) #JV = -4096 Jog speed
		self.sendMsg(idTx+axe, (0x42,0x47,0,0 )) #BeGin

		#time.sleep(10)
		ts = time.time()
		self.StatusReg = 0xffffffff # muß sein, damit ich auf Antworten warte
		while (time.time()-ts) < 20 :
			self.sendMsg(idTx+axe, (0x53,0x52,0,0 )) #SR = ?
			print (self.StatusReg & (1<<11))
			if not(self.StatusReg & (1<<11)) :
				break

		self.sendMsg(idTx+axe, (0x53,0x54,0,0 )) #STop

	#	self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 0,0,0,0  )) #mo = 0 motor off
	#	self.sendMsg(idTx+axe, (0x55,0x4d,0,0, 5,0,0,0  )) #um = 5 (position mode)
	#	self.sendMsg(idTx+axe, (0x4d,0x4f,0,0, 1,0,0,0  )) #mo = 1 motor on

#		time.sleep(1)

		if axe==idZ :
			self.sendMsg(idTx+axe, (0x50,0x41,0,0, 0xA0,0x86,0x01,0x00  )) #pa = 0 set position goal to 100000
		else:
			self.sendMsg(idTx+axe, (0x50,0x41,0,0, 0,0,0,0  )) #pa = 0 set position goal to 0
		self.sendMsg(idTx+axe, (0x53,0x50,0,0, 0x00,0x20,0,0  )) #sp = 8096 set speed

		self.sendMsg(idTx+axe, (0x42,0x47,0,0 )) #BeGin



	def XReglerAnAus(self):
		msg=(0x0d, 0x0a, self.pushButtonXReglerAnAus.isChecked())
		self.sendMsg(idX, msg)
	def YReglerAnAus(self):
		msg=(0x0d, 0x0a, self.pushButtonYReglerAnAus.isChecked())
		self.sendMsg(idY, msg)
	def ZReglerAnAus(self):
		msg=(0x0d, 0x0a, self.pushButtonZReglerAnAus.isChecked())
		self.sendMsg(idZ, msg)


	def SendXParams(self):
		msg=(0x1, 0x0a, self.horizontalSliderXKp.value() & 0xff , (self.horizontalSliderXKp.value()>>8) & 0xff)
		self.sendMsg(idX, msg)
		msg=(0x2, 0x0a, self.horizontalSliderXKi.value() & 0xff , (self.horizontalSliderXKi.value()>>8) & 0xff)
		self.sendMsg(idX, msg)
		msg=(0x3, 0x0a, self.horizontalSliderXKd.value() & 0xff , (self.horizontalSliderXKd.value()>>8) & 0xff)
		self.sendMsg(idX, msg)
		msg=(0x4, 0x0a, self.horizontalSliderXKvff.value() & 0xff , (self.horizontalSliderXKvff.value()>>8) & 0xff)
		self.sendMsg(idX, msg)
		msg=(0x5, 0x0a, self.horizontalSliderXKbias.value() & 0xff , (self.horizontalSliderXKbias.value()>>8) & 0xff)
		self.sendMsg(idX, msg)

	def SendYParams(self):
		msg=(0x1, 0x0a, self.horizontalSliderYKp.value() & 0xff , (self.horizontalSliderYKp.value()>>8) & 0xff)
		self.sendMsg(idY, msg)
		msg=(0x2, 0x0a, self.horizontalSliderYKi.value() & 0xff , (self.horizontalSliderYKi.value()>>8) & 0xff)
		self.sendMsg(idY, msg)
		msg=(0x3, 0x0a, self.horizontalSliderYKd.value() & 0xff , (self.horizontalSliderYKd.value()>>8) & 0xff)
		self.sendMsg(idY, msg)
		msg=(0x4, 0x0a, self.horizontalSliderYKvff.value() & 0xff , (self.horizontalSliderYKvff.value()>>8) & 0xff)
		self.sendMsg(idY, msg)
		msg=(0x5, 0x0a, self.horizontalSliderYKbias.value() & 0xff , (self.horizontalSliderYKbias.value()>>8) & 0xff)
		self.sendMsg(idY, msg)

	def SendZParams(self):
		msg=(0x1, 0x0a, self.horizontalSliderZKp.value() & 0xff , (self.horizontalSliderZKp.value()>>8) & 0xff)
		self.sendMsg(idZ, msg)
		msg=(0x2, 0x0a, self.horizontalSliderZKi.value() & 0xff , (self.horizontalSliderZKi.value()>>8) & 0xff)
		self.sendMsg(idZ, msg)
		msg=(0x3, 0x0a, self.horizontalSliderZKd.value() & 0xff , (self.horizontalSliderZKd.value()>>8) & 0xff)
		self.sendMsg(idZ, msg)
		msg=(0x4, 0x0a, self.horizontalSliderZKvff.value() & 0xff , (self.horizontalSliderZKvff.value()>>8) & 0xff)
		self.sendMsg(idZ, msg)
		msg=(0x5, 0x0a, self.horizontalSliderZKbias.value() & 0xff , (self.horizontalSliderZKbias.value()>>8) & 0xff)
		self.sendMsg(idZ, msg)


	def goX0Y0(self):
		self.sendMsg(idTx+idX, (0x50,0x41,0,0, 0,0,0,0  )) #pa = 0 set position goal to 0
		self.sendMsg(idTx+idY, (0x50,0x41,0,0, 0,0,0,0  )) #pa = 0 set position goal to 0
		self.sendMsg(idTx+idX, (0x53,0x50,0,0, 0x00,0x20,0,0  )) #sp = 8096 set speed
		self.sendMsg(idTx+idY, (0x53,0x50,0,0, 0x00,0x20,0,0  )) #sp = 8096 set speed
		self.sendMsg(idTx+idX, (0x42,0x47,0,0 )) #BeGin
		self.sendMsg(idTx+idY, (0x42,0x47,0,0 )) #BeGin

	def goZmax(self):
		self.sendMsg(idTx+idZ, (0x50,0x41,0,0, 0xA0,0x86,0x01,0x00  )) #pa = 0 set position goal to 100000
		self.sendMsg(idTx+idZ, (0x53,0x50,0,0, 0x00,0x20,0,0  )) #sp = 8096 set speed
		self.sendMsg(idTx+idZ, (0x42,0x47,0,0 )) #BeGin

	def goC0(self):
		self.sendMsg(idTx+idC, (0x50,0x41,0,0, 0x0,0x0,0x0,0x0  )) #pa = 0 set position goal to 00000
		self.sendMsg(idTx+idC, (0x53,0x50,0,0, 0x00,0x10,0,0  )) #sp = 4096 set speed
		self.sendMsg(idTx+idC, (0x42,0x47,0,0 )) #BeGin

	def goX20(self):
		self.sendMsg(idTx+idX2, (0x50,0x41,0,0, 0x4c,0x1d,0x0,0x0  )) #pa = 0 set position goal to 7500
		self.sendMsg(idTx+idX2, (0x53,0x50,0,0, 0x00,0x10,0,0  )) #sp = 4096 set speed
		self.sendMsg(idTx+idX2, (0x42,0x47,0,0 )) #BeGin

	def goXmaxY0(self):
		self.PosX=max[0]
		self.PosY=0
		self.goXYZ()
	def goX0Ymax(self):
		self.PosX=0
		self.PosY=max[1]
		self.goXYZ()
	def goXmaxYmax(self):
		self.PosX=max[0]
		self.PosY=max[1]
		self.goXYZ()

	def goXYZNow(self):
		self.PosX=self.SliderPosX.value()
		self.PosY=self.SliderPosY.value()
		self.PosZ=self.SliderPosZ.value()
		self.goXYZ()

	def goXYZ(self):
		for i in self.status:
			if i != ready:
				print("machine not ready")
				return
		distX = self.oldPosRandX - self.PosX
		distY = self.oldPosRandY - self.PosY
		distZ = self.oldPosRandZ - self.PosZ
		dist = math.sqrt(distX * distX + distY * distY + distZ * distZ)
		if dist == 0 :
			return #dividing by zero is not nice...
		qX = distX/dist
		qY = distY/dist
		qZ = distZ/dist
		print("qX: %f, qY: %f, qZ: %f" %(qX,qY,qZ))
		self.vMaxX = abs(int(self.vMax * qX)) #adjust speeds and acceleration so that we all arrive at same time.
		self.aMaxX = abs(int(self.aMax * qX))
		self.vMaxY = abs(int(self.vMax * qY))
		self.aMaxY = abs(int(self.aMax * qY))
		self.vMaxZ = abs(int(self.vMax * qZ))
		self.aMaxZ = abs(int(self.aMax * qZ))
		print("vX: %d, vY: %d, vZ: %d" % (self.vMaxX, self.vMaxY, self.vMaxZ))
		print("aX: %d, aY: %d, aZ: %d" % (self.aMaxX, self.aMaxY, self.aMaxZ))

		self.AccOrVelChange()

		if self.oldPosRandX != self.PosX : #check if we need to move, otherwise do nothing
			self.posSet(0, self.PosX)
		if self.oldPosRandY != self.PosY :
			self.posSet(1, self.PosY)
		if self.oldPosRandZ != self.PosZ :
			self.posSet(2, self.PosZ)

		self.oldPosRandX = self.PosX
		self.oldPosRandY = self.PosY
		self.oldPosRandZ = self.PosZ


	def AccChange(self):
		self.aMax = self.SliderMaxAcc.value()
		self.aMaxX = self.aMax
		self.aMaxY = self.aMax
		self.aMaxZ = self.aMax
		self.AccOrVelChange()

	def VelChange(self):
		self.vMax = self.SliderMaxVel.value()
		self.vMaxX = self.vMax
		self.vMaxY = self.vMax
		self.vMaxZ = self.vMax
		self.AccOrVelChange()

	def AccOrVelChange(self):
		if self.vMaxX > vMaxX :
			self.vMaxX = vMaxX
		if self.vMaxY > vMaxY :
			self.vMaxY = vMaxY
		if self.vMaxZ > vMaxZ :
			self.vMaxZ = vMaxZ
		if self.aMaxX > aMaxX :
			self.aMaxX = aMaxX
		if self.aMaxY > aMaxY :
			self.aMaxY = aMaxY
		if self.aMaxZ > aMaxZ :
			self.aMaxZ = aMaxZ

		if (vMaxX != 0) and (aMaxX != 0) : # only change speed or acc if both are not zero. otherwise it does not make sense
			msg=(0x26, 0x0a, self.aMaxX & 0xff, (self.aMaxX>>8) & 0xff, (self.aMaxX>>16) & 0xff, self.vMaxX & 0xff, (self.vMaxX>>8) & 0xff, (self.vMaxX>>16) & 0xff)
			self.sendMsg(idX,msg)
		if (vMaxY != 0) and (aMaxY != 0) :
			msg=(0x26, 0x0a, self.aMaxY & 0xff, (self.aMaxY>>8) & 0xff, (self.aMaxY>>16) & 0xff, self.vMaxY & 0xff, (self.vMaxY>>8) & 0xff, (self.vMaxY>>16) & 0xff)
			self.sendMsg(idY,msg)
		if (vMaxZ != 0) and (aMaxZ != 0) :
			msg=(0x26, 0x0a, self.aMaxZ & 0xff, (self.aMaxZ>>8) & 0xff, (self.aMaxZ>>16) & 0xff, self.vMaxZ & 0xff, (self.vMaxZ>>8) & 0xff, (self.vMaxZ>>16) & 0xff)
			self.sendMsg(idZ,msg)



	def aboutBox(self):
		QtGui.QMessageBox.about(self,"Über dieses Programm", "Einfaches Programm zum Testen der Servos")

	#def PosXChange(self):
		#self.PosX=self.SliderPosX.value()
		#if self.pushButtonImmediate.isChecked() :
			#self.goXYZNow()

	#def PosYChange(self):
		#self.PosY=self.SliderPosY.value()
		#if self.pushButtonImmediate.isChecked() :
			#self.goXYZNow()

	#def PosZChange(self):
		#self.PosZ=self.SliderPosZ.value()
		#if self.pushButtonImmediate.isChecked() :
			#self.goXYZNow()

	def sendMsg(self, msgid, msg):
		print( "%03x :" %(msgid), end="")
		for j in range(len(msg)) :
			print( " %02x" % ( msg[j] ), end="")
		print( ". ")
		self.handle1.write(msgid, msg)
		time.sleep(0.05)

	def initCAN(self):

		self.cl = canlib.canlib()

		print("canlib version: %s" % self.cl.getVersion())

		channel = 0
		self.handle1 = self.cl.openChannel(channel, canlib.canOPEN_ACCEPT_VIRTUAL)
		print( "Using channel: %s, EAN: %s" % (self.handle1.getChannelData_Name(), self.handle1.getChannelData_EAN()))

		self.handle1.setBusOutputControl(canlib.canDRIVER_NORMAL)
		self.handle1.setBusParams(canlib.canBITRATE_1M)
		self.handle1.busOn()

	def startCANComm(self):
		self.sendMsg(0x00, (0x82,idX)) #Reset CAN comm
		self.sendMsg(0x00, (0x82,idX2)) #Reset CAN comm
		self.sendMsg(0x00, (0x82,idY)) #Reset CAN comm
		self.sendMsg(0x00, (0x82,idZ)) #Reset CAN comm
		self.sendMsg(0x00, (0x82,idC)) #Reset CAN comm
		time.sleep(0.5)
		self.sendMsg(0x00, (0x01,idX)) #Start CAN Comm
		self.sendMsg(0x00, (0x01,idX2)) #Start CAN Comm
		self.sendMsg(0x00, (0x01,idY)) #Start CAN Comm
		self.sendMsg(0x00, (0x01,idZ)) #Start CAN Comm
		self.sendMsg(0x00, (0x01,idC)) #Start CAN Comm

	def randomRun(self):
		self.PosX = random.randint(0,max[0])
		self.PosY = random.randint(0,max[1])
		self.PosZ = random.randint(0,max[2])
		self.goXYZ()

	def posSet(self, axis, pos):
		print(pos)
		if(pos > max[axis]) or (pos < 0 ):
			print("tul messze mennel")
			return
		self.status[axis] = moving
		msgid = axis * 8
		msg=(0x25, 0x0a, pos & 0xff, (pos>>8) & 0xff, (pos>>16) & 0xff)
		print ("./test ",msgid,msg)
		self.sendMsg(msgid,msg)

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


def main():

	app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
	form = ExampleApp()  # We set the form to be our ExampleApp (design)
	form.show()  # Show the form
	sys.exit(app.exec_())  # and execute the app and exit after it is finished




if __name__ == '__main__':  # if we're running file directly and not importing it



	main()  # run the main function
