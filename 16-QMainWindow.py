from PySide2 import QtWidgets

from ui import mainwindow2

import sys


class MainWindow(QtWidgets.QMainWindow, mainwindow2.Ui_MainWindow):

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.actionQuit.triggered.connect(self.exitApp)


    def exitApp(self):
        sys.exit(0)


app = QtWidgets.QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
