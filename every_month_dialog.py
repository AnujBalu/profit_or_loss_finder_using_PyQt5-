from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(469, 442)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(110, 410, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(50, 50, 78, 331))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_11 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.verticalLayout.addWidget(self.label_11)
        self.label_7 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_12 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.label_9 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout.addWidget(self.label_10)
        self.label_13 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.verticalLayout.addWidget(self.label_13)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(140, 50, 291, 341))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.month_1_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_1_wage.setObjectName("month_1_wage")
        self.verticalLayout_2.addWidget(self.month_1_wage)
        self.month_2_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_2_wage.setObjectName("month_2_wage")
        self.verticalLayout_2.addWidget(self.month_2_wage)
        self.month_3_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_3_wage.setObjectName("month_3_wage")
        self.verticalLayout_2.addWidget(self.month_3_wage)
        self.month_4_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_4_wage.setObjectName("month_4_wage")
        self.verticalLayout_2.addWidget(self.month_4_wage)
        self.month_5_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_5_wage.setObjectName("month_5_wage")
        self.verticalLayout_2.addWidget(self.month_5_wage)
        self.month_6_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_6_wage.setObjectName("month_6_wage")
        self.verticalLayout_2.addWidget(self.month_6_wage)
        self.month_7_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_7_wage.setObjectName("month_7_wage")
        self.verticalLayout_2.addWidget(self.month_7_wage)
        self.month_8_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_8_wage.setObjectName("month_8_wage")
        self.verticalLayout_2.addWidget(self.month_8_wage)
        self.month_9_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_9_wage.setObjectName("month_9_wage")
        self.verticalLayout_2.addWidget(self.month_9_wage)
        self.month_10_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_10_wage.setObjectName("month_10_wage")
        self.verticalLayout_2.addWidget(self.month_10_wage)
        self.month_11_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_11_wage.setObjectName("month_11_wage")
        self.verticalLayout_2.addWidget(self.month_11_wage)
        self.month_12_wage = QtWidgets.QDoubleSpinBox(self.widget1,maximum=100000000000000000,minimum=0)
        self.month_12_wage.setObjectName("month_12_wage")
        self.verticalLayout_2.addWidget(self.month_12_wage)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Monthly Salary"))
        self.label_4.setText(_translate("Dialog", "Month 1"))
        self.label_3.setText(_translate("Dialog", "Month 2"))
        self.label_2.setText(_translate("Dialog", "Month 3"))
        self.label_6.setText(_translate("Dialog", "Month 4"))
        self.label_5.setText(_translate("Dialog", "Month 5"))
        self.label_11.setText(_translate("Dialog", "Month 6"))
        self.label_7.setText(_translate("Dialog", "Month 7"))
        self.label_8.setText(_translate("Dialog", "Month 8"))
        self.label_12.setText(_translate("Dialog", "Month 9"))
        self.label_9.setText(_translate("Dialog", "Month 10"))
        self.label_10.setText(_translate("Dialog", "Month 11"))
        self.label_13.setText(_translate("Dialog", "Month 12"))