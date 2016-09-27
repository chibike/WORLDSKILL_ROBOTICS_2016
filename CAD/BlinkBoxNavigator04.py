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

def getRectangle(width, height, pen, brush):
    rect = QtGui.QPolygonF([
        QtCore.QPointF(0,0), QtCore.QPointF(0,height),
        QtCore.QPointF(width, height), QtCore.QPointF(width,0),
        QtCore.QPointF(0, 0)
        ])
    rectItem = QtGui.QGraphicsPolygonItem()
    rectItem.setPolygon(rect)
    rectItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    rectItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    rectItem.setBrush(brush)
    rectItem.setPen(pen)
    return rectItem

def getLine(length, pen, brush):
    line = QtGui.QPolygonF([
        QtCore.QPointF(0,0), QtCore.QPointF(length, 0)
        ])
    lineItem = QtGui.QGraphicsPolygonItem()
    lineItem.setPolygon(line)
    lineItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    lineItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    lineItem.setBrush(brush)
    lineItem.setPen(pen)
    return lineItem

def getTriangle(a, b, c, pen, brush):
    triangle = QtGui.QPolygonF([
        QtCore.QPointF(0,0),QtCore.QPointF(50,50),
        QtCore.QPointF(0,50),QtCore.QPointF(0,0)
        ])
    triangleItem = QtGui.QGraphicsPolygonItem()
    triangleItem.setPolygon(triangle)
    triangleItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    triangleItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    triangleItem.setBrush(brush)
    triangleItem.setPen(pen)
    return triangleItem

class MapScene(QtGui.QGraphicsScene):
    def __init__(self, parent=None):
        super(MapScene, self).__init__(parent)
    def wheelEvent(self, wheelEvent):
        #print "wheelEvent =",dir(wheelEvent)
        #p = QtGui.QGraphicsSceneWheelEvent()
        #print "p=",p.delta()
        #print "p=",p
        pass
