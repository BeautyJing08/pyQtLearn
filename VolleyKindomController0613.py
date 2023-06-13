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

# 首先來開啟資料庫 ###################################################
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

cursor.close()
mydb.close()


class MainWindow(QtWidgets.QMainWindow, Ui_VolleyKindomForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent) #呼叫父類別 "QtWidgets.QMainWindow" 的建構函式，確保父類別的初始化
        self.setupUi(self) #設置介面的版面配置和控制元件
        self.on_binding_ui() #這是讓功能鍵生效
        # self.n = 0 #若要記錄某個按鍵的點擊次數，那要建立在Main的__init__內，成為全域變數
        # end function


    def on_binding_ui(self): #這個是拿來綁定各個按鈕的功能
        self.Buttom_Im_player.clicked.connect(self.showWeekForm)

        # self.bottom_inForm2_addLabel.clicked.connect(self.form2_addLabel)
        # end function

    #顯示 WeekForm
    def showWeekForm(self):
        self.weekForm = QtWidgets.QWidget()
        self.WeekForm_ui = Ui_WeekForm()
        self.WeekForm_ui.setupUi(self.weekForm)
        self.WeekForm_ui.comboBox_weekBox.clear() #把預設combobox的內容都先給清空
        self.WeekForm_ui.comboBox_weekBox.addItem("")
        for weekTag in weekTagArray:
            self.WeekForm_ui.comboBox_weekBox.addItem(weekTag) #把讀到的週次資料給顯示出來 (放進combobox)
        #先讓預設的pushBottom都清空
        self.WeekForm_ui.pushButton.setText(""),self.WeekForm_ui.pushButton_2.setText(""), self.WeekForm_ui.pushButton_3.setText(""),self.WeekForm_ui.pushButton_4.setText(""), self.WeekForm_ui.pushButton_5.setText(""), self.WeekForm_ui.pushButton_6.setText(""),self.WeekForm_ui.pushButton_7.setText("")
        #先讓預設的pushBottom為禁用
        def FalusAllpushBottom():
            self.WeekForm_ui.pushButton.setEnabled(False), self.WeekForm_ui.pushButton_2.setEnabled(False), self.WeekForm_ui.pushButton_3.setEnabled(
                False), self.WeekForm_ui.pushButton_4.setEnabled(False), self.WeekForm_ui.pushButton_5.setEnabled(False),self.WeekForm_ui.pushButton_6.setEnabled(False),self.WeekForm_ui.pushButton_7.setEnabled(False)
        FalusAllpushBottom() #禁用所有pushBottom

        def TrueAllpushBottom():
            self.WeekForm_ui.pushButton.setEnabled(True), self.WeekForm_ui.pushButton_2.setEnabled(True), self.WeekForm_ui.pushButton_3.setEnabled(
                True), self.WeekForm_ui.pushButton_4.setEnabled(True), self.WeekForm_ui.pushButton_5.setEnabled(
                True), self.WeekForm_ui.pushButton_6.setEnabled(True), self.WeekForm_ui.pushButton_7.setEnabled(True)
        # end function

        def updatePushBottomText(index):
            selected_weekTag = self.WeekForm_ui.comboBox_weekBox.itemText(index)
            if selected_weekTag == "": #若選到的weekTag 是字串"" 空值
                print("這沒有資料")
                FalusAllpushBottom() #就把所有按鈕封鎖
                self.WeekForm_ui.pushButton.setText(""),self.WeekForm_ui.pushButton_2.setText("") ,self.WeekForm_ui.pushButton_3.setText(""),self.WeekForm_ui.pushButton_4.setText(""),self.WeekForm_ui.pushButton_5.setText("") ,self.WeekForm_ui.pushButton_6.setText(""),self.WeekForm_ui.pushButton_7.setText("")
            else:#若選到的weekTag不是空值
                print(selected_weekTag) #這是嘗試印出combox item有變動時的內容資料 #也成功惹
                TrueAllpushBottom() #打開所有按鈕
                mydb = openMydb() #重啟資料庫
                cursor2 = mydb.cursor()
                query2 = "SELECT * FROM weektable WHERE weekTag = %s"
                params = (selected_weekTag,)
                cursor2.execute(query2, params)
                result = cursor2.fetchone()
                # print(result)
                # print(result[1])
                # print(type(result[1]))
                # print(result[1].strftime('%m%d'))

                cursor2.close() #使用完要關閉游標
                mydb.close() #使用完要關閉資料庫
                ### 現在要去修改pushBottom的text
                self.WeekForm_ui.pushButton.setText(str(result[1].strftime('%m%d')))
                self.WeekForm_ui.pushButton_2.setText(str(result[2].strftime('%m%d')))
                self.WeekForm_ui.pushButton_3.setText(str(result[3].strftime('%m%d')))
                self.WeekForm_ui.pushButton_4.setText(str(result[4].strftime('%m%d')))
                self.WeekForm_ui.pushButton_5.setText(str(result[5].strftime('%m%d')))
                self.WeekForm_ui.pushButton_6.setText(str(result[6].strftime('%m%d')))
                self.WeekForm_ui.pushButton_7.setText(str(result[7].strftime('%m%d')))
        #### end updatePushBottomText function

        self.WeekForm_ui.comboBox_weekBox.currentIndexChanged.connect(updatePushBottomText) #當combobox有調整時，就連動到修改文字的function

        self.WeekForm_ui.pushButton.clicked.connect(lambda :self.showSignUpForm(self.WeekForm_ui.pushButton.text()))
        self.WeekForm_ui.pushButton_2.clicked.connect(lambda :self.showSignUpForm(self.WeekForm_ui.pushButton_2.text()))
        self.WeekForm_ui.pushButton_3.clicked.connect(lambda :self.showSignUpForm(self.WeekForm_ui.pushButton_3.text()))
        self.WeekForm_ui.pushButton_4.clicked.connect(lambda :self.showSignUpForm(self.WeekForm_ui.pushButton_4.text()))
        self.WeekForm_ui.pushButton_5.clicked.connect(lambda :self.showSignUpForm(self.WeekForm_ui.pushButton_5.text()))
        self.WeekForm_ui.pushButton_6.clicked.connect(lambda :self.showSignUpForm(self.WeekForm_ui.pushButton_6.text()))
        self.WeekForm_ui.pushButton_7.clicked.connect(lambda :self.showSignUpForm(self.WeekForm_ui.pushButton_7.text()))
        self.weekForm.show()
        # end function


    def showSignUpForm(self, bottom_text):
        print("showSignForm")
        print(bottom_text)
        self.SignUpForm = QtWidgets.QWidget()
        self.SignUpFormUi = Ui_SignUpForm()
        self.SignUpFormUi.setupUi(self.SignUpForm)
        self.SignUpFormUi.label.setText(bottom_text)
        self.SignUpForm.show()
        self.SignUpFormUi.pushButton.clicked.connect(lambda: self.showOrderData(bottom_text)) #lambda貌似是個虛擬函數??可以幫忙傳到下一個function內


    def showOrderData(self,bottom_text):
        # self.n += 1
        print(f"hiJing, it's bottom check")
        print(bottom_text)
        print(type(bottom_text))
        newDate = f"2023-{bottom_text[:2]}-{bottom_text[2:]}"
        print(newDate)
        self.mysql_FindOrderTable(newDate)
        # mydb = openMydb()
        # cursor3 = mydb.cursor()
        # query3 = f"SELECT * FROM volleykindom2.ordertable WHERE date = '{newDate}'"
        # cursor3.execute(query3)
        # result = cursor3.fetchone()
        # print(result)
        # cursor3.close()
        # mydb.close()
        # self.SignUpFormUi.label_date_change.set
    def mysql_FindOrderTable(self, newDate):
        mydb =openMydb()
        cursor3 = mydb.cursor()
        query3 = f"SELECT * FROM volleykindom2.ordertable WHERE date = '{newDate}'"
        cursor3.execute(query3)
        result = cursor3.fetchone()
        print(result)
        cursor3.close()
        mydb.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    window = MainWindow() #把MainWindows()類別用一個變數 windows裝起來
    window.show() #顯示MainWindows()視窗
    sys.exit(app.exec_()) #沒寫這行的話，視窗不會懸浮，會出現後馬上消失


