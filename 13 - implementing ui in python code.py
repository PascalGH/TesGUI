from threading import Thread
from PySide2 import QtWidgets
from PySide2.QtCore import QThread
from PySide2.QtCore import Signal
from ui import showGui
import time
import sys


class MainDialog(QtWidgets.QDialog, showGui.Ui_mainDialog):

    def __init__(self, parent = None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.showButton.setText("Process")
        self.showButton.clicked.connect(self.process_data)

        self.workerThread = WorkerThread()
        self.workerThread.completed.connect(self.thread_done)

    def process_data(self):
        print("Launching thread")
        self.workerThread.start()
        QtWidgets.QMessageBox.information(self, "Done!", "Done")
        self.workerThread.wait()

    def thread_done(self):
        QtWidgets.QMessageBox.warning(self, "Warning!", "Thread execution completed")


class WorkerThread(QThread):

    completed = Signal(str)

    def __init__(self, parent = None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        time.sleep(5)
        print("Thread started")
        self.completed.emit("Thread Completed")


app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()
