from PySide2 import QtWidgets
from PySide2.QtCore import Signal
import signal


import sys

__appname__ = "Tenth Video"

class Program(QtWidgets.QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)
        btn = QtWidgets.QPushButton("Open dialog")
        self.mainSpinBox = QtWidgets.QSpinBox()
        self.mainCheckBox = QtWidgets.QCheckBox("Main Checkbox Value")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        layout.addWidget(btn)


        self.setLayout(layout)

        btn.clicked.connect(self.dialogOpen)

    def dialogOpen(self):

        initValues = {"mainSpinBox" : self.mainSpinBox.value(), "mainCheckBox" : self.mainCheckBox.isChecked()}
        dialog = Dialog(initValues)
        if dialog.exec_():
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())



class Dialog(QtWidgets.QDialog):

    def __init__(self, initValues, parent = None):
        super(Dialog, self).__init__(parent)
        self.setWindowTitle("Dialog")

        self.checkBox = QtWidgets.QCheckBox("Check me out!")
        self.spinBox = QtWidgets.QSpinBox()
        buttonOK = QtWidgets.QPushButton("Ok")
        buttonCancel = QtWidgets.QPushButton("Cancel")

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.spinBox, 0, 0)
        layout.addWidget(self.checkBox, 0, 1)
        layout.addWidget(buttonCancel)
        layout.addWidget(buttonOK)
        self.setLayout(layout)

        self.spinBox.setValue(initValues["mainSpinBox"])
        self.checkBox.setChecked(initValues["mainCheckBox"])

        buttonOK.clicked.connect(self.accept)
        buttonCancel.clicked.connect(self.reject)

    def accept(self):


        class GreaterThanFive(BaseException): pass
        class IsZero(BaseException): pass

        try:
            if self.spinBox.value() > 5:
                raise(GreaterThanFive, "The SpinBox value cannot be greater than 5")
            elif self.spinBox.value() == 0:
                raise(IsZero, "The Spinbox value cannot be equal to 0")
            else:
                QtWidgets.QDialog.accept()

        except(GreaterThanFive) as x:
            QtWidgets.QMessageBox.warning(self, __appname__, str(x))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return

        except(IsZero) as x:
            QtWidgets.QMessageBox.warning(self, __appname__, str(x))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return


app = QtWidgets.QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
