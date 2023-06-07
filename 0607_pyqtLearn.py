# web = https://steam.oxxostudio.tw/category/python/pyqt5/start.html

# from PyQt5 import QtWidgets, QtCore
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

############################### another way to code ###########################################

from PyQt5 import QtWidgets, QtCore
import sys


class MyWidget(QtWidgets.QWidget):  # 用class包住一個qtWidgets
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.setWindowTitle('oxxo.studio')  # 視窗名稱
        self.resize(300, 200)  # 設定視窗大小
        self.ui()

    def ui(self):
        pushButton = QtWidgets.QPushButton(self) #設定一個按鈕
        pushButton.setGeometry(QtCore.QRect(100, 70, 113, 32)) #設定這按鈕的位置(100,70) 大小(113,32)
        pushButton.setObjectName("pushButton") # 按鈕的名稱
        pushButton.setText("PushButton jing") # 按鈕的文字


if __name__ == '__main__': # 設定 main function
    app = QtWidgets.QApplication(sys.argv) # 視窗程式開始
    MainWindow = MyWidget() #  主要的畫面 = 這個 MyWidget class
    MainWindow.show() # 顯示元件
    sys.exit(app.exec_()) # 視窗程式結束 ### 若沒有寫這行的話，視窗不會frozen 在畫面上
