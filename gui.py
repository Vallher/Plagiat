# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Apr 22 21:54:05 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

QtCore.QTextCodec.setCodecForCStrings(QtCore.QTextCodec.codecForName("UTF-8"))

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(858, 599)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.stackedWidget = QtGui.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, -20, 751, 541))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.Loading = QtGui.QWidget()
        self.Loading.setObjectName(_fromUtf8("Loading"))
        self.label_3 = QtGui.QLabel(self.Loading)
        self.label_3.setGeometry(QtCore.QRect(80, 50, 791, 451))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("Image/main.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar_StartProgram = QtGui.QProgressBar(self.Loading)
        self.progressBar_StartProgram.setGeometry(QtCore.QRect(150, 440, 451, 23))
        self.progressBar_StartProgram.setAutoFillBackground(False)
        self.progressBar_StartProgram.setProperty("value", 0)
        self.progressBar_StartProgram.setTextVisible(False)
        self.progressBar_StartProgram.setObjectName(_fromUtf8("progressBar_StartProgram"))
        self.testButton = QtGui.QPushButton(self.Loading)
        self.testButton.setGeometry(QtCore.QRect(240, 10, 131, 23))
        self.testButton.setObjectName(_fromUtf8("testButton"))
        self.stackedWidget.addWidget(self.Loading)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(190, 90, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.Button_LoadMainFile = QtGui.QPushButton(self.page)
        self.Button_LoadMainFile.setEnabled(True)
        self.Button_LoadMainFile.setGeometry(QtCore.QRect(40, 170, 101, 31))
        self.Button_LoadMainFile.setObjectName(_fromUtf8("Button_LoadMainFile"))
        self.Line_LoadMainFile_Path = QtGui.QLineEdit(self.page)
        self.Line_LoadMainFile_Path.setEnabled(True)
        self.Line_LoadMainFile_Path.setGeometry(QtCore.QRect(200, 200, 341, 31))
        self.Line_LoadMainFile_Path.setReadOnly(True)
        self.Line_LoadMainFile_Path.setObjectName(_fromUtf8("Line_LoadMainFile_Path"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(200, 340, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.Button_Next1 = QtGui.QPushButton(self.page)
        self.Button_Next1.setGeometry(QtCore.QRect(580, 160, 101, 41))
        self.Button_Next1.setObjectName(_fromUtf8("Button_Next1"))
        self.Button_LoadConfig = QtGui.QPushButton(self.page)
        self.Button_LoadConfig.setEnabled(True)
        self.Button_LoadConfig.setGeometry(QtCore.QRect(40, 390, 101, 31))
        self.Button_LoadConfig.setObjectName(_fromUtf8("Button_LoadConfig"))
        self.Line_LoadMainFile_Config = QtGui.QLineEdit(self.page)
        self.Line_LoadMainFile_Config.setEnabled(True)
        self.Line_LoadMainFile_Config.setGeometry(QtCore.QRect(200, 390, 341, 31))
        self.Line_LoadMainFile_Config.setReadOnly(True)
        self.Line_LoadMainFile_Config.setObjectName(_fromUtf8("Line_LoadMainFile_Config"))
        self.Button_Next2 = QtGui.QPushButton(self.page)
        self.Button_Next2.setGeometry(QtCore.QRect(590, 390, 101, 41))
        self.Button_Next2.setObjectName(_fromUtf8("Button_Next2"))
        self.lineEdit_LoadMainFile_Name = QtGui.QLineEdit(self.page)
        self.lineEdit_LoadMainFile_Name.setGeometry(QtCore.QRect(210, 150, 331, 21))
        self.lineEdit_LoadMainFile_Name.setObjectName(_fromUtf8("lineEdit_LoadMainFile_Name"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.Button_LoadOutFileCandidate = QtGui.QPushButton(self.page_2)
        self.Button_LoadOutFileCandidate.setGeometry(QtCore.QRect(90, 180, 101, 61))
        self.Button_LoadOutFileCandidate.setObjectName(_fromUtf8("Button_LoadOutFileCandidate"))
        self.Label_LoadConfig = QtGui.QLabel(self.page_2)
        self.Label_LoadConfig.setGeometry(QtCore.QRect(30, 20, 111, 41))
        self.Label_LoadConfig.setObjectName(_fromUtf8("Label_LoadConfig"))
        self.testText = QtGui.QLineEdit(self.page_2)
        self.testText.setGeometry(QtCore.QRect(-20, 290, 711, 211))
        self.testText.setObjectName(_fromUtf8("testText"))
        self.Line_LoadOutFile_Path = QtGui.QLineEdit(self.page_2)
        self.Line_LoadOutFile_Path.setEnabled(True)
        self.Line_LoadOutFile_Path.setGeometry(QtCore.QRect(60, 130, 341, 31))
        self.Line_LoadOutFile_Path.setReadOnly(True)
        self.Line_LoadOutFile_Path.setObjectName(_fromUtf8("Line_LoadOutFile_Path"))
        self.Button_AddOutFromCandidate = QtGui.QPushButton(self.page_2)
        self.Button_AddOutFromCandidate.setGeometry(QtCore.QRect(330, 190, 91, 23))
        self.Button_AddOutFromCandidate.setObjectName(_fromUtf8("Button_AddOutFromCandidate"))
        self.listWidget_CandidateOutFiles = QtGui.QListWidget(self.page_2)
        self.listWidget_CandidateOutFiles.setGeometry(QtCore.QRect(80, 250, 256, 192))
        self.listWidget_CandidateOutFiles.setObjectName(_fromUtf8("listWidget_CandidateOutFiles"))
        self.listWidget_OutFiles = QtGui.QListWidget(self.page_2)
        self.listWidget_OutFiles.setGeometry(QtCore.QRect(400, 250, 256, 192))
        self.listWidget_OutFiles.setObjectName(_fromUtf8("listWidget_OutFiles"))
        self.Button_ShowRaport = QtGui.QPushButton(self.page_2)
        self.Button_ShowRaport.setGeometry(QtCore.QRect(430, 510, 91, 23))
        self.Button_ShowRaport.setObjectName(_fromUtf8("Button_ShowRaport"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.listWidget_MainFile = QtGui.QListWidget(self.page_3)
        self.listWidget_MainFile.setGeometry(QtCore.QRect(10, 100, 351, 481))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        self.listWidget_MainFile.setFont(font)
        self.listWidget_MainFile.setObjectName(_fromUtf8("listWidget_MainFile"))
        self.listWidget_OutFilesList = QtGui.QListWidget(self.page_3)
        self.listWidget_OutFilesList.setGeometry(QtCore.QRect(360, 30, 351, 61))
        self.listWidget_OutFilesList.setObjectName(_fromUtf8("listWidget_OutFilesList"))
        self.listWidget_ChoosenOutFile = QtGui.QListWidget(self.page_3)
        self.listWidget_ChoosenOutFile.setGeometry(QtCore.QRect(370, 100, 351, 481))
        self.listWidget_ChoosenOutFile.setObjectName(_fromUtf8("listWidget_ChoosenOutFile"))
        self.stackedWidget.addWidget(self.page_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 858, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.testButton.setText(_translate("MainWindow", "spamToLoadButton XD", None))
        self.label.setText(_translate("MainWindow", "Load Main File", None))
        self.Button_LoadMainFile.setText(_translate("MainWindow", "Load", None))
        self.label_2.setText(_translate("MainWindow", "or Config", None))
        self.Button_Next1.setText(_translate("MainWindow", "Next", None))
        self.Button_LoadConfig.setText(_translate("MainWindow", "Load", None))
        self.Button_Next2.setText(_translate("MainWindow", "Next", None))
        self.Button_LoadOutFileCandidate.setText(_translate("MainWindow", "Load Candidate", None))
        self.Label_LoadConfig.setText(_translate("MainWindow", "LoadConfig", None))
        self.Button_AddOutFromCandidate.setText(_translate("MainWindow", "Make OutFile", None))
        self.Button_ShowRaport.setText(_translate("MainWindow", "Raport", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))

