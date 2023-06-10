from PyQt5 import QtWidgets, QtGui, QtCore
from JingMainForm import Ui_MainForm
from JingForm2 import Ui_Form2

# class MainWindows(QtWidgets.QMainWindow):
#     def __init__(self):
#         super(MainWindows, self).__init__()
#         self.ui = Ui_MainForm()
#         self.ui.setupUi(self)
#         self.on_binding_ui()
#         # self.setup_control()

class MainWindow(QtWidgets.QMainWindow, Ui_MainForm):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        # self.ui = Ui_MainForm()
        self.setupUi(self)
        self.on_binding_ui()
        # self.setup_control()
    def on_binding_ui(self):
        self.bottom_openNewForm.clicked.connect(self.showNewWindow)

    def showNewWindow(self):
        self.nw = QtWidgets.QWidget()
        form2 = Ui_Form2
        form2.setupUi(self.nw)
        form2.nw.show()
        x = self.nw.pos().x()
        y = self.nw.pos().y()
        self.nw.move(x+50, y+50)
    # def setup_control(self):

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())