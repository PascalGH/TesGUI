from PySide2 import QtWidgets
from PySide2.QtCore import Signal
import signal


import sys

__appname__ = "Ninth Video"

class Program(QtWidgets.QDialog):

    def __init__(self, parent = None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)
        openButton = QtWidgets.QPushButton("Open dialog")
        self.label1 = QtWidgets.QLabel("Label 1 result")
        self.label2 = QtWidgets.QLabel("Label 2 result")

        
 #       openButton.clicked.connect(self.open)
 #       saveButton.clicked.connect(self.save)
 #       closeButton.clicked.connect(self.close)

        


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)

        self.setLayout(layout)

        openButton.clicked.connect(self.dialogOpen)

    def dialogOpen(self):

        dialog = Dialog()
        if dialog.exec_():
            self.label1.setText("Spinbox value is: " + str(dialog.spinBox.value()))
            self.label2.setText("Checkbox is: " + str(dialog.checkBox.isChecked()))
        else:
            QtWidgets.QMessageBox.warning(self, __appname__, "Dialog Cancelled")

#        self.dial.valueChanged.connect(self.spinbox.setValue)
#        self.spinbox.valueChanged.connect(self.dial.setValue)


class Dialog(QtWidgets.QDialog):

    def __init__(self, parent = None):
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

        buttonOK.clicked.connect(self.accept())
        buttonCancel.clicked.connect(self.reject())










app = QtWidgets.QApplication(sys.argv)
form = Program()
form.show()
app.exec_()
