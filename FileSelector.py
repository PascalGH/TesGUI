from PySide2 import QtWidgets
from PySide2.QtCore import Signal
import signal


import sys

__appname__ = "Eight Video"

class Program(QtWidgets.QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QtWidgets.QPushButton("Open")
        saveButton = QtWidgets.QPushButton("Save")
        closeButton = QtWidgets.QPushButton("Close")
        
        openButton.clicked.connect(self.open)
        saveButton.clicked.connect(self.save)
        closeButton.clicked.connect(self.close)
 #       self.dial.valueChanged.connect(self.spinbox.setValue)
        


        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(closeButton)

        self.setLayout(layout)


#        self.dial.valueChanged.connect(self.spinbox.setValue)
#        self.spinbox.valueChanged.connect(self.dial.setValue)


    def open(self):
        dir = "."
        fileObj = QtWidgets.QFileDialog.getOpenFileName(self, __appname__ + " open file dialog", dir = dir, filters = "Text files (.txt)")
        filename = fileObj[0]
        file = open(filename, "r")
        read = file.read()
        file.close()
        print(read)

    def save(self):
        dir = "."
        content = "Hello from Pascal"
        fileObj = QtWidgets.QFileDialog.getOpenFileName(self, __appname__, dir=dir, filters="Text files (.txt)")
        filename = fileObj[0].split(".")[0] + "_." + fileObj[0].split(".")[1]
        print(filename)
        file = open(filename, "w")
        file.write(content)
        file.close()










app = QtWidgets.QApplication(sys.argv)
program = Program()
program.show()
app.exec_()
