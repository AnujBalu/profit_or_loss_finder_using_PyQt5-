
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(515, 257)
        self.password_text = QtWidgets.QLineEdit(Dialog)
        self.password_text.setGeometry(QtCore.QRect(130, 150, 294, 31))
        self.password_text.setObjectName("password_text")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(130, 100, 291, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.title = QtWidgets.QLabel(Dialog)
        self.title.setGeometry(QtCore.QRect(100, 40, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.layoutWidget_3 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 150, 101, 31))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.password = QtWidgets.QLabel(self.layoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.password.setFont(font)
        self.password.setAlignment(QtCore.Qt.AlignCenter)
        self.password.setObjectName("password")
        self.horizontalLayout_6.addWidget(self.password)
        self.layoutWidget_6 = QtWidgets.QWidget(Dialog)
        self.layoutWidget_6.setGeometry(QtCore.QRect(60, 100, 71, 31))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(self.layoutWidget_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(330, 210, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "edit_account"))
        self.title.setText(_translate("Dialog", "Edit Account"))
        self.password.setText(_translate("Dialog", "PASSWORD"))
        self.label.setText(_translate("Dialog", "Gmail"))
