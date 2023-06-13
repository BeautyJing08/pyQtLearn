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
        self.bottom_text= ""
        self.order_id = ""
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
        try:
            print("showSignForm")
            print(bottom_text)
            self.bottom_text =bottom_text
            self.SignUpForm = QtWidgets.QWidget()
            self.SignUpFormUi = Ui_SignUpForm()
            self.SignUpFormUi.setupUi(self.SignUpForm)
            self.SignUpFormUi.label.setText(bottom_text)

            self.SignUpFormUi.pushButton.clicked.connect(lambda: self.showOrderData(self.bottom_text)) #lambda貌似是個虛擬函數??可以幫忙傳到下一個function內
            self.SignUpFormUi.pushButton_SignIn.clicked.connect(lambda : self.insertTOsignInTable(self.order_id)) #連結報名的按鈕
            self.SignUpForm.show()
        except Exception as e:
            print("showSignUPfrom an error occurred: " ,str(e))

    def insertTOsignInTable(self,order_id):
        try:

            # print("成功!!!")
            name = self.SignUpFormUi.lineEdit_SignInName.text()
            if self.SignUpFormUi.radioButton_boy.isChecked():
                sex = 1
            elif self.SignUpFormUi.radioButton_girl.isChecked():
                sex = 0
            phone = self.SignUpFormUi.lineEdit_phoneNum.text()

            mydb = openMydb()
            cursor6 = mydb.cursor()

            query6 = "INSERT INTO `volleykindom2`.`signintable`(`FK_order_id`,`user_name`, `user_sex`, `user_phoneNum`) VALUES (%s,%s,%s,%s) "
            value = (order_id,name,sex,phone)
            cursor6.execute(query6,value)

            mydb.commit()
            cursor6.close()
            mydb.close()
            print("完成報名了喔喔喔喔喔?")
            self.showOrderData(self.bottom_text) #會更新依次資料表
            self.SignUpFormUi.label_bookIsSuccess.setStyleSheet("color=red")
            self.SignUpFormUi.label_bookIsSuccess.setVisible(True) #把報名成功顯示出來
        except Exception as e:
            print("insertTOsignInTable a error occurred: ", str(e))

    def showOrderData(self,bottom_text):
        try:
            self.bottom_text =bottom_text
            # self.n += 1
            print(f"hiJing, it's bottom check")
            print(bottom_text)
            print(type(bottom_text))
            newDate = f"2023-{bottom_text[:2]}-{bottom_text[2:]}"
            print(newDate)
            findOrderResult = self.mysql_FindOrderTable(newDate) #去找到OrderTable內的資料
            self.order_id= findOrderResult[0][0]
            self.SignUpFormUi.label_date_change.setText(findOrderResult[0][2].strftime('%y-%m-%d')) #設定報名時間
            self.SignUpFormUi.label_date_change.setVisible(True)
            self.SignUpFormUi.label_height_change.setText(findOrderResult[0][4]) #設定網高
            self.SignUpFormUi.label_height_change.setVisible(True)
            self.SignUpFormUi.label_openNum_change.setText(str(findOrderResult[0][5])) #設定總人數
            self.SignUpFormUi.label_openNum_change.setVisible(True)
            self.SignUpFormUi.label_AlreadyBookNumChange.setText(str(findOrderResult[0][6])) #設定已報名人數
            self.SignUpFormUi.label_AlreadyBookNumChange.setVisible(True)
            self.SignUpFormUi.label_fee_change.setText(str(findOrderResult[0][7]))
            self.SignUpFormUi.label_fee_change.setVisible(True)
            sessionResult = self.mysql_FindSession(findOrderResult[0][3]) #讀取sessionTable
            self.SignUpFormUi.label_session_change.setText(sessionResult[0][2]) #場次說明
            self.SignUpFormUi.label_session_change.setVisible(True)
            self.SignUpFormUi.label_session_time_change.setText(sessionResult[0][3]+"-"+sessionResult[0][4]) #場次時間
            self.SignUpFormUi.label_session_time_change.setVisible(True)
            findAlreadySignNumResult = self.mysql_FindalreadySignNum(findOrderResult[0][0])
            self.SignUpFormUi.label_AlreadyBookNumChange.setText(str(findAlreadySignNumResult[2]))
            self.SignUpFormUi.label_alreadyBookNum_women_change.setText(str(findAlreadySignNumResult[0]))
            self.SignUpFormUi.label_alreadyBookNum_women_change.setVisible(True)
            self.SignUpFormUi.label_alreadyBookNum_man_change.setText(str(findAlreadySignNumResult[1]))
            self.SignUpFormUi.label_alreadyBookNum_man_change.setVisible(True)

            # self.SignUpFormUi.pushButton_SignIn.clicked.connect(lambda : self.insertTOsignInTable(findOrderResult[0][0]))
        except Exception as e:
            print("showOrderData a error occurred: ", str(e))

    def mysql_FindOrderTable(self, newDate):
        try:
            mydb =openMydb()
            cursor3 = mydb.cursor()
            query3 = f"SELECT * FROM volleykindom2.ordertable WHERE date = '{newDate}'"
            cursor3.execute(query3)
            result =cursor3.fetchall() #為甚麼這邊要用fetchall()不會跳出問題， i do not know why
            # result = cursor3.fetchone()
            print(result)
            cursor3.close()
            mydb.close()
            return result
        except Exception as e:
            print("mysql_FindOrderTable a error occurred: ", str(e))
            # return result
    def mysql_FindSession(self, session):
        try:
            mydb = openMydb()
            cursor4 = mydb.cursor()
            query4 = f"SELECT * FROM volleykindom2.sessiontable WHERE session = '{session}'"
            cursor4.execute(query4)
            result = cursor4.fetchall()
            print(result)
            cursor4.close()
            mydb.close()
            return result
        except Exception as e:
            print("mysql_FindSession a error occurred: ", str(e))
    def mysql_FindalreadySignNum(self,order_id): #這個是到signIntable內找到某個場次已報名人數
        try:
            mydb = openMydb()
            cursor5 = mydb.cursor()
            query5 = f"SELECT SUM(CASE WHEN user_sex = 0 THEN 1 ELSE 0 END) AS femaleCount, SUM(CASE WHEN user_sex = 1 THEN 1 ELSE 0 END) AS maleCount, COUNT(*) AS totalCount FROM volleykindom2.signIntable WHERE FK_order_id = {order_id};"
            cursor5.execute(query5)
            result = cursor5.fetchone()
            print(result)
            cursor5.close()
            mydb.close()
            return result
        except Exception as e:
            print("mysql_FindalreadySignNum a error occurred: ", str(e))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)  # 視窗程式開始
    window = MainWindow() #把MainWindows()類別用一個變數 windows裝起來
    window.show() #顯示MainWindows()視窗
    sys.exit(app.exec_()) #沒寫這行的話，視窗不會懸浮，會出現後馬上消失