class Ui_Blink_Box_v12(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Blink_Box_v12, self).__init__()
        self.setObjectName(_fromUtf8("Blink_Box_v12"))
        self.resize(1468, 902)
        self.setMinimumSize(QtCore.QSize(1124, 822))
        self.setWindowIcon(QtGui.QIcon("logo01.png"))
        
        self.setup_stroke()
        self.setup_fill()
        
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

        self.moveButton = QtGui.QPushButton(QtGui.QIcon('moveObjectButton01.png'), "Move")
        self.moveButton.setObjectName(_fromUtf8("moveButton"))
        
        self.tweakButton = QtGui.QPushButton(QtGui.QIcon('tweakButton01.png'), "Tweak")
        self.tweakButton.setObjectName(_fromUtf8("tweakButton"))

        self.pointerTypeGroup = QtGui.QButtonGroup()
        self.pointerTypeGroup.addButton(self.moveButton)
        self.pointerTypeGroup.addButton(self.tweakButton)
        self.pointerTypeGroup.buttonClicked[int].connect(self.pointer_group_clicked)
        
        self.shapesButton = QtGui.QPushButton(QtGui.QIcon('shapesButton01.png'), "Shapes")
        self.shapesButton.setObjectName(_fromUtf8("shapesButton"))

        self.pathButton = QtGui.QPushButton(QtGui.QIcon("pathButton01.png"), "Route")
        self.pathButton.setObjectName(_fromUtf8("pathButton"))

        self.todoButton = QtGui.QPushButton(QtGui.QIcon('addToDo09.png'), "Todo")
        self.todoButton.setObjectName(_fromUtf8("todoButton"))

        self.tagButton = QtGui.QPushButton(QtGui.QIcon('addTag01.png'), "Tag")
        self.tagButton.setObjectName(_fromUtf8("tagButton"))

        self.draw_tab_font_creator();
        
        self.shapesToolBar = QtGui.QToolBar(self)
        self.shapesToolBar.setObjectName(_fromUtf8("shapesToolBar"))
        self.shapesToolBar.toolButtonStyle()
        self.shapesToolBar.addWidget(self.moveButton)
        self.shapesToolBar.addWidget(self.tweakButton)
        self.shapesToolBar.addSeparator()
        self.shapesToolBar.addWidget(self.shapesButton)
        self.shapesToolBar.addWidget(self.pathButton)
        self.shapesToolBar.addWidget(self.todoButton)
        self.shapesToolBar.addWidget(self.tagButton)
        self.shapesToolBar.addSeparator()
        self.shapesToolBar.addWidget(self.fontCombo)
        self.shapesToolBar.addWidget(self.fontSizeCombo)
        self.shapesToolBar.addAction(self.boldAction)
        self.shapesToolBar.addAction(self.italicAction)
        self.shapesToolBar.addAction(self.underlineAction)
        self.shapesToolBar.addSeparator()
        self.shapesToolBar.addWidget(self.fontColorToolButton)
        self.shapesToolBar.addWidget(self.fillColorToolButton)
        self.shapesToolBar.addWidget(self.lineColorToolButton)
        self.shapesToolBar.addSeparator()
        self.shapesToolBar.addAction(self.sendToBackAction)
        self.shapesToolBar.addAction(self.sendToFrontAction)
        self.shapesToolBar.addAction(self.deleteAction)
        
        self.mapVerticalLayout.addWidget(self.shapesToolBar)

        #self.scene = QtGui.QGraphicsScene()
        self.scene = MapScene()
        self.scene.wheelEvent(self.scroll_event_handler)
        self.graphicsView = QtGui.QGraphicsView(self.scene)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.mapVerticalLayout.addWidget(self.graphicsView)

        #self.optionsToolBar = QtGui.QToolBar(self)
        #self.optionsToolBar.setObjectName(_fromUtf8("optionsToolBar"))
        #self.mapVerticalLayout.addWidget(self.optionsToolBar)

        self.bottom_widget_creator()
        self.mapVerticalLayout.addWidget(self.objectOptionsTabWidth)
        
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

        self.shapesSelectionMenu = QtGui.QMenu()
        self.shapesSelectionMenu.setObjectName(_fromUtf8("shapesSelectionMenu"))

        self.todoSelectionMenu = QtGui.QMenu()
        self.todoSelectionMenu.setObjectName(_fromUtf8("todoSelectionMenu"))

        self.tagSelectionMenu = QtGui.QMenu()
        self.tagSelectionMenu.setObjectName(_fromUtf8("tagSelectionMenu"))
        
        self.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        self.setStatusBar(self.statusbar)
        
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

        evaluateAction = QtGui.QAction(QtGui.QIcon('evaluateButton03.png'), "Evaluate Map", self)
        evaluateAction.triggered.connect(self.evaluate_map)
        evaluateAction.setStatusTip("Evaluate Map Route  Ctrl+Atl+R")
        evaluateAction.setShortcut("Ctrl+Atl+R")

        self.mainToolBar = QtGui.QToolBar(self)
        self.mainToolBar.setIconSize(QtCore.QSize(40, 40))
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        self.mainToolBar.addAction(buildAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(uploadAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(excuteAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(evaluateAction)
        
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        
        #self.statusToolBar = QtGui.QToolBar(self)
        #self.statusToolBar.setObjectName(_fromUtf8("statusToolBar"))
        
        #self.addToolBar(QtCore.Qt.BottomToolBarArea, self.statusToolBar)
        
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

        self.actionLine = QtGui.QAction(self)
        self.actionLine.setObjectName(_fromUtf8("actionLine"))

        self.actionRectangle = QtGui.QAction(self)
        self.actionRectangle.setObjectName(_fromUtf8("actionRectangle"))

        self.actionEllipse = QtGui.QAction(self)
        self.actionEllipse.setObjectName(_fromUtf8("actionEllipse"))

        self.actionTriangle = QtGui.QAction(self)
        self.actionTriangle.setObjectName(_fromUtf8("actionTriangle"))

        self.actionPolygon = QtGui.QAction(self)
        self.actionPolygon.setObjectName(_fromUtf8("actionPolygon"))

        self.shapesSelectionMenu.addAction(self.actionLine)
        self.shapesSelectionMenu.addAction(self.actionRectangle)
        self.shapesSelectionMenu.addAction(self.actionEllipse)
        self.shapesSelectionMenu.addAction(self.actionTriangle)
        self.shapesSelectionMenu.addAction(self.actionPolygon)
        
        self.shapesButton.setMenu(self.shapesSelectionMenu)

        
        self.actionScan = QtGui.QAction(self)
        self.actionScan.setObjectName(_fromUtf8("actionScan"))
        
        self.todoSelectionMenu.addAction(self.actionScan)
        
        self.todoButton.setMenu(self.todoSelectionMenu)

        self.actionAvoidObstacles = QtGui.QAction(self)
        self.actionAvoidObstacles.setObjectName(_fromUtf8("actionAvoidObstacles"))
        
        self.tagSelectionMenu.addAction(self.actionAvoidObstacles)
        
        self.tagButton.setMenu(self.tagSelectionMenu)
        
        #self.bottom_widget_creator()
        
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        
    def retranslateUi(self):
        self.setWindowTitle(_translate("Blink_Box_v12", "Blink Box Navigator v12", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))
        self.okayButton.setText(_translate("Form", "Okay", None))
        self.radiusLabel.setText(_translate("Form", "Radius", None))
        self.widthLabel.setText(_translate("Form", "Width", None))
        self.StrokeTypeLabel.setText(_translate("Form", "Stroke Type", None))
        self.xPositionLabel.setText(_translate("Form", "xPosition", None))
        self.yPositionLabel.setText(_translate("Form", "yPositon", None))
        self.strokeWidthLabel.setText(_translate("Form", "Stroke Width", None))
        self.heightLabel.setText(_translate("Form", "Height", None))
        self.zoomLabel.setText(_translate("Form", "Zoom", None))
        self.lengthLabel.setText(_translate("Form", "Length", None))
        self.selectStrokeColorButton.setText(_translate("Form", "Select Stroke Color", None))
        self.selectFillColorButton.setText(_translate("Form", "Select Fill Color", None))
        self.objectOptionsTabWidth.setTabText(self.objectOptionsTabWidth.indexOf(self.tab), _translate("Form", "Object Properties", None))
        self.sendButton.setText(_translate("Form", "Send", None))
        self.readAllButton.setText(_translate("Form", "Read All", None))
        self.save2FileButton.setText(_translate("Form", "Save to File", None))
        self.clearButton.setText(_translate("Form", "Clear", None))
        self.connectButton.setText(_translate("Form", "Connect", None))
        self.serialPortLabel.setText(_translate("Form", "Serial Port", None))
        self.baudrateLabel.setText(_translate("Form", "Baud Rate", None))
        self.objectOptionsTabWidth.setTabText(self.objectOptionsTabWidth.indexOf(self.serialTab), _translate("Form", "Bluetooth Com Port Settings", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.mapTab), _translate("Blink_Box_v12", "Map", None))
        
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scripts), _translate("Blink_Box_v12", "Scripts", None))
        
        self.menuFile.setTitle(_translate("Blink_Box_v12", "File", None))
        
        self.menuEdit.setTitle(_translate("Blink_Box_v12", "Edit", None))
        
        self.menuOptions.setTitle(_translate("Blink_Box_v12", "Options", None))
        
        self.menuObjects.setTitle(_translate("Blink_Box_v12", "Objects", None))
        
        self.menuHelp.setTitle(_translate("Blink_Box_v12", "Help", None))
        
        self.menuSettings.setTitle(_translate("Blink_Box_v12", "Settings", None))
        
        self.shapesToolBar.setWindowTitle(_translate("Blink_Box_v12", "shapesToolBar", None))
        
        #self.optionsToolBar.setWindowTitle(_translate("Blink_Box_v12", "optionsToolBar", None))
        
        self.mainToolBar.setWindowTitle(_translate("Blink_Box_v12", "mainToolBar", None))
        
        #self.statusToolBar.setWindowTitle(_translate("Blink_Box_v12", "statusToolBar", None))
        
        self.actionNew.setText(_translate("Blink_Box_v12", "New", None))

        self.actionScan.setText(_translate("Blink_Box_v12", "Add Scan Task", None))
        #self.actionScan.setShortcut("")
        self.actionScan.setStatusTip("Click Any Junction To Add a Scan Remindered")
        self.actionScan.triggered.connect(self.add_todo_scan)
        self.actionScan.setIcon(QtGui.QIcon('scanTask02.png'))

        self.actionAvoidObstacles.setText(_translate("Blink_Box_v12", "Add Obstacle Avoidance Tag", None))
        #self.actionAvoidObstacles.setShortcut("")
        self.actionAvoidObstacles.setStatusTip("Click Any Route To Add An Obstacles Avoidance Tag")
        self.actionAvoidObstacles.triggered.connect(self.add_tag_avoid_obstacles)
        self.actionAvoidObstacles.setIcon(QtGui.QIcon('obstacleTag02.png'))

        self.actionLine.setText(_translate("Blink_Box_v12", "Line", None))
        #self.actionLine.setShortcut("")
        self.actionLine.setStatusTip("Draw Line")
        self.actionLine.triggered.connect(self.draw_line)
        self.actionLine.setIcon(QtGui.QIcon('lineButton01.png'))
        
        self.actionRectangle.setText(_translate("Blink_Box_v12", "Rectangle", None))
        #self.actionRectangle.setShortcut("")
        self.actionRectangle.setStatusTip("Draw Rectangle")
        self.actionRectangle.triggered.connect(self.draw_rect)
        self.actionRectangle.setIcon(QtGui.QIcon('shapesRectButton01.png'))

        self.actionEllipse.setText(_translate("Blink_Box_v12", "Ellipse", None))
        #self.actionEllipse.setShortcut("")
        self.actionEllipse.setStatusTip("Draw Ellipse")
        self.actionEllipse.triggered.connect(self.draw_ellipse)
        self.actionEllipse.setIcon(QtGui.QIcon('shapesEllipseButton01.png'))

        self.actionTriangle.setText(_translate("Blink_Box_v12", "Triangle", None))
        #self.actionTriangle.setShortcut("")
        self.actionTriangle.setStatusTip("Draw Triangle")
        self.actionTriangle.triggered.connect(self.draw_triangle)
        self.actionTriangle.setIcon(QtGui.QIcon('shapesTriangleButton01.png'))

        self.actionPolygon.setText(_translate("Blink_Box_v12", "Polygon", None))
        #self.actionPolygon.setShortcut("")
        self.actionPolygon.setStatusTip("Draw Polygon")
        self.actionPolygon.triggered.connect(self.draw_polygon)
        self.actionPolygon.setIcon(QtGui.QIcon('shapesPolygonButton01.png'))
        
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
    def bottom_widget_creator(self):
        self.objectOptionsTabWidth = QtGui.QTabWidget()
        self.objectOptionsTabWidth.setGeometry(QtCore.QRect(10, 0, 1311, 400))
        self.objectOptionsTabWidth.setTabsClosable(False)
        self.objectOptionsTabWidth.setMovable(True)
        self.objectOptionsTabWidth.setObjectName(_fromUtf8("objectOptionsTabWidth"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 1, 1181, 261))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 10, 3, 1, 1)
        self.okayButton = QtGui.QPushButton(self.widget)
        self.okayButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.okayButton.setObjectName(_fromUtf8("okayButton"))
        self.gridLayout.addWidget(self.okayButton, 10, 2, 1, 1)
        self.zoomHorizontalSlider = QtGui.QSlider(self.widget)
        self.zoomHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomHorizontalSlider.setObjectName(_fromUtf8("zoomHorizontalSlider"))
        self.zoomHorizontalSlider.setTickInterval(2)
        self.zoomHorizontalSlider.setTickPosition(self.zoomHorizontalSlider.TicksBothSides)
        self.zoomHorizontalSlider.setMinimum(-150)
        self.zoomHorizontalSlider.setMaximum(150)
        self.zoomHorizontalSlider.valueChanged.connect(self.set_qview_zoom)
        self.gridLayout.addWidget(self.zoomHorizontalSlider, 9, 1, 1, 3)
        self.strokeWidthSpinBox = QtGui.QSpinBox(self.widget)
        self.strokeWidthSpinBox.setObjectName(_fromUtf8("strokeWidthSpinBox"))
        self.gridLayout.addWidget(self.strokeWidthSpinBox, 1, 3, 1, 1)
        self.radiusLabel = QtGui.QLabel(self.widget)
        self.radiusLabel.setObjectName(_fromUtf8("radiusLabel"))
        self.gridLayout.addWidget(self.radiusLabel, 3, 0, 1, 1)
        self.widthLabel = QtGui.QLabel(self.widget)
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.gridLayout.addWidget(self.widthLabel, 1, 0, 1, 1)
        self.StrokeTypeLabel = QtGui.QLabel(self.widget)
        self.StrokeTypeLabel.setObjectName(_fromUtf8("StrokeTypeLabel"))
        self.gridLayout.addWidget(self.StrokeTypeLabel, 2, 2, 1, 1)
        self.xPositionLabel = QtGui.QLabel(self.widget)
        self.xPositionLabel.setObjectName(_fromUtf8("xPositionLabel"))
        self.gridLayout.addWidget(self.xPositionLabel, 3, 2, 1, 1)
        self.xPositionSpinBox = QtGui.QSpinBox(self.widget)
        self.xPositionSpinBox.setObjectName(_fromUtf8("xPositionSpinBox"))
        self.gridLayout.addWidget(self.xPositionSpinBox, 3, 3, 1, 1)
        self.yPositionSpinBox = QtGui.QSpinBox(self.widget)
        self.yPositionSpinBox.setObjectName(_fromUtf8("yPositionSpinBox"))
        self.gridLayout.addWidget(self.yPositionSpinBox, 4, 3, 1, 1)
        self.strokeTypeComboBox = QtGui.QComboBox(self.widget)
        self.strokeTypeComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.strokeTypeComboBox.setObjectName(_fromUtf8("strokeTypeComboBox"))
        self.gridLayout.addWidget(self.strokeTypeComboBox, 2, 3, 1, 1)
        self.yPositionLabel = QtGui.QLabel(self.widget)
        self.yPositionLabel.setObjectName(_fromUtf8("yPositionLabel"))
        self.gridLayout.addWidget(self.yPositionLabel, 4, 2, 1, 1)
        self.strokeWidthLabel = QtGui.QLabel(self.widget)
        self.strokeWidthLabel.setObjectName(_fromUtf8("strokeWidthLabel"))
        self.gridLayout.addWidget(self.strokeWidthLabel, 1, 2, 1, 1)
        self.lengthEntry = QtGui.QLineEdit(self.widget)
        self.lengthEntry.setMaxLength(50000)
        self.lengthEntry.setObjectName(_fromUtf8("lengthEntry"))
        self.gridLayout.addWidget(self.lengthEntry, 4, 1, 1, 1)
        self.widthEntry = QtGui.QLineEdit(self.widget)
        self.widthEntry.setMaxLength(50000)
        self.widthEntry.setObjectName(_fromUtf8("widthEntry"))
        self.gridLayout.addWidget(self.widthEntry, 1, 1, 1, 1)
        self.heightLabel = QtGui.QLabel(self.widget)
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.gridLayout.addWidget(self.heightLabel, 2, 0, 1, 1)
        self.zoomLabel = QtGui.QLabel(self.widget)
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.gridLayout.addWidget(self.zoomLabel, 9, 0, 1, 1)
        self.heightEntry = QtGui.QLineEdit(self.widget)
        self.heightEntry.setMaxLength(50000)
        self.heightEntry.setObjectName(_fromUtf8("heightEntry"))
        self.gridLayout.addWidget(self.heightEntry, 2, 1, 1, 1)
        self.lengthLabel = QtGui.QLabel(self.widget)
        self.lengthLabel.setObjectName(_fromUtf8("lengthLabel"))
        self.gridLayout.addWidget(self.lengthLabel, 4, 0, 1, 1)
        self.raduisEntry = QtGui.QLineEdit(self.widget)
        self.raduisEntry.setMaxLength(50000)
        self.raduisEntry.setObjectName(_fromUtf8("raduisEntry"))
        self.gridLayout.addWidget(self.raduisEntry, 3, 1, 1, 1)
        self.selectStrokeColorButton = QtGui.QPushButton(self.widget)
        self.selectStrokeColorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectStrokeColorButton.setObjectName(_fromUtf8("selectStrokeColorButton"))
        self.gridLayout.addWidget(self.selectStrokeColorButton, 1, 4, 1, 1)
        self.selectFillColorButton = QtGui.QPushButton(self.widget)
        self.selectFillColorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.selectFillColorButton.setObjectName(_fromUtf8("selectFillColorButton"))
        self.gridLayout.addWidget(self.selectFillColorButton, 3, 4, 1, 1)
        self.objectOptionsTabWidth.addTab(self.tab, _fromUtf8(""))
        self.serialTab = QtGui.QWidget()
        self.serialTab.setObjectName(_fromUtf8("serialTab"))
        self.gridLayoutWidget_2 = QtGui.QWidget(self.serialTab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 1, 1171, 282))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.sendButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.sendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.verticalLayout_2.addWidget(self.sendButton)
        self.readAllButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.readAllButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.readAllButton.setObjectName(_fromUtf8("readAllButton"))
        self.verticalLayout_2.addWidget(self.readAllButton)
        self.save2FileButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.save2FileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save2FileButton.setObjectName(_fromUtf8("save2FileButton"))
        self.verticalLayout_2.addWidget(self.save2FileButton)
        self.clearButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.verticalLayout_2.addWidget(self.clearButton)
        self.connectButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.connectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        self.verticalLayout_2.addWidget(self.connectButton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.serialMessageEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.serialMessageEntry.setMaxLength(200000)
        self.serialMessageEntry.setObjectName(_fromUtf8("serialMessageEntry"))
        self.verticalLayout_3.addWidget(self.serialMessageEntry)
        self.serialMessageDisplay = QtGui.QPlainTextEdit(self.gridLayoutWidget_2)
        self.serialMessageDisplay.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.serialMessageDisplay.setFrameShadow(QtGui.QFrame.Plain)
        self.serialMessageDisplay.setReadOnly(True)
        self.serialMessageDisplay.setObjectName(_fromUtf8("serialMessageDisplay"))
        self.verticalLayout_3.addWidget(self.serialMessageDisplay)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.serialPortEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.serialPortEntry.setMaxLength(200000)
        self.serialPortEntry.setObjectName(_fromUtf8("serialPortEntry"))
        self.gridLayout_2.addWidget(self.serialPortEntry, 1, 1, 1, 1)
        self.baudrateEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.baudrateEntry.setMaxLength(200000)
        self.baudrateEntry.setObjectName(_fromUtf8("baudrateEntry"))
        self.gridLayout_2.addWidget(self.baudrateEntry, 2, 1, 1, 1)
        self.serialPortLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.serialPortLabel.setObjectName(_fromUtf8("serialPortLabel"))
        self.gridLayout_2.addWidget(self.serialPortLabel, 1, 0, 1, 1)
        self.baudrateLabel = QtGui.QLabel(self.gridLayoutWidget_2)
        self.baudrateLabel.setObjectName(_fromUtf8("baudrateLabel"))
        self.gridLayout_2.addWidget(self.baudrateLabel, 2, 0, 1, 1)
        self.objectOptionsTabWidth.addTab(self.serialTab, _fromUtf8(""))

        self.objectOptionsTabWidth.setCurrentIndex(0)

    def set_qview_zoom(self, value):
        value = (value/140)
        print "Val =",value
        self.graphicsView.scale(value, value)
    def scroll_event_handler(self, event):
        print "scroll event =",event
    def setup_stroke(self):
        self.myPen = QtGui.QPen()
        self.myPen.setColor(QtCore.Qt.black)
        self.myPen.setWidth(5)

    def setup_fill(self):
        self.myBrush = QtGui.QBrush()
        self.myBrush.setColor(QtCore.Qt.black)
        
    def create_color_tool_button_icon(self, imageFile, color):
        pixmap = QtGui.QPixmap(50, 80)
        pixmap.fill(QtCore.Qt.transparent)
        painter = QtGui.QPainter(pixmap)
        image = QtGui.QPixmap(imageFile)
        target = QtCore.QRect(0, 0, 50, 60)
        source = QtCore.QRect(0, 0, 42, 42)
        painter.fillRect(QtCore.QRect(0, 60, 50, 80), color)
        painter.drawPixmap(target, image, source)
        painter.end()

        return QtGui.QIcon(pixmap)
    def create_color_icon(self, color):
        pixmap = QtGui.QPixmap(20, 20)
        painter = QtGui.QPainter(pixmap)
        painter.setPen(QtCore.Qt.NoPen)
        painter.fillRect(QtCore.QRect(0, 0, 20, 20), color)
        painter.end()

        return QtGui.QIcon(pixmap)
    
    def create_color_menu(self, slot, defaultColor):
        colors = [QtCore.Qt.black, QtCore.Qt.white, QtCore.Qt.red, QtCore.Qt.darkRed, QtCore.Qt.blue, QtCore.Qt.darkBlue,
                  QtCore.Qt.yellow, QtCore.Qt.green, QtCore.Qt.darkGreen, QtCore.Qt.cyan, QtCore.Qt.darkCyan,
                  QtCore.Qt.magenta, QtCore.Qt.darkMagenta, QtCore.Qt.darkYellow, QtCore.Qt.gray, QtCore.Qt.darkGray,
                  QtCore.Qt.lightGray, QtCore.Qt.transparent]
        names = ["black", "white", "red", "darkRed", "blue", "darkBlue",
                 "yellow", "green", "darkGreen", "cyan", "darkCyan",
                 "magenta", "darkMagenta", "darkYellow", "gray", "darkGray",
                 "lightGray", "transparent"]

        colorMenu = QtGui.QMenu(self)
        for color, name in zip(colors, names):
            action = QtGui.QAction(self.create_color_icon(color), name, self,
                                   triggered = slot)
            action.setData(QtGui.QColor(color))
            colorMenu.addAction(action)
            if color == defaultColor:
                colorMenu.setDefaultAction(action)
        return colorMenu
    def item_color_changed(self):
        self.fillAction = self.sender()
        self.fillColorToolButton.setIcon(self.create_color_tool_button_icon(
                    'floodfill.png',
                    QtGui.QColor(self.fillAction.data())))
        self.fill_button_triggered()
    def font_size_changed(self, font):
        print "New Font =",font
        self.handle_font_change()
        
    def current_font_changed(self, font):
        print "New Font =",font
        self.handle_font_change()
    def text_color_changed(self):
        self.textAction = self.sender()
        self.fontColorToolButton.setIcon(
            self.create_color_tool_button_icon('textpointer.png',
                                           QtGui.QColor(self.textAction.data())
                                           )
            )
        self.text_button_triggered()
    def line_color_changed(self):
        self.lineAction = self.sender()
        self.lineColorToolButton.setIcon(self.create_color_tool_button_icon(
                    'linecolor.png',
                    QtGui.QColor(self.lineAction.data())))
        self.line_button_triggered()
    def handle_font_change(self):
        font = self.fontCombo.currentFont()
        font.setPointSize(self.fontSizeCombo.currentText().toInt()[0])
        if self.boldAction.isChecked():
            font.setWeight(QtGui.QFont.Bold)
        else:
            font.setWeight(QtGui.QFont.Normal)
        font.setItalic(self.italicAction.isChecked())
        font.setUnderline(self.underlineAction.isChecked())
        self.scene.setFont(font)
    def line_button_triggered(self):
        self.myPen.setColor(QtGui.QColor(self.lineAction.data()))
        print "line_button_triggered"
    def text_button_triggered(self):
        print "text_button_triggered"
        #self.Brush.setColor(QtGui.QColor(self.textAction.data()))
    def fill_button_triggered(self):
        print "fill_button_triggered"
        self.myBrush.setColor(QtGui.QColor(self.fillAction.data()))
    def bring_to_front(self):
        if not self.scene.selectedItems():
            return
        selectedItem = self.scene.selectedItems()[0]
        overlapItems = selectedItem.collidingItems()

        zValue = 0
        for item in overlapItems:
            if item.zValue() >= zValue:
                zValue = item.zValue() + 0.1
        selectedItem.setZValue(zValue)
    def send_to_back(self):
        if not self.scene.selectedItems():
            return

        selectedItem = self.scene.selectedItems()[0]
        overlapItems = selectedItem.collidingItems()

        zValue = 0
        for item in overlapItems:
            if item.zValue <= zValue:
                zValue = itme.zValue() - 0.1
        selectedItem.setZValue(zValue)
    def delete_item(self):
        if not self.scene.selectedItems():
            return

        for item in self.scene.selectedItems():
            self.scene.removeItem(item)
    def tweak_item(self):
        print "Tweak mode enabled"
    def move_item(self):
        print "Move mode enabled"
    def pointer_group_clicked(self, i):
        print "button clicked =",i
        #self.scene.setMode(self.pointerTypeGroup.checkedId())
    def add_todo_scan(self):
        print "Will Add Scanning to Selected Junction"
    def add_tag_avoid_obstacles(self):
        print "Will Add Obstacle Avoidance to Selected Road"
    def draw_path(self):
        print "Drawing Path"
    def draw_triangle(self):
        print "Drawing Triangle"
        triangle = getTriangle(100, 100, 100, self.myPen, self.myBrush)
        self.scene.addItem(triangle)
    def draw_polygon(self):
        print "Drawing Polygon"
    def draw_ellipse(self):
        print "Drawing Ellipse"
    def draw_rect(self):
        print "Drawing Rectangle"
        rectItem = getRectangle(50, 100, self.myPen, self.myBrush)
        #rectItem = QtGui.QGraphicsRectItem(0,0, 50, 100)
        #rectItem.setBrush(self.myBrush)
        #rectItem.setPen(self.myPen)
        self.scene.addItem(rectItem)
        
    def draw_line(self):
        print "Drawing Line"
        line = getLine(100, self.myPen, self.myBrush)
        self.scene.addItem(line)
    def find(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Cut Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.copyAvailable:
                pass
    def print_file(self):
        print "printing"
    def cut(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Cut Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.copyAvailable:
                self.textEdit.cut()
    def copy(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Copy Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.textEdit.copyAvailable:
                self.textEdit.copy()
    def paste(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Paste Map"
        elif self.tabWidget.currentWidget() == self.Scripts:
            self.textEdit.paste()
    def select_all(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            print "Select all Map"
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
    def delete_item(self):
        print "Delete item"
        for item in self.scene.selectedItems():
            self.scene.removeItem(item)
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
    def evaluate_map(self):
        print "Evaluating Map"
    def excute_map(self):
        print "Excuting Map"
    def upload_map(self):
        print "Uploading Map"
    def build_map(self):
        print "Building Map"
    def draw_tab_font_creator(self):
        self.fontCombo = QtGui.QFontComboBox()
        self.fontCombo.currentFontChanged.connect(self.current_font_changed)
        
        self.fontSizeCombo = QtGui.QComboBox()
        self.fontSizeCombo.setEditable(True)
        for i in range(6, 50, 2):
            self.fontSizeCombo.addItem(str(i))
        validator = QtGui.QIntValidator(2, 64, self)
        self.fontSizeCombo.setValidator(validator)
        self.fontSizeCombo.currentIndexChanged.connect(self.font_size_changed)

        self.fontColorToolButton = QtGui.QToolButton()
        self.fontColorToolButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.fontColorToolButton.setMenu(
            self.create_color_menu(self.text_color_changed, QtCore.Qt.black)
            )
        self.textAction = self.fontColorToolButton.menu().defaultAction()
        self.fontColorToolButton.setIcon(
            self.create_color_tool_button_icon('textpointer.png', QtCore.Qt.black)
            )
        self.fontColorToolButton.setAutoFillBackground(True)
        self.fontColorToolButton.clicked.connect(self.text_button_triggered)

        self.fillColorToolButton = QtGui.QToolButton()
        self.fillColorToolButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.fillColorToolButton.setMenu(
                self.create_color_menu(self.item_color_changed, QtCore.Qt.white))
        self.fillAction = self.fillColorToolButton.menu().defaultAction()
        self.fillColorToolButton.setIcon(
                self.create_color_tool_button_icon('floodfill.png',
                        QtCore.Qt.white))
        self.fillColorToolButton.clicked.connect(self.fill_button_triggered)
        
        self.lineColorToolButton = QtGui.QToolButton()
        self.lineColorToolButton.setPopupMode(QtGui.QToolButton.MenuButtonPopup)
        self.lineColorToolButton.setMenu(
            self.create_color_menu(self.line_color_changed, QtCore.Qt.black)
            )
        self.lineAction = self.lineColorToolButton.menu().defaultAction()
        self.lineColorToolButton.setIcon(
            self.create_color_tool_button_icon("linecolor.png", QtCore.Qt.black)
            )
        self.lineColorToolButton.clicked.connect(self.line_button_triggered)

        self.sendToFrontAction = QtGui.QAction(
                QtGui.QIcon('bringtofront.png'), "Bring to Front",
                self, shortcut="Ctrl+]", statusTip="Bring Object to front",
                triggered=self.bring_to_front)

        self.sendToBackAction = QtGui.QAction(
                QtGui.QIcon('sendtoback.png'), "Send to Back", self,
                shortcut="Ctrl+[", statusTip="Send Object to back",
                triggered=self.send_to_back)

        
        self.deleteAction = QtGui.QAction(QtGui.QIcon('delete.png'),
                "Delete", self, shortcut="Delete",
                statusTip="Delete item from map",
                triggered=self.delete_item)

        self.exitAction = QtGui.QAction("Exit", self, statusTip="Quit", triggered=self.close_application)

        self.boldAction = QtGui.QAction(QtGui.QIcon('bold.png'),
                "Bold", self, checkable=True, shortcut="Ctrl+B",
                triggered=self.handle_font_change)

        self.italicAction = QtGui.QAction(QtGui.QIcon('italic.png'),
                "Italic", self, checkable=True, shortcut="Ctrl+I",
                triggered=self.handle_font_change)

        self.underlineAction = QtGui.QAction(
                QtGui.QIcon('underline.png'), "Underline", self,
                checkable=True, shortcut="Ctrl+U",
                triggered=self.handle_font_change)
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
