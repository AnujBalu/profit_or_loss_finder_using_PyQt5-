
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(405, 103)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(200, 50, 181, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.yes_month_input = QtWidgets.QPushButton(self.widget)
        self.yes_month_input.setObjectName("yes_month_input")
        self.horizontalLayout.addWidget(self.yes_month_input)
        self.no_month_input = QtWidgets.QPushButton(self.widget)
        self.no_month_input.setObjectName("no_month_input")
        self.horizontalLayout.addWidget(self.no_month_input)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "month_question"))
        self.label.setText(_translate("Dialog", "Do you get constant salary every month ?"))
        self.yes_month_input.setText(_translate("Dialog", "Yes"))
        self.no_month_input.setText(_translate("Dialog", "No"))
