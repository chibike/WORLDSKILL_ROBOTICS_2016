import sys
from PyQt4 import QtCore, QtGui

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

class Ui_Blink_Box_v12(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Blink_Box_v12, self).__init__()
        self.setObjectName(_fromUtf8("Blink_Box_v12"))
        self.resize(1468, 902)
        self.setMinimumSize(QtCore.QSize(1124, 822))
        self.setWindowIcon(QtGui.QIcon("logo01.png"))
        
        self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Triangular)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))

        self.mapTab = QtGui.QWidget()
        self.mapTab.setObjectName(_fromUtf8("mapTab"))

        self.mapVerticalLayout = QtGui.QVBoxLayout(self.mapTab)
        self.mapVerticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.graphicsView = QtGui.QGraphicsView()
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.mapVerticalLayout.addWidget(self.graphicsView)
        
        self.tabWidget.addTab(self.mapTab, _fromUtf8(""))
        
        self.Scripts = QtGui.QWidget()
        self.Scripts.setObjectName(_fromUtf8("Scripts"))

        self.scriptsVerticalLayout = QtGui.QVBoxLayout(self.Scripts)
        self.scriptsVerticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.textEdit = QtGui.QTextEdit()
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.scriptsVerticalLayout.addWidget(self.textEdit)
        
        self.tabWidget.addTab(self.Scripts, _fromUtf8(""))
        
        self.verticalLayout.addWidget(self.tabWidget)

        self.tabWidget.setCurrentWidget(self.mapTab)
        
        #self.pushButton = QtGui.QPushButton(self.centralwidget)
        #self.pushButton.setGeometry(QtCore.QRect(270, 370, 112, 34))
        #self.pushButton.setObjectName(_fromUtf8("pushButton"))
        
        self.setCentralWidget(self.centralwidget)
        
        self.menubar = QtGui.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1468, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        
        self.menuOptions = QtGui.QMenu(self.menubar)
        self.menuOptions.setObjectName(_fromUtf8("menuOptions"))
        
        self.menuObjects = QtGui.QMenu(self.menubar)
        self.menuObjects.setObjectName(_fromUtf8("menuObjects"))
        
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        
        self.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        self.setStatusBar(self.statusbar)
        
        self.shapesToolBar = QtGui.QToolBar(self)
        self.shapesToolBar.setObjectName(_fromUtf8("shapesToolBar"))
        
        self.addToolBar(QtCore.Qt.LeftToolBarArea, self.shapesToolBar)
        
        self.optionsToolBar = QtGui.QToolBar(self)
        self.optionsToolBar.setObjectName(_fromUtf8("optionsToolBar"))
        
        self.addToolBar(QtCore.Qt.RightToolBarArea, self.optionsToolBar)

        buildAction = QtGui.QAction(QtGui.QIcon('buildSign01.png'), "Build Map", self)
        buildAction.triggered.connect(self.build_map)
        buildAction.setStatusTip("Build Map  F5")
        buildAction.setShortcut("F5")

        uploadAction = QtGui.QAction(QtGui.QIcon('uploadButton01.png'), "Upload Map", self)
        uploadAction.triggered.connect(self.upload_map)
        uploadAction.setStatusTip("Upload Map  Ctrl+U")
        uploadAction.setShortcut("Ctrl+U")

        excuteAction = QtGui.QAction(QtGui.QIcon('excuteButton01.png'), "Excute Map", self)
        excuteAction.triggered.connect(self.excute_map)
        excuteAction.setStatusTip("Excute Map  Ctrl+R")
        excuteAction.setShortcut("Ctrl+R")
        
        self.mainToolBar = QtGui.QToolBar(self)
        self.mainToolBar.setIconSize(QtCore.QSize(40, 40))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBar.addAction(buildAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(uploadAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(excuteAction)
        self.mainToolBar.addSeparator()
        
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        
        self.statusToolBar = QtGui.QToolBar(self)
        self.statusToolBar.setObjectName(_fromUtf8("statusToolBar"))
        
        self.addToolBar(QtCore.Qt.BottomToolBarArea, self.statusToolBar)
        
        self.actionNew = QtGui.QAction(self)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        
        self.actionOpen = QtGui.QAction(self)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        
        self.actionSave = QtGui.QAction(self)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        
        self.actionSave_as = QtGui.QAction(self)
        self.actionSave_as.setObjectName(_fromUtf8("actionSave_as"))
        
        self.actionSave_all = QtGui.QAction(self)
        self.actionSave_all.setObjectName(_fromUtf8("actionSave_all"))
        
        self.actionSave_as_Template = QtGui.QAction(self)
        self.actionSave_as_Template.setObjectName(_fromUtf8("actionSave_as_Template"))
        
        self.actionPrint = QtGui.QAction(self)
        self.actionPrint.setObjectName(_fromUtf8("actionPrint"))
        
        self.actionSave_as_Image = QtGui.QAction(self)
        self.actionSave_as_Image.setObjectName(_fromUtf8("actionSave_as_Image"))
        
        self.actionClose = QtGui.QAction(self)
        self.actionClose.setObjectName(_fromUtf8("actionClose"))
        
        self.actionQuit = QtGui.QAction(self)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_all)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionSave_as_Image)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addAction(self.actionQuit)

        self.actionRedo = QtGui.QAction(self)
        self.actionRedo.setObjectName(_fromUtf8("actionRedo"))

        self.actionUndo = QtGui.QAction(self)
        self.actionUndo.setObjectName(_fromUtf8("actionUndo"))

        self.actionCut = QtGui.QAction(self)
        self.actionCut.setObjectName(_fromUtf8("actionCut"))

        self.actionCopy = QtGui.QAction(self)
        self.actionCopy.setObjectName(_fromUtf8("actionCopy"))

        self.actionPaste = QtGui.QAction(self)
        self.actionPaste.setObjectName(_fromUtf8("actionPaste"))

        self.actionSelectAll = QtGui.QAction(self)
        self.actionSelectAll.setObjectName(_fromUtf8("actionSelectAll"))

        self.actionFind = QtGui.QAction(self)
        self.actionFind.setObjectName(_fromUtf8("actionFind"))
        
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuEdit.addAction(self.actionSelectAll)
        self.menuEdit.addSeparator()
        
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuObjects.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi()
        
        self.tabWidget.setCurrentIndex(1)
        
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        self.setWindowTitle(_translate("Blink_Box_v12", "Blink Box Navigator v12", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapTab), _translate("Blink_Box_v12", "Map", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scripts), _translate("Blink_Box_v12", "Scripts", None))
        
        #self.pushButton.setText(_translate("Blink_Box_v12", "PushButton", None))
        
        self.menuFile.setTitle(_translate("Blink_Box_v12", "File", None))
        
        self.menuEdit.setTitle(_translate("Blink_Box_v12", "Edit", None))
        
        self.menuOptions.setTitle(_translate("Blink_Box_v12", "Options", None))
        
        self.menuObjects.setTitle(_translate("Blink_Box_v12", "Objects", None))
        
        self.menuHelp.setTitle(_translate("Blink_Box_v12", "Help", None))
        
        self.menuSettings.setTitle(_translate("Blink_Box_v12", "Settings", None))
        
        self.shapesToolBar.setWindowTitle(_translate("Blink_Box_v12", "toolBar", None))
        
        self.optionsToolBar.setWindowTitle(_translate("Blink_Box_v12", "toolBar_2", None))
        
        self.mainToolBar.setWindowTitle(_translate("Blink_Box_v12", "toolBar_3", None))
        
        self.statusToolBar.setWindowTitle(_translate("Blink_Box_v12", "toolBar", None))
        
        self.actionNew.setText(_translate("Blink_Box_v12", "New", None))
        
        self.actionOpen.setText(_translate("Blink_Box_v12", "Open", None))
        self.actionOpen.setShortcut("Ctrl+O")
        self.actionOpen.setStatusTip("Open Map File")
        self.actionOpen.triggered.connect(self.open_map_file)
        
        self.actionSave.setText(_translate("Blink_Box_v12", "Save", None))
        self.actionSave.setShortcut("Ctrl+S")
        self.actionSave.setStatusTip("Save Current Tab")
        self.actionSave.triggered.connect(self.save_current_tab)
        
        self.actionSave_as.setText(_translate("Blink_Box_v12", "Save as", None))
        
        self.actionSave_all.setText(_translate("Blink_Box_v12", "Save all", None))
        
        self.actionSave_as_Template.setText(_translate("Blink_Box_v12", "Save as Template", None))
        
        self.actionPrint.setText(_translate("Blink_Box_v12", "Print", None))
        
        self.actionSave_as_Image.setText(_translate("Blink_Box_v12", "Save as Image", None))
        
        self.actionClose.setText(_translate("Blink_Box_v12", "Close", None))
        self.actionClose.setShortcut("Alt+F4")
        self.actionClose.setStatusTip("Close Application")
        self.actionClose.triggered.connect(self.close_application)
        
        self.actionQuit.setText(_translate("Blink_Box_v12", "Quit", None))
        self.actionQuit.setShortcut("Ctrl+Q")
        self.actionQuit.setStatusTip("Quit Application")
        self.actionQuit.triggered.connect(self.close_application)

        self.actionRedo.setText(_translate("Blink_Box_v12", "Redo", None))
        self.actionRedo.setShortcut("Ctrl+Y")
        self.actionRedo.setStatusTip("Redo")
        self.actionRedo.triggered.connect(self.redo)

        self.actionUndo.setText(_translate("Blink_Box_v12", "Undo", None))
        self.actionUndo.setShortcut("Ctrl+Z")
        self.actionUndo.setStatusTip("Undo")
        self.actionUndo.triggered.connect(self.undo)
        
        self.actionCut.setText(_translate("Blink_Box_v12", "Cut", None))
        self.actionCut.setShortcut("Ctrl+X")
        self.actionCut.setStatusTip("Cut")
        self.actionCut.triggered.connect(self.cut)

        self.actionCopy.setText(_translate("Blink_Box_v12", "Copy", None))
        self.actionCopy.setShortcut("Ctrl+C")
        self.actionCopy.setStatusTip("Copy")
        self.actionCopy.triggered.connect(self.copy)

        self.actionPaste.setText(_translate("Blink_Box_v12", "Paste", None))
        self.actionPaste.setShortcut("Ctrl+V")
        self.actionPaste.setStatusTip("Paste")
        self.actionPaste.triggered.connect(self.paste)

        self.actionSelectAll.setText(_translate("Blink_Box_v12", "Select All", None))
        self.actionSelectAll.setShortcut("Ctrl+A")
        self.actionSelectAll.setStatusTip("Select All")
        self.actionSelectAll.triggered.connect(self.select_all)

        self.actionFind.setText(_translate("Blink_Box_v12", "Find", None))
        self.actionFind.setShortcut("Ctrl+F")
        self.actionFind.setStatusTip("Find")
        self.actionFind.triggered.connect(self.find)
        
        self.show()
    def fine(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Cut Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.copyAvailable:
                pass
    def print_file(self):
        print "printing"
        #printer = QtGui.QPrintDialog.getPrinter()
        #self.print_file()
    def cut(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Cut Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.copyAvailable:
                self.textEdit.cut()
    def copy(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Cut Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.copyAvailable:
                self.textEdit.copy()
    def paste(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Cut Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            self.textEdit.paste()
    def select_all(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Cut Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            self.textEdit.selectAll()
    def redo(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Redo Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.redoAvailable:
                self.textEdit.redo()
    def undo(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Undo Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.undoAvailable:
                self.textEdit.undo()
    def open_map_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        if name:
            fileName = str(name)
            with open(name, 'r') as file:
                text = file.read()
                if fileName.endswith('.txt') or fileName.endswith('.bm_script'):
                    self.textEdit.setText(text)
                elif fileName.endswith('.b_map'):
                    pass
                else:
                    print "invalid name"
                    self.warning("Invalid File")
        else:
            self.warning("Invalid Name")
    def warning(self, info):
        QtGui.QMessageBox.about(self, "Warning !!!", info)
    def save_current_tab(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Saving Maps"
        elif self.tabWidget.currentWidget() == self.Scripts:
            name = QtGui.QFileDialog.getSaveFileName(self, "Save File")
            if name:
                file = open(name, 'w')
                text = self.textEdit.toPlainText()
                file.write(text)
                file.close()
            else:
                return
        else:
            print self.tabWidget.currentWidget()
    def excute_map(self):
        print "Excuting Map"
    def upload_map(self):
        print "Uploading Map"
    def build_map(self):
        print "Building Map"
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Close Window",
                                            "Do you want to exit?",
                                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Blink_Box_v12()
    sys.exit(app.exec_())
