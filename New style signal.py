#!/usr/bin/env python3.7

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import sys


class MainDialog(QDialog):

    myOwnSignal = Signal((int,), (str,))

    def __init__(self, paret=None):
        QDialog.__init__(self)

        self.btn1 = QPushButton("Button!")

        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)

        self.btn1.clicked.connect(self.btn1clicked)

        #self.connect(self, SIGNAL("myOwnSignal()"), self.myOwnSignalEmited)
        self.myOwnSignal.connect(self.myOwnSignalEmited)
        self.myOwnSignal[str].connect(self.myOwnSignalEmited)

    def btn1clicked(self):
        # self.emit(SIGNAL("myOwnSignal()"))
        self.myOwnSignal[str].emit("Hello")

    def myOwnSignalEmited(self, param):
        print("SIGNAL EMMITED! " + str(param))
        print(type(param))


app = QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
