# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Gui.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
	_fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
	def _fromUtf8(s):
		return s

try:
	_encoding = QtGui.QApplication.UnicodeUTF8
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
	def _translate(context, text, disambig):
		return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName(_fromUtf8("MainWindow"))
		MainWindow.resize(812, 467)
		self.centralwidget = QtGui.QWidget(MainWindow)
		self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
		self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
		self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
		self.gridLayout = QtGui.QGridLayout()
		self.gridLayout.setSpacing(0)
		self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
		self.lcdNumberDROPosC = QtGui.QLCDNumber(self.centralwidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lcdNumberDROPosC.sizePolicy().hasHeightForWidth())
		self.lcdNumberDROPosC.setSizePolicy(sizePolicy)
		self.lcdNumberDROPosC.setMinimumSize(QtCore.QSize(0, 46))
		self.lcdNumberDROPosC.setNumDigits(6)
		self.lcdNumberDROPosC.setSegmentStyle(QtGui.QLCDNumber.Filled)
		self.lcdNumberDROPosC.setObjectName(_fromUtf8("lcdNumberDROPosC"))
		self.gridLayout.addWidget(self.lcdNumberDROPosC, 1, 4, 1, 1)
		self.lcdNumberDROPosZ = QtGui.QLCDNumber(self.centralwidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lcdNumberDROPosZ.sizePolicy().hasHeightForWidth())
		self.lcdNumberDROPosZ.setSizePolicy(sizePolicy)
		self.lcdNumberDROPosZ.setMinimumSize(QtCore.QSize(0, 46))
		self.lcdNumberDROPosZ.setNumDigits(6)
		self.lcdNumberDROPosZ.setSegmentStyle(QtGui.QLCDNumber.Filled)
		self.lcdNumberDROPosZ.setObjectName(_fromUtf8("lcdNumberDROPosZ"))
		self.gridLayout.addWidget(self.lcdNumberDROPosZ, 1, 3, 1, 1)
		self.lcdNumberDROPosY = QtGui.QLCDNumber(self.centralwidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lcdNumberDROPosY.sizePolicy().hasHeightForWidth())
		self.lcdNumberDROPosY.setSizePolicy(sizePolicy)
		self.lcdNumberDROPosY.setMinimumSize(QtCore.QSize(0, 46))
		self.lcdNumberDROPosY.setNumDigits(6)
		self.lcdNumberDROPosY.setSegmentStyle(QtGui.QLCDNumber.Filled)
		self.lcdNumberDROPosY.setObjectName(_fromUtf8("lcdNumberDROPosY"))
		self.gridLayout.addWidget(self.lcdNumberDROPosY, 1, 2, 1, 1)
		self.lcdNumberDROPosX2 = QtGui.QLCDNumber(self.centralwidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lcdNumberDROPosX2.sizePolicy().hasHeightForWidth())
		self.lcdNumberDROPosX2.setSizePolicy(sizePolicy)
		self.lcdNumberDROPosX2.setMinimumSize(QtCore.QSize(0, 46))
		self.lcdNumberDROPosX2.setNumDigits(6)
		self.lcdNumberDROPosX2.setSegmentStyle(QtGui.QLCDNumber.Filled)
		self.lcdNumberDROPosX2.setObjectName(_fromUtf8("lcdNumberDROPosX2"))
		self.gridLayout.addWidget(self.lcdNumberDROPosX2, 1, 1, 1, 1)
		self.label_2 = QtGui.QLabel(self.centralwidget)
		self.label_2.setObjectName(_fromUtf8("label_2"))
		self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
		self.label_3 = QtGui.QLabel(self.centralwidget)
		self.label_3.setObjectName(_fromUtf8("label_3"))
		self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
		self.label_4 = QtGui.QLabel(self.centralwidget)
		self.label_4.setObjectName(_fromUtf8("label_4"))
		self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
		self.label_5 = QtGui.QLabel(self.centralwidget)
		self.label_5.setObjectName(_fromUtf8("label_5"))
		self.gridLayout.addWidget(self.label_5, 0, 4, 1, 1)
		self.pushButtonNotStop = QtGui.QPushButton(self.centralwidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonNotStop.sizePolicy().hasHeightForWidth())
		self.pushButtonNotStop.setSizePolicy(sizePolicy)
		self.pushButtonNotStop.setObjectName(_fromUtf8("pushButtonNotStop"))
		self.gridLayout.addWidget(self.pushButtonNotStop, 0, 5, 3, 1)
		self.lcdNumberDROPosX = QtGui.QLCDNumber(self.centralwidget)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.lcdNumberDROPosX.sizePolicy().hasHeightForWidth())
		self.lcdNumberDROPosX.setSizePolicy(sizePolicy)
		self.lcdNumberDROPosX.setMinimumSize(QtCore.QSize(0, 46))
		self.lcdNumberDROPosX.setNumDigits(6)
		self.lcdNumberDROPosX.setSegmentStyle(QtGui.QLCDNumber.Filled)
		self.lcdNumberDROPosX.setObjectName(_fromUtf8("lcdNumberDROPosX"))
		self.gridLayout.addWidget(self.lcdNumberDROPosX, 1, 0, 1, 1)
		self.label_6 = QtGui.QLabel(self.centralwidget)
		self.label_6.setObjectName(_fromUtf8("label_6"))
		self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
		self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
		self.tabWidget = QtGui.QTabWidget(self.centralwidget)
		self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
		self.tab_2 = QtGui.QWidget()
		self.tab_2.setObjectName(_fromUtf8("tab_2"))
		self.gridLayout_3 = QtGui.QGridLayout(self.tab_2)
		self.gridLayout_3.setMargin(0)
		self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
		self.pushButtonMotorZAus = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonMotorZAus.sizePolicy().hasHeightForWidth())
		self.pushButtonMotorZAus.setSizePolicy(sizePolicy)
		self.pushButtonMotorZAus.setCheckable(True)
		self.pushButtonMotorZAus.setChecked(False)
		self.pushButtonMotorZAus.setDefault(False)
		self.pushButtonMotorZAus.setObjectName(_fromUtf8("pushButtonMotorZAus"))
		self.gridLayout_3.addWidget(self.pushButtonMotorZAus, 4, 7, 1, 1)
		self.pushButtonInitX2 = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonInitX2.sizePolicy().hasHeightForWidth())
		self.pushButtonInitX2.setSizePolicy(sizePolicy)
		self.pushButtonInitX2.setCheckable(False)
		self.pushButtonInitX2.setObjectName(_fromUtf8("pushButtonInitX2"))
		self.gridLayout_3.addWidget(self.pushButtonInitX2, 0, 5, 1, 1)
		self.pushButtonHomeX2 = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonHomeX2.sizePolicy().hasHeightForWidth())
		self.pushButtonHomeX2.setSizePolicy(sizePolicy)
		self.pushButtonHomeX2.setCheckable(True)
		self.pushButtonHomeX2.setObjectName(_fromUtf8("pushButtonHomeX2"))
		self.gridLayout_3.addWidget(self.pushButtonHomeX2, 2, 5, 1, 1)
		self.pushButtonHomeZ = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonHomeZ.sizePolicy().hasHeightForWidth())
		self.pushButtonHomeZ.setSizePolicy(sizePolicy)
		self.pushButtonHomeZ.setCheckable(True)
		self.pushButtonHomeZ.setObjectName(_fromUtf8("pushButtonHomeZ"))
		self.gridLayout_3.addWidget(self.pushButtonHomeZ, 2, 7, 1, 1)
		self.pushButtonInitX = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonInitX.sizePolicy().hasHeightForWidth())
		self.pushButtonInitX.setSizePolicy(sizePolicy)
		self.pushButtonInitX.setCheckable(False)
		self.pushButtonInitX.setObjectName(_fromUtf8("pushButtonInitX"))
		self.gridLayout_3.addWidget(self.pushButtonInitX, 0, 4, 1, 1)
		self.pushButtonInitZ = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonInitZ.sizePolicy().hasHeightForWidth())
		self.pushButtonInitZ.setSizePolicy(sizePolicy)
		self.pushButtonInitZ.setCheckable(False)
		self.pushButtonInitZ.setObjectName(_fromUtf8("pushButtonInitZ"))
		self.gridLayout_3.addWidget(self.pushButtonInitZ, 0, 7, 1, 1)
		self.pushButtonInitY = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonInitY.sizePolicy().hasHeightForWidth())
		self.pushButtonInitY.setSizePolicy(sizePolicy)
		self.pushButtonInitY.setCheckable(False)
		self.pushButtonInitY.setObjectName(_fromUtf8("pushButtonInitY"))
		self.gridLayout_3.addWidget(self.pushButtonInitY, 0, 6, 1, 1)
		self.pushButtonHomeX = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonHomeX.sizePolicy().hasHeightForWidth())
		self.pushButtonHomeX.setSizePolicy(sizePolicy)
		self.pushButtonHomeX.setCheckable(True)
		self.pushButtonHomeX.setObjectName(_fromUtf8("pushButtonHomeX"))
		self.gridLayout_3.addWidget(self.pushButtonHomeX, 2, 4, 1, 1)
		self.pushButtonHomeY = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonHomeY.sizePolicy().hasHeightForWidth())
		self.pushButtonHomeY.setSizePolicy(sizePolicy)
		self.pushButtonHomeY.setCheckable(True)
		self.pushButtonHomeY.setObjectName(_fromUtf8("pushButtonHomeY"))
		self.gridLayout_3.addWidget(self.pushButtonHomeY, 2, 6, 1, 1)
		self.pushButtonMotorXAus = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonMotorXAus.sizePolicy().hasHeightForWidth())
		self.pushButtonMotorXAus.setSizePolicy(sizePolicy)
		self.pushButtonMotorXAus.setCheckable(True)
		self.pushButtonMotorXAus.setChecked(False)
		self.pushButtonMotorXAus.setDefault(False)
		self.pushButtonMotorXAus.setObjectName(_fromUtf8("pushButtonMotorXAus"))
		self.gridLayout_3.addWidget(self.pushButtonMotorXAus, 4, 4, 1, 1)
		self.pushButtonMotorYAus = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonMotorYAus.sizePolicy().hasHeightForWidth())
		self.pushButtonMotorYAus.setSizePolicy(sizePolicy)
		self.pushButtonMotorYAus.setCheckable(True)
		self.pushButtonMotorYAus.setChecked(False)
		self.pushButtonMotorYAus.setDefault(False)
		self.pushButtonMotorYAus.setObjectName(_fromUtf8("pushButtonMotorYAus"))
		self.gridLayout_3.addWidget(self.pushButtonMotorYAus, 4, 6, 1, 1)
		self.pushButtonInitC = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonInitC.sizePolicy().hasHeightForWidth())
		self.pushButtonInitC.setSizePolicy(sizePolicy)
		self.pushButtonInitC.setCheckable(False)
		self.pushButtonInitC.setObjectName(_fromUtf8("pushButtonInitC"))
		self.gridLayout_3.addWidget(self.pushButtonInitC, 0, 8, 1, 1)
		self.pushButtonHomeC = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonHomeC.sizePolicy().hasHeightForWidth())
		self.pushButtonHomeC.setSizePolicy(sizePolicy)
		self.pushButtonHomeC.setCheckable(True)
		self.pushButtonHomeC.setObjectName(_fromUtf8("pushButtonHomeC"))
		self.gridLayout_3.addWidget(self.pushButtonHomeC, 2, 8, 1, 1)
		self.pushButtonMotorCAus = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonMotorCAus.sizePolicy().hasHeightForWidth())
		self.pushButtonMotorCAus.setSizePolicy(sizePolicy)
		self.pushButtonMotorCAus.setCheckable(True)
		self.pushButtonMotorCAus.setChecked(False)
		self.pushButtonMotorCAus.setDefault(False)
		self.pushButtonMotorCAus.setObjectName(_fromUtf8("pushButtonMotorCAus"))
		self.gridLayout_3.addWidget(self.pushButtonMotorCAus, 4, 8, 1, 1)
		self.pushButtonMotorX2Aus = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonMotorX2Aus.sizePolicy().hasHeightForWidth())
		self.pushButtonMotorX2Aus.setSizePolicy(sizePolicy)
		self.pushButtonMotorX2Aus.setCheckable(True)
		self.pushButtonMotorX2Aus.setChecked(False)
		self.pushButtonMotorX2Aus.setDefault(False)
		self.pushButtonMotorX2Aus.setObjectName(_fromUtf8("pushButtonMotorX2Aus"))
		self.gridLayout_3.addWidget(self.pushButtonMotorX2Aus, 4, 5, 1, 1)
		self.pushButtonHomeAll = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonHomeAll.sizePolicy().hasHeightForWidth())
		self.pushButtonHomeAll.setSizePolicy(sizePolicy)
		self.pushButtonHomeAll.setCheckable(False)
		self.pushButtonHomeAll.setChecked(False)
		self.pushButtonHomeAll.setDefault(False)
		self.pushButtonHomeAll.setObjectName(_fromUtf8("pushButtonHomeAll"))
		self.gridLayout_3.addWidget(self.pushButtonHomeAll, 0, 3, 1, 1)
		self.pushButtonGoX0Y0 = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonGoX0Y0.sizePolicy().hasHeightForWidth())
		self.pushButtonGoX0Y0.setSizePolicy(sizePolicy)
		self.pushButtonGoX0Y0.setCheckable(False)
		self.pushButtonGoX0Y0.setObjectName(_fromUtf8("pushButtonGoX0Y0"))
		self.gridLayout_3.addWidget(self.pushButtonGoX0Y0, 2, 1, 1, 1)
		self.pushButtonReadPos = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonReadPos.sizePolicy().hasHeightForWidth())
		self.pushButtonReadPos.setSizePolicy(sizePolicy)
		self.pushButtonReadPos.setCheckable(True)
		self.pushButtonReadPos.setChecked(True)
		self.pushButtonReadPos.setDefault(False)
		self.pushButtonReadPos.setObjectName(_fromUtf8("pushButtonReadPos"))
		self.gridLayout_3.addWidget(self.pushButtonReadPos, 0, 1, 1, 1)
		self.pushButtonGoX20 = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonGoX20.sizePolicy().hasHeightForWidth())
		self.pushButtonGoX20.setSizePolicy(sizePolicy)
		self.pushButtonGoX20.setCheckable(False)
		self.pushButtonGoX20.setObjectName(_fromUtf8("pushButtonGoX20"))
		self.gridLayout_3.addWidget(self.pushButtonGoX20, 4, 1, 1, 1)
		self.pushButtonGoZmax = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonGoZmax.sizePolicy().hasHeightForWidth())
		self.pushButtonGoZmax.setSizePolicy(sizePolicy)
		self.pushButtonGoZmax.setCheckable(False)
		self.pushButtonGoZmax.setObjectName(_fromUtf8("pushButtonGoZmax"))
		self.gridLayout_3.addWidget(self.pushButtonGoZmax, 2, 3, 1, 1)
		self.pushButtonGoC0 = QtGui.QPushButton(self.tab_2)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonGoC0.sizePolicy().hasHeightForWidth())
		self.pushButtonGoC0.setSizePolicy(sizePolicy)
		self.pushButtonGoC0.setCheckable(False)
		self.pushButtonGoC0.setObjectName(_fromUtf8("pushButtonGoC0"))
		self.gridLayout_3.addWidget(self.pushButtonGoC0, 4, 3, 1, 1)
		self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
		self.tab = QtGui.QWidget()
		self.tab.setObjectName(_fromUtf8("tab"))
		self.gridLayout_4 = QtGui.QGridLayout(self.tab)
		self.gridLayout_4.setMargin(0)
		self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
		self.label_8 = QtGui.QLabel(self.tab)
		self.label_8.setObjectName(_fromUtf8("label_8"))
		self.gridLayout_4.addWidget(self.label_8, 6, 0, 1, 1)
		self.Yset = QtGui.QSlider(self.tab)
		self.Yset.setMinimum(-19260)
		self.Yset.setMaximum(22080)
		self.Yset.setPageStep(100)
		self.Yset.setOrientation(QtCore.Qt.Vertical)
		self.Yset.setTickPosition(QtGui.QSlider.TicksBelow)
		self.Yset.setTickInterval(1000)
		self.Yset.setObjectName(_fromUtf8("Yset"))
		self.gridLayout_4.addWidget(self.Yset, 2, 4, 1, 1)
		self.X2set = QtGui.QSlider(self.tab)
		self.X2set.setMinimum(-4600)
		self.X2set.setMaximum(7500)
		self.X2set.setPageStep(100)
		self.X2set.setOrientation(QtCore.Qt.Horizontal)
		self.X2set.setInvertedAppearance(True)
		self.X2set.setTickPosition(QtGui.QSlider.TicksAbove)
		self.X2set.setTickInterval(1000)
		self.X2set.setObjectName(_fromUtf8("X2set"))
		self.gridLayout_4.addWidget(self.X2set, 6, 3, 1, 1)
		self.spinBoxX2 = QtGui.QSpinBox(self.tab)
		self.spinBoxX2.setMinimum(-4600)
		self.spinBoxX2.setMaximum(7500)
		self.spinBoxX2.setObjectName(_fromUtf8("spinBoxX2"))
		self.gridLayout_4.addWidget(self.spinBoxX2, 6, 1, 1, 2)
		self.spinBoxVmax = QtGui.QSpinBox(self.tab)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.spinBoxVmax.sizePolicy().hasHeightForWidth())
		self.spinBoxVmax.setSizePolicy(sizePolicy)
		self.spinBoxVmax.setMaximum(200000)
		self.spinBoxVmax.setProperty("value", 20000)
		self.spinBoxVmax.setObjectName(_fromUtf8("spinBoxVmax"))
		self.gridLayout_4.addWidget(self.spinBoxVmax, 7, 2, 1, 1)
		self.label_11 = QtGui.QLabel(self.tab)
		self.label_11.setObjectName(_fromUtf8("label_11"))
		self.gridLayout_4.addWidget(self.label_11, 0, 5, 1, 1)
		self.spinBoxX = QtGui.QSpinBox(self.tab)
		self.spinBoxX.setMinimum(-16000)
		self.spinBoxX.setMaximum(16300)
		self.spinBoxX.setObjectName(_fromUtf8("spinBoxX"))
		self.gridLayout_4.addWidget(self.spinBoxX, 4, 1, 2, 2)
		self.label_12 = QtGui.QLabel(self.tab)
		self.label_12.setObjectName(_fromUtf8("label_12"))
		self.gridLayout_4.addWidget(self.label_12, 7, 0, 1, 2)
		self.label_9 = QtGui.QLabel(self.tab)
		self.label_9.setObjectName(_fromUtf8("label_9"))
		self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
		self.spinBoxC = QtGui.QSpinBox(self.tab)
		self.spinBoxC.setMinimum(-4100)
		self.spinBoxC.setMaximum(4100)
		self.spinBoxC.setObjectName(_fromUtf8("spinBoxC"))
		self.gridLayout_4.addWidget(self.spinBoxC, 0, 2, 1, 1)
		self.label_7 = QtGui.QLabel(self.tab)
		self.label_7.setObjectName(_fromUtf8("label_7"))
		self.gridLayout_4.addWidget(self.label_7, 4, 0, 1, 1)
		self.spinBoxY = QtGui.QSpinBox(self.tab)
		self.spinBoxY.setMinimum(-19260)
		self.spinBoxY.setMaximum(22080)
		self.spinBoxY.setSingleStep(1)
		self.spinBoxY.setObjectName(_fromUtf8("spinBoxY"))
		self.gridLayout_4.addWidget(self.spinBoxY, 1, 4, 1, 1)
		self.Zset = QtGui.QSlider(self.tab)
		self.Zset.setMaximum(104000)
		self.Zset.setPageStep(100)
		self.Zset.setProperty("value", 100000)
		self.Zset.setOrientation(QtCore.Qt.Vertical)
		self.Zset.setTickPosition(QtGui.QSlider.TicksBelow)
		self.Zset.setTickInterval(10000)
		self.Zset.setObjectName(_fromUtf8("Zset"))
		self.gridLayout_4.addWidget(self.Zset, 2, 5, 1, 1)
		self.label_10 = QtGui.QLabel(self.tab)
		self.label_10.setObjectName(_fromUtf8("label_10"))
		self.gridLayout_4.addWidget(self.label_10, 0, 4, 1, 1)
		self.spinBoxZ = QtGui.QSpinBox(self.tab)
		self.spinBoxZ.setMaximum(104000)
		self.spinBoxZ.setProperty("value", 100000)
		self.spinBoxZ.setObjectName(_fromUtf8("spinBoxZ"))
		self.gridLayout_4.addWidget(self.spinBoxZ, 1, 5, 1, 1)
		self.Cset = QtGui.QDial(self.tab)
		self.Cset.setMinimum(-4100)
		self.Cset.setMaximum(4100)
		self.Cset.setPageStep(50)
		self.Cset.setSliderPosition(0)
		self.Cset.setInvertedAppearance(True)
		self.Cset.setWrapping(True)
		self.Cset.setNotchTarget(10.0)
		self.Cset.setNotchesVisible(True)
		self.Cset.setObjectName(_fromUtf8("Cset"))
		self.gridLayout_4.addWidget(self.Cset, 0, 3, 3, 1)
		self.X1set = QtGui.QSlider(self.tab)
		self.X1set.setMinimum(-16000)
		self.X1set.setMaximum(16300)
		self.X1set.setPageStep(100)
		self.X1set.setOrientation(QtCore.Qt.Horizontal)
		self.X1set.setTickPosition(QtGui.QSlider.TicksAbove)
		self.X1set.setTickInterval(1000)
		self.X1set.setObjectName(_fromUtf8("X1set"))
		self.gridLayout_4.addWidget(self.X1set, 4, 3, 2, 1)
		self.pushButtonGo = QtGui.QPushButton(self.tab)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.pushButtonGo.sizePolicy().hasHeightForWidth())
		self.pushButtonGo.setSizePolicy(sizePolicy)
		self.pushButtonGo.setObjectName(_fromUtf8("pushButtonGo"))
		self.gridLayout_4.addWidget(self.pushButtonGo, 3, 4, 5, 2)
		self.Vmaxset = QtGui.QSlider(self.tab)
		self.Vmaxset.setMaximum(200000)
		self.Vmaxset.setPageStep(100)
		self.Vmaxset.setProperty("value", 20000)
		self.Vmaxset.setSliderPosition(20000)
		self.Vmaxset.setOrientation(QtCore.Qt.Horizontal)
		self.Vmaxset.setTickPosition(QtGui.QSlider.TicksAbove)
		self.Vmaxset.setTickInterval(1000)
		self.Vmaxset.setObjectName(_fromUtf8("Vmaxset"))
		self.gridLayout_4.addWidget(self.Vmaxset, 7, 3, 1, 1)
		self.tabWidget.addTab(self.tab, _fromUtf8(""))
		self.tab_3 = QtGui.QWidget()
		self.tab_3.setObjectName(_fromUtf8("tab_3"))
		self.gridLayout_5 = QtGui.QGridLayout(self.tab_3)
		self.gridLayout_5.setMargin(0)
		self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
		self.label_15 = QtGui.QLabel(self.tab_3)
		self.label_15.setObjectName(_fromUtf8("label_15"))
		self.gridLayout_5.addWidget(self.label_15, 0, 0, 1, 1)
		self.pushButtonSendMsg = QtGui.QPushButton(self.tab_3)
		self.pushButtonSendMsg.setCheckable(False)
		self.pushButtonSendMsg.setChecked(False)
		self.pushButtonSendMsg.setDefault(False)
		self.pushButtonSendMsg.setObjectName(_fromUtf8("pushButtonSendMsg"))
		self.gridLayout_5.addWidget(self.pushButtonSendMsg, 0, 1, 1, 1)
		self.plainTextEditSendMsg = QtGui.QPlainTextEdit(self.tab_3)
		self.plainTextEditSendMsg.setObjectName(_fromUtf8("plainTextEditSendMsg"))
		self.gridLayout_5.addWidget(self.plainTextEditSendMsg, 1, 0, 1, 2)
		self.label_13 = QtGui.QLabel(self.tab_3)
		self.label_13.setObjectName(_fromUtf8("label_13"))
		self.gridLayout_5.addWidget(self.label_13, 2, 0, 1, 1)
		self.label_14 = QtGui.QLabel(self.tab_3)
		self.label_14.setObjectName(_fromUtf8("label_14"))
		self.gridLayout_5.addWidget(self.label_14, 2, 2, 1, 1)
		self.pushButtonCanlog = QtGui.QPushButton(self.tab_3)
		self.pushButtonCanlog.setCheckable(True)
		self.pushButtonCanlog.setChecked(False)
		self.pushButtonCanlog.setDefault(False)
		self.pushButtonCanlog.setObjectName(_fromUtf8("pushButtonCanlog"))
		self.gridLayout_5.addWidget(self.pushButtonCanlog, 3, 0, 1, 1)
		self.pushButtonClearCanlog = QtGui.QPushButton(self.tab_3)
		self.pushButtonClearCanlog.setCheckable(False)
		self.pushButtonClearCanlog.setChecked(False)
		self.pushButtonClearCanlog.setDefault(False)
		self.pushButtonClearCanlog.setObjectName(_fromUtf8("pushButtonClearCanlog"))
		self.gridLayout_5.addWidget(self.pushButtonClearCanlog, 3, 1, 1, 1)
		self.pushButtonSocketlog = QtGui.QPushButton(self.tab_3)
		self.pushButtonSocketlog.setCheckable(True)
		self.pushButtonSocketlog.setChecked(False)
		self.pushButtonSocketlog.setDefault(False)
		self.pushButtonSocketlog.setObjectName(_fromUtf8("pushButtonSocketlog"))
		self.gridLayout_5.addWidget(self.pushButtonSocketlog, 3, 2, 1, 1)
		self.pushButtonClearSocketlog = QtGui.QPushButton(self.tab_3)
		self.pushButtonClearSocketlog.setCheckable(False)
		self.pushButtonClearSocketlog.setChecked(False)
		self.pushButtonClearSocketlog.setDefault(False)
		self.pushButtonClearSocketlog.setObjectName(_fromUtf8("pushButtonClearSocketlog"))
		self.gridLayout_5.addWidget(self.pushButtonClearSocketlog, 3, 3, 1, 1)
		self.plainTextEditCanLog = QtGui.QPlainTextEdit(self.tab_3)
		self.plainTextEditCanLog.setObjectName(_fromUtf8("plainTextEditCanLog"))
		self.gridLayout_5.addWidget(self.plainTextEditCanLog, 4, 0, 1, 2)
		self.plainTextEditSocketLog = QtGui.QPlainTextEdit(self.tab_3)
		self.plainTextEditSocketLog.setObjectName(_fromUtf8("plainTextEditSocketLog"))
		self.gridLayout_5.addWidget(self.plainTextEditSocketLog, 4, 2, 1, 2)
		self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
		self.tab_4 = QtGui.QWidget()
		self.tab_4.setObjectName(_fromUtf8("tab_4"))
		self.pushButtonJoysticMode = QtGui.QPushButton(self.tab_4)
		self.pushButtonJoysticMode.setGeometry(QtCore.QRect(10, 10, 111, 71))
		self.pushButtonJoysticMode.setCheckable(True)
		self.pushButtonJoysticMode.setObjectName(_fromUtf8("pushButtonJoysticMode"))
		self.pushButtonbCNCMode = QtGui.QPushButton(self.tab_4)
		self.pushButtonbCNCMode.setGeometry(QtCore.QRect(150, 10, 111, 71))
		self.pushButtonbCNCMode.setCheckable(True)
		self.pushButtonbCNCMode.setObjectName(_fromUtf8("pushButtonbCNCMode"))
		self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
		self.gridLayout_2.addWidget(self.tabWidget, 1, 0, 1, 1)
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtGui.QMenuBar(MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 25))
		self.menubar.setObjectName(_fromUtf8("menubar"))
		self.menuFile = QtGui.QMenu(self.menubar)
		self.menuFile.setObjectName(_fromUtf8("menuFile"))
		self.menuHelp = QtGui.QMenu(self.menubar)
		self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtGui.QStatusBar(MainWindow)
		self.statusbar.setObjectName(_fromUtf8("statusbar"))
		MainWindow.setStatusBar(self.statusbar)
		self.actionExit = QtGui.QAction(MainWindow)
		self.actionExit.setObjectName(_fromUtf8("actionExit"))
		self.actionAbout = QtGui.QAction(MainWindow)
		self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
		self.actionHelp = QtGui.QAction(MainWindow)
		self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
		self.menuFile.addAction(self.actionExit)
		self.menuHelp.addAction(self.actionAbout)
		self.menuHelp.addAction(self.actionHelp)
		self.menubar.addAction(self.menuFile.menuAction())
		self.menubar.addAction(self.menuHelp.menuAction())

		self.retranslateUi(MainWindow)
		self.tabWidget.setCurrentIndex(0)
		QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
		QtCore.QObject.connect(self.Cset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxC.setValue)
		QtCore.QObject.connect(self.spinBoxC, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Cset.setValue)
		QtCore.QObject.connect(self.spinBoxZ, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Zset.setValue)
		QtCore.QObject.connect(self.Zset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxZ.setValue)
		QtCore.QObject.connect(self.spinBoxY, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Yset.setValue)
		QtCore.QObject.connect(self.Yset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxY.setValue)
		QtCore.QObject.connect(self.spinBoxX, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.X1set.setValue)
		QtCore.QObject.connect(self.X1set, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxX.setValue)
		QtCore.QObject.connect(self.spinBoxX2, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.X2set.setValue)
		QtCore.QObject.connect(self.X2set, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxX2.setValue)
		QtCore.QObject.connect(self.pushButtonClearCanlog, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEditCanLog.clear)
		QtCore.QObject.connect(self.pushButtonClearSocketlog, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEditSocketLog.clear)
		QtCore.QObject.connect(self.spinBoxVmax, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.Vmaxset.setValue)
		QtCore.QObject.connect(self.Vmaxset, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.spinBoxVmax.setValue)
		QtCore.QObject.connect(self.pushButtonNotStop, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButtonMotorXAus.setChecked)
		QtCore.QObject.connect(self.pushButtonNotStop, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButtonMotorX2Aus.setChecked)
		QtCore.QObject.connect(self.pushButtonNotStop, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButtonMotorYAus.setChecked)
		QtCore.QObject.connect(self.pushButtonNotStop, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButtonMotorZAus.setChecked)
		QtCore.QObject.connect(self.pushButtonNotStop, QtCore.SIGNAL(_fromUtf8("clicked(bool)")), self.pushButtonMotorCAus.setChecked)
		QtCore.QObject.connect(self.pushButtonHomeAll, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonHomeX.click)
		QtCore.QObject.connect(self.pushButtonHomeAll, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonHomeX2.click)
		QtCore.QObject.connect(self.pushButtonHomeAll, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonHomeY.click)
		QtCore.QObject.connect(self.pushButtonHomeAll, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonHomeZ.click)
		QtCore.QObject.connect(self.pushButtonHomeAll, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonHomeC.click)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)
		MainWindow.setTabOrder(self.tabWidget, self.pushButtonInitX)
		MainWindow.setTabOrder(self.pushButtonInitX, self.pushButtonInitY)
		MainWindow.setTabOrder(self.pushButtonInitY, self.pushButtonInitZ)
		MainWindow.setTabOrder(self.pushButtonInitZ, self.pushButtonHomeX)
		MainWindow.setTabOrder(self.pushButtonHomeX, self.pushButtonHomeY)
		MainWindow.setTabOrder(self.pushButtonHomeY, self.pushButtonHomeZ)

	def retranslateUi(self, MainWindow):
		MainWindow.setWindowTitle(_translate("MainWindow", "Openpnp CAN Middleware", None))
		self.label_2.setText(_translate("MainWindow", "X2", None))
		self.label_3.setText(_translate("MainWindow", "Y", None))
		self.label_4.setText(_translate("MainWindow", "Z", None))
		self.label_5.setText(_translate("MainWindow", "C", None))
		self.pushButtonNotStop.setText(_translate("MainWindow", "Not Stop", None))
		self.label_6.setText(_translate("MainWindow", "X", None))
		self.pushButtonMotorZAus.setText(_translate("MainWindow", "Motor Z an", None))
		self.pushButtonInitX2.setText(_translate("MainWindow", "Init X2 Regler", None))
		self.pushButtonHomeX2.setText(_translate("MainWindow", "Home X2", None))
		self.pushButtonHomeZ.setText(_translate("MainWindow", "Home Z", None))
		self.pushButtonInitX.setText(_translate("MainWindow", "Init X Regler", None))
		self.pushButtonInitZ.setText(_translate("MainWindow", "Init Z Regler", None))
		self.pushButtonInitY.setText(_translate("MainWindow", "Init Y Regler", None))
		self.pushButtonHomeX.setText(_translate("MainWindow", "Home X", None))
		self.pushButtonHomeY.setText(_translate("MainWindow", "Home Y", None))
		self.pushButtonMotorXAus.setText(_translate("MainWindow", "Motor X an", None))
		self.pushButtonMotorYAus.setText(_translate("MainWindow", "Motor Y an", None))
		self.pushButtonInitC.setText(_translate("MainWindow", "Init C Regler", None))
		self.pushButtonHomeC.setText(_translate("MainWindow", "Home C", None))
		self.pushButtonMotorCAus.setText(_translate("MainWindow", "Motor C an", None))
		self.pushButtonMotorX2Aus.setText(_translate("MainWindow", "Motor X2 an", None))
		self.pushButtonHomeAll.setText(_translate("MainWindow", "Home All", None))
		self.pushButtonGoX0Y0.setText(_translate("MainWindow", "Go X0 Y0", None))
		self.pushButtonReadPos.setText(_translate("MainWindow", "Read Positions", None))
		self.pushButtonGoX20.setText(_translate("MainWindow", "Go X2 7500", None))
		self.pushButtonGoZmax.setText(_translate("MainWindow", "Go Z 100000", None))
		self.pushButtonGoC0.setText(_translate("MainWindow", "Go C 0 ", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Homing", None))
		self.label_8.setText(_translate("MainWindow", "X2", None))
		self.label_11.setText(_translate("MainWindow", "Z", None))
		self.label_12.setText(_translate("MainWindow", "Vmax", None))
		self.label_9.setText(_translate("MainWindow", "C", None))
		self.label_7.setText(_translate("MainWindow", "X1", None))
		self.label_10.setText(_translate("MainWindow", "Y", None))
		self.pushButtonGo.setText(_translate("MainWindow", "Go", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Pos Testing", None))
		self.label_15.setText(_translate("MainWindow", "Send Msg", None))
		self.pushButtonSendMsg.setText(_translate("MainWindow", "Send Msg", None))
		self.label_13.setText(_translate("MainWindow", "CANlog", None))
		self.label_14.setText(_translate("MainWindow", "Socket Log ", None))
		self.pushButtonCanlog.setText(_translate("MainWindow", "Canlog", None))
		self.pushButtonClearCanlog.setText(_translate("MainWindow", "ClearCanlog", None))
		self.pushButtonSocketlog.setText(_translate("MainWindow", "Socketlog", None))
		self.pushButtonClearSocketlog.setText(_translate("MainWindow", "ClearSocketlog", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Log", None))
		self.pushButtonJoysticMode.setText(_translate("MainWindow", "Joystic mode", None))
		self.pushButtonbCNCMode.setText(_translate("MainWindow", "bCNC mode", None))
		self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Setting", None))
		self.menuFile.setTitle(_translate("MainWindow", "File", None))
		self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
		self.actionExit.setText(_translate("MainWindow", "Exit", None))
		self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
		self.actionAbout.setText(_translate("MainWindow", "About", None))
		self.actionHelp.setText(_translate("MainWindow", "Help", None))
		self.actionHelp.setShortcut(_translate("MainWindow", "F1", None))


if __name__ == "__main__":
	import sys
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	sys.exit(app.exec_())

