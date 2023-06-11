from PyQt5 import QtWidgets, QtGui, QtCore
from VolleyKindomForm import Ui_VolleyKindomForm
from WeekForm import Ui_WeekForm
from SignUpForm import Ui_SignUpForm

import sys
import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "5321",
    database = "volleykindom2")

cursor = mydb.cursor()
query = "SELECT * FROM weektable " #把所有weekTable的資料讀取出來
cursor.execute(query) #讓游標讀取query語言

printarray=[]
weekTagArray = []
for row in cursor:
    week_num = row[0]
    week_MON = row[1].strftime('%y-%m-%d')
    week_SUN = row[-2].strftime('%y-%m-%d')
    week_Tag = row[-1]
    # printarray = []
    smallarray=[] #小Array來裝當週的資料
    smallarray.append(week_num)
    smallarray.append(week_MON)
    smallarray.append(week_SUN)

    smallarray.append(row[1].strftime('%m-%d'))
    smallarray.append(row[-2].strftime('%m-%d'))
    smallarray.append(week_Tag)
    weekTagArray.append(week_Tag)
    printarray.append(smallarray) #再把當週資料傳進printarray

    # print(week_num,week_MON, week_SUN)
    # print(printarray)

# weekTagArray = []
# for row in printarray:
#     string01 = row[-2]
#     startDate = string01[:2] + string01[3:]
#     string02 = row[-1]
#     endDate = string02[:2] + string02[3:]
#     weekTag = startDate + "-" + endDate
#     weekTagArray.append(weekTag)
#     # print(weekTag)
#
# print(weekTagArray)




print(weekTagArray)
print(printarray[0])
string = printarray[0][-2]
startDate = string[:2] + string[3:]
print(startDate)
print(printarray[1])
#
# result = cursor.fetchall()
# for row in result:
#     print(row)

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
        ui.comboBox_weekBox.clear() #把預設combobox的內容都先給清空
        for weekTag in weekTagArray:
            ui.comboBox_weekBox.addItem(weekTag) #把讀到的週次資料給顯示出來
        # ui.comboBox_weekBox.addItem(printarray[0][-2])
        # ui.comboBox_weekBox.removeItem(2)

        # def updatePushBottomText(index):
        #     selected_weekTag = ui.comboBox_weekBox.itemText(index)
        #     ui.pushButton.setText(selected_weekTag)
        #
        #
        # ui.comboBox_weekBox.currentIndexChanged.connect(updatePushBottomText())

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


