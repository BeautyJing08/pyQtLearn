from PyQt5 import QtWidgets, QtGui, QtCore
from JingMainForm import Ui_MainForm
from JingForm2 import Ui_Form2

class MainWindows(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindows, self).__init__()
        self.ui = Ui_MainForm()
        self.ui.setupUi(self)
        # self.setup_control()

    # def setup_control(self):

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())