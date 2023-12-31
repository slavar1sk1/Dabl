# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dabl_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("Dabl")
        Form.setWindowIcon(QIcon('C:\pythonProject10\pythonProject3\Dabl\photos\icon_window.png'))
        Form.resize(794, 616)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1051, 621))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"C:\pythonProject10\pythonProject3\Dabl\photos\background_1.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semibold")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 200, 231, 71))
        font = QtGui.QFont()
        font.setFamily("Kankin")
        font.setPointSize(28)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 100, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(160, 32, 240);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 360, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Univers 45 Light")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 100, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(160, 32, 240);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 0, 531, 621))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(64, 64, 64);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 480, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Univers 45 Light")
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(200, 100, 255);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(160, 32, 240);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(360, 90, 471, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica-Black")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:white;")
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(290, 190, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid rgb(160, 32, 240);\n"
"border-radius: 30;\n"
"color: white;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(450, 270, 471, 81))
        font = QtGui.QFont()
        font.setFamily("Helvetica-Black")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color:white;")
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(410, 500, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        font.setPointSize(18)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid rgb(160, 32, 240);\n"
"border-radius: 10px;\n"
"color: white;")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 370, 491, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: #22222e;\n"
"border: 2px solid rgb(160, 32, 240);\n"
"border-radius: 30;\n"
"color: white;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("Form", "DABL VOICE 1.0"))
        self.pushButton.setText(_translate("Form", "Сommands"))
        self.pushButton_2.setText(_translate("Form", "LISTEN"))
        self.pushButton_3.setText(_translate("Form", "STOP"))
        self.label_4.setText(_translate("Form", "Recognized Text"))
        self.label_5.setText(_translate("Form", "Mode"))
        self.comboBox.setItemText(0, _translate("Form", "Vosk"))
        self.comboBox.setItemText(1, _translate("Form", "SpeechRecognition"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
