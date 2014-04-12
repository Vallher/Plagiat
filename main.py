# -*- coding: utf-8 -*-
#pyuic form1.ui > form1.py
from os import path
from Tkinter import Tk
from tkFileDialog import askopenfilename
import sys
from PyQt4 import QtCore, QtGui

sys.path.append(path.abspath('./Class'))
from Source import Source

from gui import Ui_MainWindow

class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # nazwa klasy
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.source=Source()
        QtCore.QObject.connect(self.ui.Button_LoadMainFile,QtCore.SIGNAL("clicked()"), self.LoadMainFile_Button)
        QtCore.QObject.connect(self.ui.Button_Next1,QtCore.SIGNAL("clicked()"), self.Next1_Button)
        
    def LoadMainFile_Button(self):
        text=self.source.SearchFile()
        self.ui.Line_LoadMainFile.setText(text)
        
    def Next1_Button(self):
        self.ui.Button_LoadMainFile.setEnabled(False)
        self.ui.Line_LoadMainFile.setEnabled(False)
        self.ui.Button_Next1.setEnabled(False)
        self.ui.listView.setEnabled(True)
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        self.ui.pushButton_5.setEnabled(True)
        


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    app.setActiveWindow(MainWindow)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
