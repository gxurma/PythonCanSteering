# -*- coding: utf-8 -*-
# PyGui middleware
# this standing in the middle between the machine and Openpnp
# it can home the axes one by one
# interprete the g-code commands comming from openpnp,
# decide if the X2 axis has to be moved to reach to the other side of the table,
# and send the CAN bus commands to the appropriate drives

from PyQt4 import QtCore, QtGui
import sys
#from Gui import *
import Gui
import canlib
import time
#import random
#import math

import os, struct, array
from fcntl import ioctl

#ids:
idX = 0x16
idY = 0x1c
idZ = 0x39
idC = 0x18
idX2 = 0x4e

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

def cmp(a,b):
	return (a>b)-(a<b)


def v( a, n):
    a1=(a>>(8*n))&255
    return a1


class canMsg():
	def __init__(self,id, msg, dlc, flg, timestamp):
		self.id = id
		self.msg = msg
		self.dlc = dlc
		self.flg = flg
		self.timestamp = timestamp


class PyGuiApp(QtGui.QMainWindow, Gui.Ui_MainWindow):
	def __init__(self):
		# Explaining super is out of the scope of this article
		# So please google it if you're not familar with it
		# Simple reason why we use it here is that it allows us to
		# access variables, methods etc in the design.py file
		super(self.__class__, self).__init__()
		self.setupUi(self)  # This is defined in design.py file automatically
		self.actionAbout.triggered.connect(self.aboutBox)
		self.pushButtonGoX0Y0.clicked.connect(self.goX0Y0)
		self.pushButtonGoZmax.clicked.connect(self.goZmax)
		self.pushButtonGoC0.clicked.connect(self.goC0)
		self.pushButtonGoX20.clicked.connect(self.goX20)

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

		# self.vMaxX = vMaxX
		# self.aMaxX = aMaxX
		# self.vMaxY = vMaxY
		# self.aMaxY = aMaxY
		# self.vMaxZ = vMaxZ
		# self.aMaxZ = aMaxZ
		# self.vMax = vMax
		# self.aMax = aMax
		# #self.AccOrVelChange()
		# self.oldPosRandX = 0
		# self.oldPosRandY = 0
		# self.oldPosRandZ = 0
		# self.PosX = 0
		# self.PosY = 0
		# self.PosZ = 100000

		# init status machine
#		self.Status=dict(x='Stop',y='Stop',z='Stop')


		# Eigener Lese Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
		self.readThread = GenericThread(self.readMsg)
		self.connect( self, QtCore.SIGNAL("analyse(PyQt_PyObject)"), self.analyseCANMsg ) # Verbinde readMsg mit Analysefunktion
		self.readThread.start()
		# Eigener pos lese Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
		self.readPosThread = GenericThread(self.readPos)
		self.readPosThread.start()  # starte thread um Positionen zu lesen
		self.pushButtonReadPos.clicked.connect(self.readPosThread.start) #jedes mal wenn angeklickt wird, starte pos Thread

#													HomeX2(axe, velMode, homePosition, jogSpeed, searchSpeed, targetPos, targetSpeed):
		#homing threads setup
		self.homeXThread	= GenericThread(lambda:self.Home(idX,	1,		0,	4096,	-4096,		0,8192))
		self.homeX2Thread	= GenericThread(lambda:self.Home(idX2,	1,	-4000, -1792,	512,		0,8192))
		self.homeYThread	= GenericThread(lambda:self.Home(idY,	1,		0,	4096,	-4096,		0,8192))
		self.homeZThread	= GenericThread(lambda:self.Home(idZ,	0, 100000,	4096,	-4096,	100000,8192))
		self.homeCThread	= GenericThread(lambda:self.Home(idC,	0,		0,	0,		-4096,		0,8192))
		self.pushButtonHomeX.clicked.connect(self.homeXThread.start)
		self.pushButtonHomeX2.clicked.connect(self.homeX2Thread.start)
		self.pushButtonHomeY.clicked.connect(self.homeYThread.start)
		self.pushButtonHomeZ.clicked.connect(self.homeZThread.start)
		self.pushButtonHomeC.clicked.connect(self.homeCThread.start)

		# Eigener Joystic Thread, um Blockieren des GUIs zum Lesen zu vermeiden.
#		self.initJoysticHW()
#		self.joysticThread = GenericThread(self.handleJoystic)
#		self.joysticModeThread = GenericThread(self.joysticMode)

