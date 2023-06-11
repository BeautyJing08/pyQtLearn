from PyQt5 import QtWidgets, QtGui, QtCore
from VolleyKindomForm import Ui_VolleyKindomForm
from WeekForm import Ui_WeekForm
from SignUpForm import Ui_SignUpForm

import sys
import mysql.connector

def openMydb():
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "5321",
        database = "volleykindom2")
    return  mydb

mydb = openMydb()
cursor = mydb.cursor()
query = "SELECT * FROM weektable " #把所有weekTable的資料讀取出來
cursor.execute(query) #讓游標讀取query語言

dataArray=[]
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
    weekTagArray.append(week_Tag) #把週次 tag 傳進weekTagArray
    dataArray.append(smallarray) #再把當週資料傳進printarray


print(weekTagArray)
print(dataArray[0])
string = dataArray[0][-2]
startDate = string[:2] + string[3:]
print(startDate)
print(dataArray[1])
#
# result = cursor.fetchall()
# for row in result:
#     print(row)

cursor.close()
mydb.close()

# mydb = openMydb()
# cursor3 = mydb.cursor()
# query3 = "SELECT * FROM weektable WHERE weekTag = %s"
# params = (selected_weekTag,)
# cursor3.execute(query3, params)
# result = cursor2.fetchone()
# print(result)


class MainWindow(QtWidgets.QMainWindow, Ui_VolleyKindomForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent) #呼叫父類別 "QtWidgets.QMainWindow" 的建構函式，確保父類別的初始化
        self.setupUi(self) #設置介面的版面配置和控制元件
        self.on_binding_ui() #這是讓功能鍵生效
        # end function


    def on_binding_ui(self): #這個是拿來綁定各個按鈕的功能
        self.Buttom_Im_player.clicked.connect(self.showWeekForm)
        # self.bottom_inForm2_addLabel.clicked.connect(self.form2_addLabel)
        # end function

    def showWeekForm(self):
        self.weekForm = QtWidgets.QWidget()
        ui = Ui_WeekForm()
        ui.setupUi(self.weekForm)
        ui.comboBox_weekBox.clear() #把預設combobox的內容都先給清空
        ui.comboBox_weekBox.addItem("")
        for weekTag in weekTagArray:
            ui.comboBox_weekBox.addItem(weekTag) #把讀到的週次資料給顯示出來 (放進combobox)
        # end function



        def updatePushBottomText(index):
            selected_weekTag = ui.comboBox_weekBox.itemText(index)
            if selected_weekTag == "":
                print("這沒有資料")
            else:
                print(selected_weekTag) #這是嘗試印出combox item有變動時的內容資料 #也成功惹

                mydb = openMydb() #重啟資料庫
                cursor2 = mydb.cursor()
                query2 = "SELECT * FROM weektable WHERE weekTag = %s"
                params = (selected_weekTag,)
                cursor2.execute(query2, params)
                result = cursor2.fetchone()
                print(result)
                print(result[1])
                print(type(result[1]))
                print(result[1].strftime('%m%d'))

                cursor2.close() #使用完要關閉游標
                mydb.close() #使用完要關閉資料庫
                ### 現在要去修改pushBottom的text
                ui.pushButton.setText(str(result[1].strftime('%m%d')))
                ui.pushButton_2.setText(str(result[2].strftime('%m%d')))
                ui.pushButton_3.setText(str(result[3].strftime('%m%d')))
                ui.pushButton_4.setText(str(result[4].strftime('%m%d')))
                ui.pushButton_5.setText(str(result[5].strftime('%m%d')))
                ui.pushButton_6.setText(str(result[6].strftime('%m%d')))
                ui.pushButton_7.setText(str(result[7].strftime('%m%d')))

        ui.comboBox_weekBox.currentIndexChanged.connect(updatePushBottomText)
        self.weekForm.show()
        # end function




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    window = MainWindow() #把MainWindows()類別用一個變數 windows裝起來
    window.show() #顯示MainWindows()視窗
    sys.exit(app.exec_()) #沒寫這行的話，視窗不會懸浮，會出現後馬上消失


