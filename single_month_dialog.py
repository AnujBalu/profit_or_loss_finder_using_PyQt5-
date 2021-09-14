
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_single_month(object):
    def setupUi(self, single_month):
        single_month.setObjectName("single_month")
        single_month.resize(405, 167)
        self.label = QtWidgets.QLabel(single_month)
        self.label.setGeometry(QtCore.QRect(100, 0, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.single_monthly_input = QtWidgets.QDoubleSpinBox(single_month,maximum=100000000000000000,minimum=0)
        self.single_monthly_input.setGeometry(QtCore.QRect(120, 60, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.single_monthly_input.setFont(font)
        self.single_monthly_input.setObjectName("single_monthly_input")
        self.ok_monthly_wage = QtWidgets.QDialogButtonBox(single_month)
        self.ok_monthly_wage.setGeometry(QtCore.QRect(210, 120, 156, 23))
        self.ok_monthly_wage.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.ok_monthly_wage.setObjectName("ok_monthly_wage")
        self.widget = QtWidgets.QWidget(single_month)
        self.widget.setGeometry(QtCore.QRect(60, 60, 61, 33))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)

        self.retranslateUi(single_month)
        QtCore.QMetaObject.connectSlotsByName(single_month)

    def retranslateUi(self, single_month):
        _translate = QtCore.QCoreApplication.translate
        single_month.setWindowTitle(_translate("single_month", "single_month_wage"))
        self.label.setText(_translate("single_month", " Monthly salary"))
        self.label_2.setText(_translate("single_month", "Salary"))
