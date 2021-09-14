
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 0, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(230, 250, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 50, 48, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.layoutWidget1 = QtWidgets.QWidget(Dialog)
        self.layoutWidget1.setGeometry(QtCore.QRect(90, 50, 231, 178))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.day_1_usage = QtWidgets.QDoubleSpinBox(self.layoutWidget1,maximum=100000000000000000,minimum=0)
        self.day_1_usage.setObjectName("day_1_usage")
        self.verticalLayout_2.addWidget(self.day_1_usage)
        self.day_2_usage = QtWidgets.QDoubleSpinBox(self.layoutWidget1,maximum=100000000000000000,minimum=0)
        self.day_2_usage.setObjectName("day_2_usage")
        self.verticalLayout_2.addWidget(self.day_2_usage)
        self.day_3_usage = QtWidgets.QDoubleSpinBox(self.layoutWidget1,maximum=100000000000000000,minimum=0)
        self.day_3_usage.setObjectName("day_3_usage")
        self.verticalLayout_2.addWidget(self.day_3_usage)
        self.day_4_usage = QtWidgets.QDoubleSpinBox(self.layoutWidget1,maximum=100000000000000000,minimum=0)
        self.day_4_usage.setObjectName("day_4_usage")
        self.verticalLayout_2.addWidget(self.day_4_usage)
        self.day_5_usage = QtWidgets.QDoubleSpinBox(self.layoutWidget1,maximum=100000000000000000,minimum=0)
        self.day_5_usage.setObjectName("day_5_usage")
        self.verticalLayout_2.addWidget(self.day_5_usage)
        self.day_6_usage = QtWidgets.QDoubleSpinBox(self.layoutWidget1,maximum=100000000000000000,minimum=0)
        self.day_6_usage.setObjectName("day_6_usage")
        self.verticalLayout_2.addWidget(self.day_6_usage)
        self.day_7_usage = QtWidgets.QDoubleSpinBox(self.layoutWidget1,maximum=100000000000000000,minimum=0)
        self.day_7_usage.setObjectName("day_7_usage")
        self.verticalLayout_2.addWidget(self.day_7_usage)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "daily_usage_dialog"))
        self.label.setText(_translate("Dialog", "Daily Money usage"))
        self.label_2.setText(_translate("Dialog", "Day 1"))
        self.label_4.setText(_translate("Dialog", "Day 2"))
        self.label_3.setText(_translate("Dialog", "Day 3"))
        self.label_6.setText(_translate("Dialog", "Day 4"))
        self.label_8.setText(_translate("Dialog", "Day 5"))
        self.label_7.setText(_translate("Dialog", "Day 6"))
        self.label_5.setText(_translate("Dialog", "Day 7"))