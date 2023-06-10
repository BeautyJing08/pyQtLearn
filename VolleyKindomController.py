from PyQt5 import QtWidgets, QtGui, QtCore
from VolleyKindomForm import Ui_VolleyKindomForm
from WeekForm import Ui_WeekForm
from SignUpForm import Ui_SignUpForm

import sys
import pymysql.connections


mydb = pymysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "53215321",
    database = "sql_tutorial")

cursor = mydb.cursor()
cursor.execute("SELECT * FROM member_tatble ")

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
mydb.close()




class MainWindow(QtWidgets.QMainWindow, Ui_VolleyKindomForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent) #呼叫父類別 "QtWidgets.QMainWindow" 的建構函式，確保父類別的初始化
        self.setupUi(self) #設置介面的版面配置和控制元件
        self.on_binding_ui() #這是讓功能鍵生效


    def on_binding_ui(self): #這個是拿來綁定各個按鈕的功能
        self.Buttom_Im_player.clicked.connect(self.showWeekForm)
        # self.bottom_inForm2_addLabel.clicked.connect(self.form2_addLabel)

    def showWeekForm(self):
        self.weekForm = QtWidgets.QWidget()
        ui = Ui_WeekForm()
        ui.setupUi(self.weekForm)






        self.weekForm.show()


    # def showNewWindow(self): #這是開啟新視窗的功能
    #         self.form2 = QtWidgets.QWidget() # 這行程式碼創建了一個名為 form2 的新視窗，使用的是 QtWidgets.QWidget 類別。
    #         ui = Ui_Form2()
    #         ui.setupUi(self.form2)
    #         self.form2.show()
    #         self.hide() #這個程式碼的意思是，當我開啟form2視窗時，mainForm會被隱藏
    #
    # def form2_addLabel(self):
    #     # self.form2 = Ui_Form2()
    #     self.form2.ui.From2_label.setText('點擊按鈕囉')



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    window = MainWindow() #把MainWindows()類別用一個變數 windows裝起來
    window.show() #顯示MainWindows()視窗
    sys.exit(app.exec_()) #沒寫這行的話，視窗不會懸浮，會出現後馬上消失


