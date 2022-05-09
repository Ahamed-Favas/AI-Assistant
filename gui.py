from numpy import uint
from voice import Ui_MainWindow
from PyQt5 import QtCore , QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, QTimer, QTime,QDate
from PyQt5.uic import loadUiType
import sys
import os 
import time

import main


class MainThread(QThread):

    def __init__(self):

        super(MainThread,self).__init__()
 
    def run(self):
        main.Task_Gui()

startExe = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()

        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)

        self.gui.pushButton.clicked.connect(self.startTask)
        self.gui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        startExe.start()

        self.gui.label=QtGui.QMovie("Assets/bubble.gif")
        self.gui.bg_2.setMovie(self.gui.label)
        time.sleep(6)
        self.gui.label.start()

        



GuiApp = QApplication(sys.argv)
ui = Gui_Start()
ui.show()
sys.exit(GuiApp.exec_())