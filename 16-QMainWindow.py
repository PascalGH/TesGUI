from PySide2 import QtWidgets
from PySide2.QtCore import Signal
import signal

from ui import justmain

import sys

__appname__ = "Tenth Video"


class MainWindow(QtWidgets.QMainWindow, justmain.Ui_MainWindow):

    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.actionQuit.triggered.connect(self.exitApp)


    def exitApp(self):
        sys.exit(0)




    def showMessageBox(self):
        QtWidgets.QMessageBox.information(self, "Hello", "Hello there, " + self.nameEdit.text())

app = QtWidgets.QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
