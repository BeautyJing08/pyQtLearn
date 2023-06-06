# web = https://ithelp.ithome.com.tw/articles/10289589?sc=iThelpR
#
# from PyQt5 import QtCore, QtWidgets
# import sys
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
# MainWindow.setObjectName("MainWindow")
# MainWindow.setWindowTitle("oxxo.studio")
# MainWindow.resize(300, 200)
#
# pushButton = QtWidgets.QPushButton(MainWindow)
# pushButton.setGeometry(QtCore.QRect(100, 70, 113, 32))
# pushButton.setObjectName("pushButton")
# pushButton.setText("PushButton")
#
# MainWindow.show()
# sys.exit(app.exec_())

# ===============================================================================
# web = https://ithelp.ithome.com.tw/articles/10289916
# from PyQt5 import QtCore, QtGui, QtWidgets
#
# class Ui_Form(object):
#     def setupUi(self, Form):
#         Form.setObjectName("Form")
#         Form.resize(320, 240)
#         self.pushButton = QtWidgets.QPushButton(Form)
#         self.pushButton.setGeometry(QtCore.QRect(100, 130, 113, 32))
#         self.pushButton.setObjectName("pushButton")
#         self.label = QtWidgets.QLabel(Form)
#         self.label.setGeometry(QtCore.QRect(70, 70, 171, 51))
#         font = QtGui.QFont()
#         font.setPointSize(20)
#         self.label.setFont(font)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setObjectName("label")
#
#         self.retranslateUi(Form)
#         QtCore.QMetaObject.connectSlotsByName(Form)
#
#     def retranslateUi(self, Form):
#         _translate = QtCore.QCoreApplication.translate
#         Form.setWindowTitle(_translate("Form", "Form"))
#         self.pushButton.setText(_translate("Form", "PushButton"))
#         self.label.setText(_translate("Form", "TextLabel"))
#
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv) #視窗程式開始
#     Form = QtWidgets.QWidget() #放入基底元件
#     ui = Ui_Form()
#     ui.setupUi(Form)
#     Form.show() # 顯示視窗
#     sys.exit(app.exec_()) # 視窗程式結束
#
# ===============================================================================
# # web = https://ithelp.ithome.com.tw/articles/10290346
# from PyQt5 import QtWidgets
# import sys
#
# app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
#
# Form = QtWidgets.QWidget()  # 放入基底元件
# Form.show()  # 顯示元件
#
# sys.exit(app.exec_())  # 視窗程式結束

# ===============================================================================
# # web = https://ithelp.ithome.com.tw/articles/10290346
# from PyQt5 import QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore
# import sys
# app = QtWidgets.QApplication(sys.argv) # 視窗程式開始
#
# Form = QtWidgets.QWidget() # 放入基底元件
# Form.setWindowTitle('Hi, beautyJing form')      # 設定標題
# Form.resize(320, 240)                   # 設定長寬尺寸
# Form.setStyleSheet('background:#fcc;')  # 使用網頁 CSS 樣式設定背景 #可以自己設定顏色
#
# print(Form.width())                     # 印出寬度
# print(Form.height())                    # 印出高度
#
# label = QtWidgets.QLabel(Form)     # 在 Form 裡加入 label
# label.move(50,50)                  # 移動到 (50, 50) 的位置
# label.setText('hello Jing')       # 寫入文字
# label.setStyleSheet('font-size:30px; color:#00c')  # 設定樣式
#
# font = QtGui.QFont()
# font.setFamily('Verdana')                  # 設定字體
# font.setPointSize(20)                   # 設定字體大小
# font.setBold(True)                         # 粗體
# font.setItalic(True)                       # 斜體
# # font.setStrikeOut(True)                    # 刪除線
# # font.setUnderline(True)                    # 底線
#
# label.setFont(font)             #### # 設定完字體之後一定要寫入這行程式碼，字形才會調整 ####
#
#
# Form.show() # 顯示元件
# sys.exit(app.exec_()) # 視窗程式結束

# ===============================================================================
# web = https://ithelp.ithome.com.tw/articles/10291555
# bottom tutorial

from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)           # 視窗程式開始

Form = QtWidgets.QWidget()                  # 放入基底元件
Form.setWindowTitle('Jing. Bottom')     # 設定form的視窗大小
Form.resize(300, 200)                   # 視窗大小

btn1 = QtWidgets.QPushButton(Form)   # 在 Form 中加入一個 QPushButton
btn1.setText('我是按鈕1')               # 按鈕文字
btn1.move(50,30)                 # 移動到 (50,30)
# btn1.setGeometry(200,60,80,40)      # 移動到 (200,60)，大小 80x40

btn2 = QtWidgets.QPushButton(Form)
btn2.setText('按鈕 2')
btn2.setGeometry(50,60,100,50)   # 移動到 (50,60)，大小 100x50
btn2.setStyleSheet('''
    background:#ff0;
    color:#f00;
    font-size:20px;
    border:2px solid #000;
''')


Form.show()                          # 顯示元件
sys.exit(app.exec_())                   # 視窗程式結束 #### 沒寫這行的話，視窗不會懸浮，會出現後馬上消失
