# Form implementation generated from reading ui file 'clients.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ClientsWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(508, 485)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(200, 20, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Noto Sans")
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(parent=Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(30, 90, 441, 261))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 370, 151, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 370, 151, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 370, 141, 30))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Клиенты"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))
        self.pushButton_2.setText(_translate("Dialog", "Редактировать"))
        self.pushButton_3.setText(_translate("Dialog", "Удалить"))