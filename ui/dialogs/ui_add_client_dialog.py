# Form implementation generated from reading ui file 'ui/dialogs/addClientDialog.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddClientDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 364)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(130, 20, 211, 22))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.nameAddEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.nameAddEdit.setGeometry(QtCore.QRect(120, 70, 191, 30))
        self.nameAddEdit.setObjectName("nameAddEdit")
        self.surnameAddEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.surnameAddEdit.setGeometry(QtCore.QRect(120, 120, 191, 30))
        self.surnameAddEdit.setObjectName("surnameAddEdit")
        self.emailAddEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.emailAddEdit.setGeometry(QtCore.QRect(120, 270, 191, 30))
        self.emailAddEdit.setObjectName("emailAddEdit")
        self.genderAddEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.genderAddEdit.setGeometry(QtCore.QRect(120, 220, 191, 30))
        self.genderAddEdit.setObjectName("genderAddEdit")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 67, 22))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 120, 67, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 67, 22))
        self.label_4.setObjectName("label_4")
        self.comboBoxMembership = QtWidgets.QComboBox(parent=Dialog)
        self.comboBoxMembership.setGeometry(QtCore.QRect(120, 170, 191, 30))
        self.comboBoxMembership.setObjectName("comboBoxMembership")
        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 170, 91, 22))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(10, 270, 67, 22))
        self.label_6.setObjectName("label_6")
        self.addClientButton = QtWidgets.QPushButton(parent=Dialog)
        self.addClientButton.setGeometry(QtCore.QRect(160, 320, 91, 30))
        self.addClientButton.setObjectName("addClientButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Добавить клиента"))
        self.label_2.setText(_translate("Dialog", "Имя"))
        self.label_3.setText(_translate("Dialog", "Фамилия"))
        self.label_4.setText(_translate("Dialog", "Пол"))
        self.label_5.setText(_translate("Dialog", "Абонемент"))
        self.label_6.setText(_translate("Dialog", "Почта"))
        self.addClientButton.setText(_translate("Dialog", "Добавить"))
