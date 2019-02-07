from PySide2 import QtWidgets
from PySide2.QtCore import Signal
import signal

from ui import showGui

import sys

__appname__ = "Tenth Video"


class MainDialog(QtWidgets.QDialog, showGui.Ui_mainDialog):

    def __init__(self, parent = None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.showButton.clicked.connect(self.showMessageBox)

    def showMessageBox(self):
        QtWidgets.QMessageBox.information(self, "Hello", "Hello there, " + self.nameEdit.text())

app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
