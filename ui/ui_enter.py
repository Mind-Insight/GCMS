# Form implementation generated from reading ui file 'enter.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EnterWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 485)
        self.enterLabel = QtWidgets.QLabel(parent=Dialog)
        self.enterLabel.setGeometry(QtCore.QRect(50, 80, 381, 22))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(16)
        self.enterLabel.setFont(font)
        self.enterLabel.setObjectName("enterLabel")
        self.loginEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.loginEdit.setGeometry(QtCore.QRect(180, 200, 171, 30))
        self.loginEdit.setText("")
        self.loginEdit.setObjectName("loginEdit")
        self.passwordEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.passwordEdit.setGeometry(QtCore.QRect(180, 260, 171, 30))
        self.passwordEdit.setText("")
        self.passwordEdit.setObjectName("passwordEdit")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 67, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(70, 260, 67, 22))
        self.label_3.setObjectName("label_3")
        self.enterButton = QtWidgets.QPushButton(parent=Dialog)
        self.enterButton.setGeometry(QtCore.QRect(210, 330, 111, 30))
        self.enterButton.setObjectName("enterButton")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 450, 141, 30))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.enterLabel.setText(_translate("Dialog", "Название"))
        self.label_2.setText(_translate("Dialog", "Логин"))
        self.label_3.setText(_translate("Dialog", "Пароль"))
        self.enterButton.setText(_translate("Dialog", "Войти"))
        self.pushButton.setText(_translate("Dialog", "Добавить админа"))