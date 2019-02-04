from PySide2 import QtWidgets
from PySide2.QtCore import Signal
import signal


import sys


class ZeroSpinBox(QtWidgets.QSpinBox):

    zeros = 0
    atZero = Signal(int)

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.valueChanged.connect(self.check_zero)


    def check_zero(self, value):
        if value == 0:
            self.zeros += 1
            self.constant = 5
            self.atZero.emit(self.zeros)


class Form(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)


        self.dial = QtWidgets.QDial()
        self.dial.setNotchesVisible(True)

        self.spinbox = ZeroSpinBox()

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.dial)
        layout.addWidget(self.spinbox)
        self.setLayout(layout)


        self.dial.valueChanged.connect(self.spinbox.setValue)
        self.spinbox.valueChanged.connect(self.dial.setValue)

        self.spinbox.atZero.connect(self.printvalue)


    def printvalue(self, zeros):
        print("Caught the signal!")
        print(zeros)









app = QtWidgets.QApplication(sys.argv)
form = Form()
form.show()
app.exec_()
