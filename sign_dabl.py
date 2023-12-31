# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
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
        Form.resize(429, 449)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 431, 461))
        self.label.setText("")
        Form.setWindowIcon(QIcon('C:\pythonProject10\pythonProject3\Dabl\photos\icon_window.png'))
        self.label.setPixmap(QtGui.QPixmap(r"C:\pythonProject10\pythonProject3\Dabl\photos\background_2.png"))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 70, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Impact")
        font.setPointSize(26)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 170, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(64, 64, 64);\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 310, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 380, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Malgun Gothic")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(160, 160, 160);\n"
"color: white;\n"
"border-radius: 5px;\n"
"padding: 10px;")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Autorization"))
        self.lineEdit.setPlaceholderText(_translate("Form", "Login..."))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "Password..."))
        self.pushButton.setText(_translate("Form", "Sign in"))
        self.pushButton_2.setText(_translate("Form", "Sign up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