#		self.pushButtonJoysticMode.clicked.connect(self.joysticThread.start)
#		self.pushButtonJoysticMode.clicked.connect(self.joysticModeThread.start)


		# self.status = [ready,ready,ready]
		# self.axisSpeed = [0,0,0]
		# self.axisOldSpeed = [0,0,0]
		#
		# self.currentPos=[0,0,0,0,0]
		# self.StatusReg = 0
		# self.VelErr = 0


	def MotorAus(self, axe, isChecked):
		self.sendElmoMsgLong(axe, "MO",0, isChecked) #mo = 0 motor off



	def NotStop(self):
		self.sendElmoMsgLong(idX, "MO",0,0 ) # mo = 0 motor off
		self.sendElmoMsgLong(idX2,"MO",0,0 )
		self.sendElmoMsgLong(idY, "MO",0,0 )
		self.sendElmoMsgLong(idZ, "MO",0,0 )
		self.sendElmoMsgLong(idC, "MO",0,0 )

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
		while self.pushButtonJoysticMode.isChecked() :

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
			self.sendElmoMsgShort(idX, "PX",0)# get pos
			self.sendElmoMsgShort(idX2,"PX",0)# get pos
			self.sendElmoMsgShort(idY, "PX",0)# get pos
			self.sendElmoMsgShort(idZ, "PX",0)# get pos
			self.sendElmoMsgShort(idC, "PX",0)# get pos
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
		self.sendElmoMsgLong(axe, "MO", 0, 0 ) #mo = 0 motor off
		self.sendElmoMsgLong(axe, "PX", 0, 0 ) #px = 0 set PX
		self.sendElmoMsgLong(axe, "PY", 0, 0 ) #py = 0 set aux position
		self.sendElmoMsgLong(axe, "UM", 0, 5 ) #um = 5 (position mode)

	def Home(self, axe, velMode, homePosition, jogSpeed, searchSpeed, targetPos, targetSpeed):
		if velMode :
			self.sendElmoMsgLong(axe, "MO", 0, 0) #mo = 0 motor off
			self.sendElmoMsgLong(axe, "UM", 0, 2) #um = 2 (velocity mode)

		self.sendElmoMsgLong(axe, "MO", 0, 1) #mo = 1 motor on

		self.sendElmoMsgLong(axe, "HM", 2, homePosition)
		self.sendElmoMsgLong(axe, "HM", 3, 3)#hm[3] = 3 Configures the homing function to be triggered by the Index.
		self.sendElmoMsgLong(axe, "HM", 5, 0)#hm[5] = 0 The PX counter will be set to a predefined constant number HM[2]
		self.sendElmoMsgLong(axe, "HM", 4, 0)#HM[4] = 0 Stop motion after homing.

		if jogSpeed != 0:
			self.sendElmoMsgLong(axe, "JV", 0, jogSpeed)
			self.sendElmoMsgShort(axe,"BG", 0)

			ts = time.time()
			self.VelErr = 0

			while (time.time()-ts) < 1 :
				self.sendElmoMsgShort(axe, "VE",0 ) #VE = ?
				# self.sendMsg(idTx+axe, (0x56,0x45,0,0 )) #VE = ?
				print ("velocity error :", abs(self.VelErr), end="   ")
				if abs(self.VelErr) >= 1000 :
					break

			self.sendElmoMsgShort(axe, "ST",0 ) #STop

		self.sendElmoMsgLong(axe, "HM", 1,1 ) #HM[1] = 1: arm homing
		self.sendElmoMsgLong(axe, "JV", 0, searchSpeed)
		self.sendElmoMsgShort(axe,"BG", 0)

		ts = time.time()
		self.StatusReg = 0xffffffff # muß sein, damit ich auf Antworten warte
		while (time.time()-ts) < 1 :
			self.sendElmoMsgShort(axe,"SR", 0 ) #SR = ?
			print ("status: ", (self.StatusReg & (1<<11))>>11, end="  ")
			if not(self.StatusReg & (1<<11)) : #checking if homing ready
				break

		self.sendElmoMsgShort(axe, "ST", 0 ) #STop

		if velMode :  #switch back to position mode
			self.sendElmoMsgLong(axe, "MO",0,0) #mo = 0 motor off
			self.sendElmoMsgLong(axe, "UM",0,5) #um = 5 (position mode)
			self.sendElmoMsgLong(axe, "MO",0,1) #mo = 1 motor on

		self.go(axe, targetPos, targetSpeed)


	def go(self, axe, target, speed):
		self.sendElmoMsgLong(axe, "PA",0,target) #pa = target set position goal to target
		self.sendElmoMsgLong(axe, "SP",0,speed ) #sp = speed set speed
		self.sendElmoMsgShort(axe, "BG",0 ) #BeGin



	def goX0Y0(self):
		self.go(idX, 0, 8192)
		self.go(idY, 0, 8192)

	def goZmax(self):
		self.go(idZ, 100000, 8192) # go to 100000 with speed 8192

	def goC0(self):
		self.go(idC, 0, 4096) # go to 0 with speed 4096

	def goX20(self):
		self.go(idX2, 7500, 4096) # go to 7500 with speed 4096

	def aboutBox(self):
		QtGui.QMessageBox.about(self,"Über dieses Programm", '''
Dies ist ein Programm zum Testen und benutzen einer CNC Maschine
mit Elmo Motion Cello Controllern. Die Maschine besteht aus X, X2, Y, Z, und C Achsen,
und sollte eigentlich mit Openpnp zusammenarbeiten. ''')

	def sendMsg(self, msgid, msg):
		print( "%03x :" %(msgid), end="")
		for j in range(len(msg)) :
			print( " %02x" % ( msg[j] ), end="")
		print( ". ")
		self.handle1.write(msgid, msg)
		time.sleep(0.05)

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
	form = PyGuiApp()  # We set the form to be our PyGuiApp (design)
	form.show()  # Show the form
	sys.exit(app.exec_())  # and execute the app and exit after it is finished

if __name__ == '__main__':  # if we're running file directly and not importing it
	main()  # run the main function
