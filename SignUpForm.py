# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUpForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SignUpForm(object):
    def setupUi(self, SignUpForm):
        SignUpForm.setObjectName("SignUpForm")
        SignUpForm.resize(431, 373)
        self.label = QtWidgets.QLabel(SignUpForm)
        self.label.setGeometry(QtCore.QRect(30, 20, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(SignUpForm)
        self.splitter.setGeometry(QtCore.QRect(20, 50, 121, 301))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButton = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton.setFont(font)
        self.pushButton.setMouseTracking(False)
        self.pushButton.setTabletTracking(False)
        self.pushButton.setAcceptDrops(False)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setAutoExclusive(False)
        self.pushButton.setAutoDefault(False)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setTabletTracking(False)
        self.pushButton_2.setAcceptDrops(False)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setAutoExclusive(False)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setTabletTracking(False)
        self.pushButton_3.setAcceptDrops(False)
        self.pushButton_3.setAutoFillBackground(True)
        self.pushButton_3.setAutoExclusive(False)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setTabletTracking(False)
        self.pushButton_4.setAcceptDrops(False)
        self.pushButton_4.setAutoFillBackground(True)
        self.pushButton_4.setAutoExclusive(False)
        self.pushButton_4.setAutoDefault(False)
        self.pushButton_4.setDefault(False)
        self.pushButton_4.setFlat(False)
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(SignUpForm)
        QtCore.QMetaObject.connectSlotsByName(SignUpForm)

    def retranslateUi(self, SignUpForm):
        _translate = QtCore.QCoreApplication.translate
        SignUpForm.setWindowTitle(_translate("SignUpForm", "SignUpForm"))
        self.label.setText(_translate("SignUpForm", "TextLabel"))
        self.pushButton.setText(_translate("SignUpForm", "早上場"))
        self.pushButton_2.setText(_translate("SignUpForm", "下午場"))
        self.pushButton_3.setText(_translate("SignUpForm", "晚上場"))
        self.pushButton_4.setText(_translate("SignUpForm", "宵夜場"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SignUpForm = QtWidgets.QWidget()
    ui = Ui_SignUpForm()
    ui.setupUi(SignUpForm)
    SignUpForm.show()
    sys.exit(app.exec_())
