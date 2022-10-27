from PyQt5 import QtCore, QtGui, QtWidgets
import sys, threading, serial, time

ser = serial.Serial()
ser.port = "COM6"
ser.baudrate = 115200 
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 0

mode = 0
hello = 'HI'.encode('utf-8')
path = 'outputfile.txt'
	
class Ui_mainwindow(object):
	def setupUi(self, mainwindow):
		mainwindow.setObjectName("mainwindow")
		mainwindow.resize(831, 510)
		self.centralwidget = QtWidgets.QWidget(mainwindow)
		self.centralwidget.setObjectName("centralwidget")
		self.start = QtWidgets.QPushButton(self.centralwidget)
		self.start.setGeometry(QtCore.QRect(50, 250, 75, 23))
		self.start.setObjectName("start")
		self.format_box = QtWidgets.QComboBox(self.centralwidget)
		self.format_box.setGeometry(QtCore.QRect(200, 20, 69, 22))
		self.format_box.setObjectName("format_box")
		self.format_box.addItem("")
		self.format_box.addItem("")
		self.format_box.addItem("")
		self.shutter_edit = QtWidgets.QTextEdit(self.centralwidget)
		self.shutter_edit.setGeometry(QtCore.QRect(200, 50, 104, 31))
		self.shutter_edit.setObjectName("shutter_edit")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(110, 20, 81, 16))
		self.label.setObjectName("label")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(110, 60, 81, 16))
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(110, 100, 81, 16))
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(110, 140, 81, 16))
		self.label_4.setObjectName("label_4")
		self.anologgain_edit = QtWidgets.QTextEdit(self.centralwidget)
		self.anologgain_edit.setGeometry(QtCore.QRect(200, 90, 104, 31))
		self.anologgain_edit.setObjectName("anologgain_edit")
		self.digitalgain_edit = QtWidgets.QTextEdit(self.centralwidget)
		self.digitalgain_edit.setGeometry(QtCore.QRect(200, 130, 104, 31))
		self.digitalgain_edit.setObjectName("digitalgain_edit")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(60, 210, 91, 16))
		self.label_5.setObjectName("label_5")
		self.x0 = QtWidgets.QTextEdit(self.centralwidget)
		self.x0.setGeometry(QtCore.QRect(160, 200, 31, 31))
		self.x0.setObjectName("x0")
		self.y0 = QtWidgets.QTextEdit(self.centralwidget)
		self.y0.setGeometry(QtCore.QRect(210, 200, 31, 31))
		self.y0.setObjectName("y0")
		self.x1 = QtWidgets.QTextEdit(self.centralwidget)
		self.x1.setGeometry(QtCore.QRect(260, 200, 31, 31))
		self.x1.setObjectName("x1")
		self.y1 = QtWidgets.QTextEdit(self.centralwidget)
		self.y1.setGeometry(QtCore.QRect(310, 200, 31, 31))
		self.y1.setObjectName("y1")
		self.openGLWidget = QtWidgets.QOpenGLWidget(self.centralwidget)
		self.openGLWidget.setGeometry(QtCore.QRect(140, 250, 300, 200))
		self.openGLWidget.setObjectName("openGLWidget")
		self.openGLWidget_2 = QtWidgets.QOpenGLWidget(self.centralwidget)
		self.openGLWidget_2.setGeometry(QtCore.QRect(470, 250, 300, 200))
		self.openGLWidget_2.setObjectName("openGLWidget_2")
		mainwindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(mainwindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 831, 21))
		self.menubar.setObjectName("menubar")
		mainwindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(mainwindow)
		self.statusbar.setObjectName("statusbar")
		mainwindow.setStatusBar(self.statusbar)

		self.retranslateUi(mainwindow)
		QtCore.QMetaObject.connectSlotsByName(mainwindow)
		self.start.clicked.connect(self.start_clicked)
		
	def retranslateUi(self, mainwindow):
		_translate = QtCore.QCoreApplication.translate
		mainwindow.setWindowTitle(_translate("mainwindow", "test"))
		self.start.setText(_translate("mainwindow", "START"))
		self.format_box.setItemText(0, _translate("mainwindow", "BMP"))
		self.format_box.setItemText(1, _translate("mainwindow", "JPG"))
		self.format_box.setItemText(2, _translate("mainwindow", "RAW"))
		self.label.setText(_translate("mainwindow", "Image Format"))
		self.label_2.setText(_translate("mainwindow", "Shutter"))
		self.label_3.setText(_translate("mainwindow", "Anolog Gain"))
		self.label_4.setText(_translate("mainwindow", "Digital Gain"))
		self.label_5.setText(_translate("mainwindow", "ROI : X0 Y0 X1 Y1"))
	
	def start_clicked(self):
		print("hello")

def thread_1():
	print('123123')
	res = ser.readline().decode('utf-8', errors = 'replace')
	if res == 'OK':
		mode = 1
	elif res == "<<EOF>>":
		mode = 2

def receidata():
	print('mode1')
	
	ser.flushInput()
	ser.flushOutput()
	
	f = open(path, 'w')
	while mode == 1:
		res1 = "".join(ser.readline().decode('utf-8'))
		if res != '':
			f.write(res1)

def main():
	print('123')
	
if __name__ == "__main__":
	try:
		thread = threading.Thread(target = thread_1)
		thread.start()
		main()
		
		app = QtWidgets.QApplication(sys.argv)
		mainwindow = QtWidgets.QMainWindow()
		ui = Ui_mainwindow()
		ui.setupUi(mainwindow)
		mainwindow.show()
		sys.exit(app.exec_())
		
		ser.open()
	except Exception as ex:
		print(ex)
		exit()
	
