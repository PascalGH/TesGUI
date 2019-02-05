from PySide2 import QtWidgets
from PySide2.QtCore import Signal


import sys


class MainDialog(QtWidgets.QDialog):

    myOwnSignal = Signal((int,), (str,))

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.btn1 = (QtWidgets.QPushButton("Button!"))

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.btn1)
        self.setLayout(layout)

        self.btn1.clicked.connect(self.btn1clicked)
        self.myOwnSignal[str].connect(self.myOwnSignalEmitted)


    def btn1clicked(self):
        self.myOwnSignal[str].emit("Hello!")


    def myOwnSignalEmitted(self, param):
        print("Signal emitted " + param)
        print(type(param))


app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
