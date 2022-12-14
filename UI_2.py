from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_w_calibration(object):
    def setupUi(self, w_calibration):
        w_calibration.setObjectName("w_calibration")
        w_calibration.setEnabled(True)
        w_calibration.resize(560, 440)
        self.fill_in_table = QtWidgets.QTableView(w_calibration)
        self.fill_in_table.setGeometry(QtCore.QRect(10, 10, 181, 201))
        self.fill_in_table.setObjectName("fill_in_table")
        self.label = QtWidgets.QLabel(w_calibration)
        self.label.setGeometry(QtCore.QRect(20, 20, 47, 12))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(w_calibration)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 47, 12))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(w_calibration)
        self.label_3.setGeometry(QtCore.QRect(20, 60, 47, 12))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(w_calibration)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 47, 12))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(w_calibration)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 47, 12))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(w_calibration)
        self.label_6.setGeometry(QtCore.QRect(20, 120, 47, 12))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(w_calibration)
        self.label_7.setGeometry(QtCore.QRect(20, 140, 47, 12))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(w_calibration)
        self.label_8.setGeometry(QtCore.QRect(20, 160, 47, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(w_calibration)
        self.label_9.setGeometry(QtCore.QRect(70, 20, 47, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(w_calibration)
        self.label_10.setGeometry(QtCore.QRect(70, 40, 47, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(w_calibration)
        self.label_11.setGeometry(QtCore.QRect(70, 60, 47, 12))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(w_calibration)
        self.label_12.setGeometry(QtCore.QRect(70, 80, 47, 12))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(w_calibration)
        self.label_13.setGeometry(QtCore.QRect(70, 100, 47, 12))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(w_calibration)
        self.label_14.setGeometry(QtCore.QRect(70, 120, 47, 12))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(w_calibration)
        self.label_15.setGeometry(QtCore.QRect(70, 140, 47, 12))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(w_calibration)
        self.label_16.setGeometry(QtCore.QRect(70, 160, 47, 12))
        self.label_16.setObjectName("label_16")
        self.lambda1 = QtWidgets.QLineEdit(w_calibration)
        self.lambda1.setGeometry(QtCore.QRect(120, 40, 61, 16))
        self.lambda1.setText("")
        self.lambda1.setObjectName("lambda1")
        self.lambda2 = QtWidgets.QLineEdit(w_calibration)
        self.lambda2.setGeometry(QtCore.QRect(120, 60, 61, 16))
        self.lambda2.setText("")
        self.lambda2.setObjectName("lambda2")
        self.lambda3 = QtWidgets.QLineEdit(w_calibration)
        self.lambda3.setGeometry(QtCore.QRect(120, 80, 61, 16))
        self.lambda3.setText("")
        self.lambda3.setObjectName("lambda3")
        self.lambda4 = QtWidgets.QLineEdit(w_calibration)
        self.lambda4.setGeometry(QtCore.QRect(120, 100, 61, 16))
        self.lambda4.setText("")
        self.lambda4.setObjectName("lambda4")
        self.lambda5 = QtWidgets.QLineEdit(w_calibration)
        self.lambda5.setGeometry(QtCore.QRect(120, 120, 61, 16))
        self.lambda5.setText("")
        self.lambda5.setObjectName("lambda5")
        self.lambda6 = QtWidgets.QLineEdit(w_calibration)
        self.lambda6.setGeometry(QtCore.QRect(120, 140, 61, 16))
        self.lambda6.setText("")
        self.lambda6.setObjectName("lambda6")
        self.lambda7 = QtWidgets.QLineEdit(w_calibration)
        self.lambda7.setGeometry(QtCore.QRect(120, 160, 61, 16))
        self.lambda7.setText("")
        self.lambda7.setObjectName("lambda7")
        self.openGLWidget = QtWidgets.QOpenGLWidget(w_calibration)
        self.openGLWidget.setGeometry(QtCore.QRect(220, 10, 300, 200))
        self.openGLWidget.setObjectName("openGLWidget")
        self.openGLWidget_2 = QtWidgets.QOpenGLWidget(w_calibration)
        self.openGLWidget_2.setGeometry(QtCore.QRect(220, 220, 300, 200))
        self.openGLWidget_2.setObjectName("openGLWidget_2")
        self.tableView = QtWidgets.QTableView(w_calibration)
        self.tableView.setGeometry(QtCore.QRect(10, 230, 131, 101))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(w_calibration)
        self.pushButton.setGeometry(QtCore.QRect(104, 180, 81, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_17 = QtWidgets.QLabel(w_calibration)
        self.label_17.setGeometry(QtCore.QRect(20, 240, 21, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(w_calibration)
        self.label_18.setGeometry(QtCore.QRect(20, 260, 21, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(w_calibration)
        self.label_19.setGeometry(QtCore.QRect(20, 280, 21, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(w_calibration)
        self.label_20.setGeometry(QtCore.QRect(20, 300, 21, 16))
        self.label_20.setObjectName("label_20")
        self.a3_label = QtWidgets.QLabel(w_calibration)
        self.a3_label.setGeometry(QtCore.QRect(50, 240, 47, 12))
        self.a3_label.setObjectName("a3_label")
        self.a2_label = QtWidgets.QLabel(w_calibration)
        self.a2_label.setGeometry(QtCore.QRect(50, 260, 47, 12))
        self.a2_label.setObjectName("a2_label")
        self.a1_label = QtWidgets.QLabel(w_calibration)
        self.a1_label.setGeometry(QtCore.QRect(50, 280, 47, 12))
        self.a1_label.setObjectName("a1_label")
        self.a0_label = QtWidgets.QLabel(w_calibration)
        self.a0_label.setGeometry(QtCore.QRect(50, 300, 47, 12))
        self.a0_label.setObjectName("a0_label")

        self.retranslateUi(w_calibration)
        QtCore.QMetaObject.connectSlotsByName(w_calibration)

    def retranslateUi(self, w_calibration):
        _translate = QtCore.QCoreApplication.translate
        w_calibration.setWindowTitle(_translate("w_calibration", "Wavelength Calibration"))
        self.label.setText(_translate("w_calibration", "Number"))
        self.label_2.setText(_translate("w_calibration", "1"))
        self.label_3.setText(_translate("w_calibration", "2"))
        self.label_4.setText(_translate("w_calibration", "3"))
        self.label_5.setText(_translate("w_calibration", "4"))
        self.label_6.setText(_translate("w_calibration", "5"))
        self.label_7.setText(_translate("w_calibration", "6"))
        self.label_8.setText(_translate("w_calibration", "7"))
        self.label_9.setText(_translate("w_calibration", "Lambda"))
        self.label_10.setText(_translate("w_calibration", "404.656"))
        self.label_11.setText(_translate("w_calibration", "435.833"))
        self.label_12.setText(_translate("w_calibration", "546.074"))
        self.label_13.setText(_translate("w_calibration", "696.543"))
        self.label_14.setText(_translate("w_calibration", "763.511"))
        self.label_15.setText(_translate("w_calibration", "811.531"))
        self.label_16.setText(_translate("w_calibration", "912.297"))
        self.pushButton.setText(_translate("w_calibration", "CALCULATE"))
        self.label_17.setText(_translate("w_calibration", "a3"))
        self.label_18.setText(_translate("w_calibration", "a2"))
        self.label_19.setText(_translate("w_calibration", "a1"))
        self.label_20.setText(_translate("w_calibration", "a0"))
        self.a3_label.setText(_translate("w_calibration", "---"))
        self.a2_label.setText(_translate("w_calibration", "---"))
        self.a1_label.setText(_translate("w_calibration", "---"))
        self.a0_label.setText(_translate("w_calibration", "---"))
        
        self.lambda1.setValidator(QtGui.QDoubleValidator())
        self.lambda2.setValidator(QtGui.QDoubleValidator())
        self.lambda3.setValidator(QtGui.QDoubleValidator())
        self.lambda4.setValidator(QtGui.QDoubleValidator())
        self.lambda5.setValidator(QtGui.QDoubleValidator())
        self.lambda6.setValidator(QtGui.QDoubleValidator())
        self.lambda7.setValidator(QtGui.QDoubleValidator())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w_calibration = QtWidgets.QDialog()
    ui = Ui_w_calibration()
    ui.setupUi(w_calibration)
    w_calibration.show()
    sys.exit(app.exec_())
