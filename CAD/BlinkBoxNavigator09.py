from BlinkBoxNavigator_Header import _fromUtf8, _translate
from BlinkBoxNavigator_Header import*

class MapScene(QtGui.QGraphicsScene):
    def __init__(self, parent=None, mouseMoveEventHandler=None, mouseClickEventHandler=None, mouseReleaseEventHandler=None, mouseDragEventHandler=None):
        super(MapScene, self).__init__(parent)
        self._mouseMoveEventHandler = mouseMoveEventHandler
        self._mouseClickEventHandler = mouseClickEventHandler
        self._mouseReleaseEventHandler = mouseReleaseEventHandler
        self._mouseDragEventHandler = mouseDragEventHandler
    def wheelEvent(self, wheelEvent):
        #print "wheelEvent =",dir(wheelEvent)
        #p = QtGui.QGraphicsSceneWheelEvent()
        #print "p=",p.delta()
        #print "p=",p
        pass
    def mouseMoveEvent(self, mouseEvent):
        #print "event =",mouseEvent.scenePos()
        self._mouseMoveEventHandler(mouseEvent)
        
        super(MapScene, self).mouseMoveEvent(mouseEvent)
    def mousePressEvent(self, clickEvent):
        self._mouseClickEventHandler(clickEvent)
        super(MapScene, self).mousePressEvent(clickEvent)
    def mouseReleaseEvent(self, releaseEvent):
        self._mouseReleaseEventHandler(releaseEvent)
        super(MapScene, self).mouseReleaseEvent(releaseEvent)
    def mouseDragEvent(self, dragEvent):
        self._mouseDragEventHandler(dragEvent)
        super(MapScene, self).mouseDragEvent(dragEvent)
        
class Ui_Blink_Box_v12(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_Blink_Box_v12, self).__init__()
        self.setObjectName(_fromUtf8("Blink_Box_v12"))
        self.resize(1468, 902)
        self.setMinimumSize(QtCore.QSize(1500, 1000))
        self.setWindowIcon(QtGui.QIcon("logo01.png"))
        QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Plastique"))

        self.mapWidth = 0
        self.mapHeight = 0
        self.scene_mouse_x = 0
        self.scene_mouse_y = 0
        self.scene_object_x = 0
        self.scene_object_y = 0
        self.route = []
        self.drawing_polygon_status = False
        self.draw_polygon_buffer = {}
        self.mainMapRect = None
        self.previous_zoom_factor = None
        self.bluetooth_comPort = "COM15"
        self.bluetooth_baudrate = 9600
        self.bluetooth_connected = False
        self.bluetooth_connectedDevices = [0]
        self.deleted_items = []
        self.current_selected_item = None
        self.previous_selected_item = None
        self.current_selected_item_stroke_properties = None
        self.bluetooth_message_file_name = None
        self.map_file_name = None

        self.selected_stroke_1_type = QtGui.QPen()
        self.selected_stroke_1_type.setColor(QtCore.Qt.white)
        self.selected_stroke_1_type.setWidth(3)
        self.selected_stroke_1_type.setStyle(QtCore.Qt.DashLine)

        self.selected_stroke_2_type = QtGui.QPen()
        self.selected_stroke_2_type.setColor(QtCore.Qt.black)
        self.selected_stroke_2_type.setWidth(3)
        self.selected_stroke_2_type.setStyle(QtCore.Qt.DashLine)
        
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

        self.setup_scene_and_graphics_view()

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

        self.pathPlanningSelectionMenu = QtGui.QMenu()
        self.pathPlanningSelectionMenu.setObjectName(_fromUtf8("pathPlanningSelectionMenu"))

        self.rightClickSelectionMenu = QtGui.QMenu()
        self.rightClickSelectionMenu.setObjectName(_fromUtf8("rightClickSelectionMenu"))
        
        self.setMenuBar(self.menubar)
        
        self.statusbar = QtGui.QStatusBar(self)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        
        self.setStatusBar(self.statusbar)

        self.progressbar = QtGui.QProgressBar()
        self.progressbar.setGeometry(800, 500, 250, 50)
        self.progressbar.setHidden(True)
        
        self.setup_toolbar()
        self.setup_menubar()
        self.setup_shapes_toolbar()
        self.setup_stroke()
        self.setup_fill()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(300)
        self.timer.timeout.connect(self.timer_event)
        self.timer.start()

        self.setup_map()
        self.show()
    def setup_toolbar(self):
        
        buildAction = QtGui.QAction(QtGui.QIcon('buildSign01.png'), "Build Map", self)
        buildAction.triggered.connect(self.build_map)
        buildAction.setStatusTip("Build Map  F5")
        buildAction.setShortcut("F5")

        uploadAction = QtGui.QAction(QtGui.QIcon('uploadButton01.png'), "Upload Map", self)
        uploadAction.triggered.connect(self.upload_map)
        uploadAction.setStatusTip("Upload Map  Ctrl+U")
        uploadAction.setShortcut("Ctrl+U")

        self.excuteAction = QtGui.QAction(QtGui.QIcon('excuteButton01.png'), "Excute Map", self)
        self.excuteAction.setData(0)
        self.excuteAction.triggered.connect(self.excute_map)
        self.excuteAction.setStatusTip("Excute Map  Ctrl+R")
        self.excuteAction.setShortcut("Ctrl+R")

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
        self.mainToolBar.addAction(self.excuteAction)
        self.mainToolBar.addSeparator()
        self.mainToolBar.addAction(evaluateAction)
        
        self.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        
        #self.statusToolBar = QtGui.QToolBar(self)
        #self.statusToolBar.setObjectName(_fromUtf8("statusToolBar"))
        
        #self.addToolBar(QtCore.Qt.BottomToolBarArea, self.statusToolBar)
    def setup_menubar(self):
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

    def setup_map(self):
        self.mapWidth = QtGui.QInputDialog.getInteger(self,
                        "Map Properties", "Map Width", 2000, 0, 5000)#[2000, True]
        self.mapHeight =QtGui.QInputDialog.getInteger(self,
                        "Map Properties", "Map Height", 2000, 0, 5000)#[2000, True]# 
        if self.mapWidth[1] and self.mapHeight[1]:
            self.mapWidth = int(self.mapWidth[0])
            self.mapHeight = int(self.mapHeight[0])
            #self.graphicsView.setSceneRect(-20, -20, 5000+20, 5000+20)
            self.scene.setSceneRect(0, 0, self.mapWidth+20, self.mapHeight+20)
            self.scene.addRect(0, 0, self.mapWidth, self.mapHeight, QtGui.QColor(200, 0, 0), QtGui.QColor(255, 255, 255))
            self.mainMapRect = self.graphicsView.items()[0]
            #self.graphicsView.ensureVisible(-20, -20, 5000+30, 5000+30, 20, 20)
            self.graphicsView.centerOn(self.mainMapRect)
            #self.graphicsView.setTransformationAnchor(self.mainMapRect)
        else:
            self.mapWidth = 1000
            self.mapHeight = 1000
        
    def setup_scene_and_graphics_view(self):
        myPen = QtGui.QPen()
        myPen.setColor(QtCore.Qt.green)
        myPen.setWidth(10)

        myBrush = QtGui.QBrush()
        myBrush.setColor(QtCore.Qt.black)
        myBrush.setStyle(QtCore.Qt.SolidPattern)
        
        self.scene = MapScene(mouseMoveEventHandler = self.update_mouse_position,
                              mouseClickEventHandler = self.mouse_pressed_event,
                              mouseReleaseEventHandler = self.mouse_released_event,
                              mouseDragEventHandler = self.mouse_drag_event)
        self.scene.setBackgroundBrush(QtGui.QBrush(QtGui.QPixmap('background3.png')))
        self.scene.selectionChanged.connect(self.scene_selection_changed)

        self.graphicsView = QtGui.QGraphicsView(self.scene)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setMaximumSize(1900, 430)
        self.graphicsView.setMinimumHeight(420)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.mapVerticalLayout.addWidget(self.graphicsView)
        
    def setup_shapes_toolbar(self):
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

        self.actionForwardDistance = QtGui.QAction(self)
        self.actionForwardDistance.setObjectName(_fromUtf8("actionForwardDistance"))
        self.pathPlanningSelectionMenu.addAction(self.actionForwardDistance)
        self.pathButton.setMenu(self.pathPlanningSelectionMenu)
        
        #self.bottom_widget_creator()
        
        self.retranslateUi()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)
        
        
    def retranslateUi(self):
        self.setWindowTitle(_translate("Blink_Box_v12", "Blink Box Navigator v12", None))
        self.cancelButton.setText(_translate("Form", "Cancel", None))
        self.OkButton.setText(_translate("Form", "Ok", None))
        self.radiusLabel.setText(_translate("Form", "Radius", None))
        self.widthLabel.setText(_translate("Form", "Width", None))
        self.StrokeTypeLabel.setText(_translate("Form", "Stroke Type", None))
        self.xPositionLabel.setText(_translate("Form", "Object X", None))
        self.yPositionLabel.setText(_translate("Form", "Object Y", None))
        #self.LockObjectTypeLabel.setText(_translate("Form", "Lock Object", None))
        self.RotationTypeLabel.setText(_translate("Form", "Rotation", None))
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

        self.actionForwardDistance.setText(_translate("Blink_Box_v12", "Add Forward Distance Path", None))
        #self.actionForwardDistance.setShortcut("")
        self.actionForwardDistance.setStatusTip("Click to add a forward distance route")
        self.actionForwardDistance.triggered.connect(self.add_forward_distance_route)
        self.actionForwardDistance.setIcon(QtGui.QIcon('forwardDistance01.png'))
        
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
        self.actionSave_as.setShortcut("Shift+Ctrl+S")
        self.actionSave_as.setStatusTip("Save Current Tab As")
        self.actionSave_as.triggered.connect(self.save_current_tab_as)
        
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
        
    def bottom_widget_creator(self):
        self.objectOptionsTabWidth = QtGui.QTabWidget()
        self.objectOptionsTabWidth.setGeometry(QtCore.QRect(10, 0, 1200, 290))
        self.objectOptionsTabWidth.setTabsClosable(False)
        self.objectOptionsTabWidth.setMovable(True)
        self.objectOptionsTabWidth.setObjectName(_fromUtf8("objectOptionsTabWidth"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.widget = QtGui.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(0, 1, 1200, 280))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.cancelButton = QtGui.QPushButton(self.widget)
        self.cancelButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.clicked.connect(self.cancel_button_clicked)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.gridLayout.addWidget(self.cancelButton, 10, 3, 1, 1)
        self.OkButton = QtGui.QPushButton(self.widget)
        self.OkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.OkButton.clicked.connect(self.ok_button_clicked)
        self.OkButton.setObjectName(_fromUtf8("OkButton"))
        self.gridLayout.addWidget(self.OkButton, 10, 2, 1, 1)
        self.zoomHorizontalSlider = QtGui.QSlider(self.widget)
        self.zoomHorizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.zoomHorizontalSlider.setObjectName(_fromUtf8("zoomHorizontalSlider"))
        self.zoomHorizontalSlider.setTickInterval(1)
        self.zoomHorizontalSlider.setTickPosition(self.zoomHorizontalSlider.TicksBothSides)
        self.zoomHorizontalSlider.setMinimum(1)
        self.zoomHorizontalSlider.setMaximum(10)
        self.zoomHorizontalSlider.valueChanged.connect(self.set_qview_zoom)
        self.gridLayout.addWidget(self.zoomHorizontalSlider, 9, 1, 1, 3)
        self.strokeWidthSpinBox = QtGui.QSpinBox(self.widget)
        self.strokeWidthSpinBox.setObjectName(_fromUtf8("strokeWidthSpinBox"))
        self.strokeWidthSpinBox.setMinimum(0)
        self.strokeWidthSpinBox.setMaximum(50)
        self.strokeWidthSpinBox.valueChanged.connect(self.set_stroke_width)
        self.gridLayout.addWidget(self.strokeWidthSpinBox, 1, 3, 1, 1)

        self.rotationSpinBox = QtGui.QSpinBox(self.widget)
        self.rotationSpinBox.setObjectName(_fromUtf8("rotationSpinBox"))
        self.rotationSpinBox.setMinimum(-360)
        self.rotationSpinBox.setMaximum(360)
        self.rotationSpinBox.setValue(0)
        self.rotationSpinBox.valueChanged.connect(self.update_items_rotation)
        self.gridLayout.addWidget(self.rotationSpinBox, 4, 5, 1, 1)
        
        self.radiusLabel = QtGui.QLabel(self.widget)
        self.radiusLabel.setObjectName(_fromUtf8("radiusLabel"))
        self.radiusLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.radiusLabel, 3, 0, 1, 1)
        self.widthLabel = QtGui.QLabel(self.widget)
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.widthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.widthLabel, 1, 0, 1, 1)
        self.StrokeTypeLabel = QtGui.QLabel(self.widget)
        self.StrokeTypeLabel.setObjectName(_fromUtf8("StrokeTypeLabel"))
        self.StrokeTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.StrokeTypeLabel, 2, 2, 1, 1)
        self.xPositionLabel = QtGui.QLabel(self.widget)
        self.xPositionLabel.setObjectName(_fromUtf8("xPositionLabel"))
        self.xPositionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.xPositionLabel, 3, 2, 1, 1)
        self.xPositionSpinBox = QtGui.QSpinBox(self.widget)
        self.xPositionSpinBox.setObjectName(_fromUtf8("xPositionSpinBox"))
        self.xPositionSpinBox.setMinimum(-45000)
        self.xPositionSpinBox.setMaximum(45000)
        self.xPositionSpinBox.setValue(0)
        self.xPositionSpinBox.valueChanged.connect(self.x_object_value_changed)
        self.gridLayout.addWidget(self.xPositionSpinBox, 3, 3, 1, 1)
        self.yPositionSpinBox = QtGui.QSpinBox(self.widget)
        self.yPositionSpinBox.setObjectName(_fromUtf8("yPositionSpinBox"))
        self.yPositionSpinBox.setMinimum(-45000)
        self.yPositionSpinBox.setMaximum(45000)
        self.yPositionSpinBox.setValue(0)
        self.yPositionSpinBox.valueChanged.connect(self.y_object_value_changed)
        self.gridLayout.addWidget(self.yPositionSpinBox, 4, 3, 1, 1)
        self.strokeTypeComboBox = QtGui.QComboBox(self.widget)
        self.strokeTypeComboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.strokeTypeComboBox.addItem(QtGui.QIcon("lineStyle01.png"), "No Pen")
        self.strokeTypeComboBox.addItem(QtGui.QIcon("lineStyle01.png"), "Solid")
        self.strokeTypeComboBox.addItem(QtGui.QIcon("lineStyle02.png"), "Dash")
        self.strokeTypeComboBox.addItem(QtGui.QIcon("lineStyle03.png"), "Dot")
        self.strokeTypeComboBox.addItem(QtGui.QIcon("lineStyle04.png"), "Dash Dot")
        self.strokeTypeComboBox.addItem(QtGui.QIcon("lineStyle05.png"), "Dash DotDot")
        self.strokeTypeComboBox.currentIndexChanged.connect(self.set_stroke_type)
        
        self.strokeTypeComboBox.setObjectName(_fromUtf8("strokeTypeComboBox"))
        self.gridLayout.addWidget(self.strokeTypeComboBox, 2, 3, 1, 1)

        self.lockObjectCheckbox = QtGui.QCheckBox()
        self.lockObjectCheckbox.setObjectName(_fromUtf8("LockObjectCheckbox"))
        #self.lockObjectCheckbox.setText("Lock Object")
        self.lockObjectCheckbox.setIcon(QtGui.QIcon("lockObject01.png"))
        self.lockObjectCheckbox.stateChanged.connect(self.update_object_lock_properties)
        self.lockObjectCheckbox.setStatusTip("Lock or Unlock Object")
        self.gridLayout.addWidget(self.lockObjectCheckbox, 2, 4, 1, 1)
        
        #self.LockObjectTypeLabel = QtGui.QLabel(self.widget)
        #self.LockObjectTypeLabel.setObjectName(_fromUtf8("LockObjectTypeLabel"))
        #self.LockObjectTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        #self.gridLayout.addWidget(self.LockObjectTypeLabel, 2, 4, 1, 1)
        
        self.yPositionLabel = QtGui.QLabel(self.widget)
        self.yPositionLabel.setObjectName(_fromUtf8("yPositionLabel"))
        self.yPositionLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.yPositionLabel, 4, 2, 1, 1)
        
        self.RotationTypeLabel = QtGui.QLabel(self.widget)
        self.RotationTypeLabel.setObjectName(_fromUtf8("RotationTypeLabel"))
        self.RotationTypeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.RotationTypeLabel, 4, 4, 1, 1)

        self.strokeWidthLabel = QtGui.QLabel(self.widget)
        self.strokeWidthLabel.setObjectName(_fromUtf8("strokeWidthLabel"))
        self.strokeWidthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.strokeWidthLabel, 1, 2, 1, 1)
        self.lengthEntry = QtGui.QLineEdit(self.widget)
        self.lengthEntry.setMaxLength(50000)
        self.lengthEntry.setObjectName(_fromUtf8("lengthEntry"))
        self.lengthEntry.setText("50")
        self.lengthEntry.editingFinished.connect(self.length_changed)
        self.gridLayout.addWidget(self.lengthEntry, 4, 1, 1, 1)
        self.widthEntry = QtGui.QLineEdit(self.widget)
        self.widthEntry.setMaxLength(50000)
        self.widthEntry.setObjectName(_fromUtf8("widthEntry"))
        self.widthEntry.setText("50")
        self.widthEntry.editingFinished.connect(self.width_changed)
        self.gridLayout.addWidget(self.widthEntry, 1, 1, 1, 1)
        self.heightLabel = QtGui.QLabel(self.widget)
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.heightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.heightLabel, 2, 0, 1, 1)
        self.zoomLabel = QtGui.QLabel(self.widget)
        self.zoomLabel.setObjectName(_fromUtf8("zoomLabel"))
        self.zoomLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.zoomLabel, 9, 0, 1, 1)
        self.heightEntry = QtGui.QLineEdit(self.widget)
        self.heightEntry.setMaxLength(50000)
        self.heightEntry.setText("50")
        self.heightEntry.setObjectName(_fromUtf8("heightEntry"))
        self.heightEntry.editingFinished.connect(self.height_changed)
        self.gridLayout.addWidget(self.heightEntry, 2, 1, 1, 1)
        self.lengthLabel = QtGui.QLabel(self.widget)
        self.lengthLabel.setObjectName(_fromUtf8("lengthLabel"))
        self.lengthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.gridLayout.addWidget(self.lengthLabel, 4, 0, 1, 1)
        self.radiusEntry = QtGui.QLineEdit(self.widget)
        self.radiusEntry.setMaxLength(50000)
        self.radiusEntry.setObjectName(_fromUtf8("radiusEntry"))
        self.radiusEntry.setText("50")
        self.radiusEntry.editingFinished.connect(self.radius_changed)
        self.gridLayout.addWidget(self.radiusEntry, 3, 1, 1, 1)
        
        self.selectStrokeColorButton = QtGui.QPushButton(self.widget)
        self.selectStrokeColorButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        #self.selectStrokeColorButton.clicked.connect(self.select_Stroke_Color)
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
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 1, 1200, 280))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        
        self.sendButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.sendButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.sendButton.clicked.connect(self.send_bluetooth_message)
        self.sendButton.setObjectName(_fromUtf8("sendButton"))
        self.verticalLayout_2.addWidget(self.sendButton)
        
        self.readAllButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.readAllButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.readAllButton.clicked.connect(self.read_all_bluetooth_incoming_message)
        self.readAllButton.setObjectName(_fromUtf8("readAllButton"))
        self.verticalLayout_2.addWidget(self.readAllButton)
        
        self.save2FileButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.save2FileButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save2FileButton.clicked.connect(self.save_bluetooth_buffer_2_file)
        self.save2FileButton.setObjectName(_fromUtf8("save2FileButton"))
        self.verticalLayout_2.addWidget(self.save2FileButton)
        
        self.clearButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.clearButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearButton.clicked.connect(self.clear_bluetooth_receive_buffer)
        self.clearButton.setObjectName(_fromUtf8("clearButton"))
        self.verticalLayout_2.addWidget(self.clearButton)
        
        self.connectButton = QtGui.QPushButton(self.gridLayoutWidget_2)
        self.connectButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.connectButton.clicked.connect(self.connect_2_bluetooth_device)
        self.connectButton.setObjectName(_fromUtf8("connectButton"))
        
        self.verticalLayout_2.addWidget(self.connectButton)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.serialMessageEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.serialMessageEntry.setMaxLength(1000)#maximum bluetooth transfer characters
        self.serialMessageEntry.setObjectName(_fromUtf8("serialMessageEntry"))
        self.serialMessageEntry.editingFinished.connect(self.send_bluetooth_message)
        self.verticalLayout_3.addWidget(self.serialMessageEntry)
        self.serialMessageDisplay = QtGui.QPlainTextEdit(self.gridLayoutWidget_2)
        #self.serialMessageDisplay.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.serialMessageDisplay.setFrameShadow(QtGui.QFrame.Plain)
        self.serialMessageDisplay.setReadOnly(True)
        self.serialMessageDisplay.setObjectName(_fromUtf8("serialMessageDisplay"))
        self.verticalLayout_3.addWidget(self.serialMessageDisplay)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        
        self.serialPortEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.serialPortEntry.setMaxLength(6)
        self.serialPortEntry.textChanged.connect(self.set_com_port)
        self.serialPortEntry.setText(self.bluetooth_comPort)
        self.serialPortEntry.setObjectName(_fromUtf8("serialPortEntry"))
        self.gridLayout_2.addWidget(self.serialPortEntry, 1, 1, 1, 1)
        self.baudrateEntry = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.baudrateEntry.setMaxLength(200000)
        self.baudrateEntry.textChanged.connect(self.set_baudrate)
        self.baudrateEntry.setText(str(self.bluetooth_baudrate))
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
    def display_popup_menu(self,pos):
        if self.current_selected_item == None:
            pass
        elif isinstance(self.current_selected_item, QtGui.QGraphicsLineItem):
            tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
            if "ItemIsPolygon***" in tagData:
                pass
            else:
                self.rightClickSelectionMenu.clear()

                actionSendToBack = QtGui.QAction(self)
                actionSendToBack.setObjectName(_fromUtf8("actionSendToBack"))
                actionSendToBack.setText(_translate("Blink_Box_v12", "Send to Back", None))
                #actionSendToBack.setShortcut("")
                actionSendToBack.setStatusTip("Send item to back")
                actionSendToBack.triggered.connect(self.send_to_back)
                #actionSendToBack.setIcon(QtGui.QIcon('shapesRectButton01.png'))

                actionBringToFront = QtGui.QAction(self)
                actionBringToFront.setObjectName(_fromUtf8("actionBringToFront"))
                actionBringToFront.setText(_translate("Blink_Box_v12", "Bring to Front", None))
                #actionBringToFront.setShortcut("")
                actionBringToFront.setStatusTip("Bring item to front")
                actionBringToFront.triggered.connect(self.bring_to_front)
                #actionBringToFront.setIcon(QtGui.QIcon('shapesRectButton01.png'))

                actionSetPosition = QtGui.QAction(self)
                actionSetPosition.setObjectName(_fromUtf8("actionSetPosition"))
                actionSetPosition.setText(_translate("Blink_Box_v12", "Set Position", None))
                #actionSetPosition.setShortcut("")
                actionSetPosition.setStatusTip("Set line's position")
                actionSetPosition.triggered.connect(self.set_position)
                #actionSetPosition.setIcon(QtGui.QIcon('shapesRectButton01.png'))
                
                actionSetLength = QtGui.QAction(self)
                actionSetLength.setObjectName(_fromUtf8("actionSetLength"))
                actionSetLength.setText(_translate("Blink_Box_v12", "Set Length", None))
                #actionSetLength.setShortcut("")
                actionSetLength.setStatusTip("Set line's length")
                actionSetLength.triggered.connect(self.set_length)
                #actionSetLength.setIcon(QtGui.QIcon('shapesRectButton01.png'))
                
                actionSetRotation = QtGui.QAction(self)
                actionSetRotation.setObjectName(_fromUtf8("actionSetRotation"))
                actionSetRotation.setText(_translate("Blink_Box_v12", "Set Rotation", None))
                #actionSetRotation.setShortcut("")
                actionSetRotation.setStatusTip("Set line's rotation")
                actionSetRotation.triggered.connect(self.set_rotation)
                #actionSetRotation.setIcon(QtGui.QIcon('shapesRectButton01.png'))
                
                self.rightClickSelectionMenu.addAction(actionSendToBack)
                self.rightClickSelectionMenu.addAction(actionBringToFront)
                self.rightClickSelectionMenu.addSeparator()
                self.rightClickSelectionMenu.addAction(actionSetPosition)
                self.rightClickSelectionMenu.addAction(actionSetLength)
                self.rightClickSelectionMenu.addAction(actionSetRotation)
                self.rightClickSelectionMenu.popup(QtCore.QPoint(pos.x(), pos.y()))

                #self.draw_polgon_popup_menu((self.scene_mouse_x,self.scene_mouse_y))
        return
    def draw_polgon_popup_menu(self, pos):
        pass
    def timer_event(self):
        if self.bluetooth_connected == True:
            if int(self.bluetooth_connectedDevices[0].inWaiting()) > 0:
                try:
                    s = str(self.bluetooth_connectedDevices[0].readline())
                    if s.endswith("\n") or s.endswith("\r"):
                        s = s[0:len(s)-1]
                    elif s.endswith("\r\n") or s.endswith("\r\n"):
                        s = s[0:len(s)-2]
                    self.serialMessageDisplay.appendPlainText(s)
                except:
                    try:
                        self.bluetooth_connectedDevices[0].close()
                    except:
                        self.bluetooth_connectedDevices = []
                    finally:
                        self.display_warning("Bluetooth Connection", "Bluetooth Connection Has Been Disconnected")
            else:
                pass
        else:
            #self.serialMessageDisplay.appendPlainText("timer_out")
            pass
                
    def send_bluetooth_message(self):
        if self.bluetooth_connected == True:
            msg = str(self.serialMessageEntry.text())
            if msg:
                self.bluetooth_connectedDevices[0].write(msg)
                self.serialMessageEntry.clear()
        else:
            print "not connected msg =",str(self.serialMessageEntry.text())
    def send_bluetooth_message_message(self, msg):
        if self.bluetooth_connected == True:
            if msg:
                self.bluetooth_connectedDevices[0].write(msg)
                time.sleep(1.5)
        else:
            print "not connected msg =",str(self.serialMessageEntry.text())
    def read_all_bluetooth_incoming_message(self):
        print "read_all_bluetooth_incoming_message"
    def save_bluetooth_buffer_2_file(self):
        self.save_current_tab()
    def clear_bluetooth_receive_buffer(self):
        print "clear_bluetooth_receive_buffer"
        self.serialMessageDisplay.clear()
    def connect_2_bluetooth_device(self):
        if str(self.connectButton.text()).lower() == "connect":
            try:
                s = serial.Serial(port=str(self.bluetooth_comPort), baudrate=int(self.bluetooth_baudrate), timeout=3)
                self.bluetooth_connectedDevices.append(self.bluetooth_connectedDevices[0])
                self.bluetooth_connectedDevices[0] = s
                self.bluetooth_connected = True
                self.connectButton.setText(_translate("Form", "Disconnect", None))
            except:
                #print "Could not connect"
                self.display_warning("Bluetooth Connection", "Connection Failed")
        else:
            try:
                self.bluetooth_connectedDevices[0].close()
                self.bluetooth_connected = False
                self.connectButton.setText(_translate("Form", "Connect", None))
            except:
                self.display_warning("Bluetooth Connection", "Disconnection Failed")
    def mouse_pressed_event(self, event):
        self.scene_mouse_x,self.scene_mouse_y = event.scenePos().x(),event.scenePos().y()
        if event.button() == 2:
            self.display_popup_menu(event.screenPos())
        else:
            if self.drawing_polygon_status == True:
                self.xPositionSpinBox.setValue(self.scene_mouse_x)
                self.yPositionSpinBox.setValue(self.scene_mouse_y)
                self.current_selected_item.addPoint((self.scene_mouse_x, self.scene_mouse_y))
            elif self.current_selected_item == None:
                self.xPositionSpinBox.setValue(self.scene_mouse_x)
                self.yPositionSpinBox.setValue(self.scene_mouse_y)
            else:
                pass
    def mouse_released_event(self, event):
        print "onRelease"
        return
    def mouse_drag_event(self, event):
        print "onDrag"
        return
    def update_mouse_position(self, event):
        self.scene_mouse_x,self.scene_mouse_y = event.scenePos().x(),event.scenePos().y()
        if self.current_selected_item != None:
            self.xPositionSpinBox.setValue(self.scene_object_x)
            self.yPositionSpinBox.setValue(self.scene_object_y)
        #else:
        #    self.xPositionSpinBox.setValue(self.scene_mouse_x)
        #    self.yPositionSpinBox.setValue(self.scene_mouse_y)
    def scene_selection_changed(self):
        if self.scene.selectedItems() and self.drawing_polygon_status != True:
            if self.scene.selectedItems()[0] != self.current_selected_item:
                item = self.scene.selectedItems()[0]
                self.previous_selected_item = self.current_selected_item
                self.current_selected_item = item
                self.scene_object_x = item.x()
                self.scene_object_y = item.y()
                self.xPositionSpinBox.setValue(self.scene_object_x)
                self.yPositionSpinBox.setValue(self.scene_object_y)
                self.rotationSpinBox.setValue(item.rotation())
                if isinstance(item, QtGui.QGraphicsLineItem):
                    self.lengthEntry.setText(str( item.data(1).toInt()[0] ))
                elif isinstance(item, QtGui.QGraphicsRectItem):
                    self.widthEntry.setText(str( item.data(1).toList()[0].toInt()[0] ))
                    self.heightEntry.setText(str( item.data(1).toList()[1].toInt()[0] ))

                tagData = [i.toString() for i in item.data(0).toList()]
                if "ItemIsMovable" in tagData:
                    self.lockObjectCheckbox.setCheckState(0)
                else:
                    self.lockObjectCheckbox.setCheckState(2)
        elif self.drawing_polygon_status == True:
            pass
        else:
            self.previous_selected_item = self.current_selected_item
            self.current_selected_item = None
        self.update_item_selection()
        return
    def update_item_selection(self):
        if self.current_selected_item != None:
            if isinstance(self.current_selected_item, QtGui.QGraphicsLineItem):
                self.enable_stroke_properties()
                self.enable_length_properties()
                self.disable_width_height_properties()
                self.disable_radius_properties()
            elif isinstance(self.current_selected_item, QtGui.QGraphicsRectItem):
                self.enable_stroke_properties()
                self.disable_length_properties()
                self.enable_width_height_properties()
                self.disable_radius_properties()
        else:
            self.enable_stroke_properties()
            self.enable_width_height_properties()
            self.enable_radius_properties()
            self.enable_length_properties()
                
        #if self.previous_selected_item != None:
        #    self.previous_selected_item.setPen(self.current_selected_item_stroke_properties)
        #if self.current_selected_item != None:
        #    self.current_selected_item_stroke_properties = self.current_selected_item.pen()
        #    if self.current_selected_item_stroke_properties == self.selected_stroke_1_type:
        #        self.current_selected_item.setPen(self.selected_stroke_2_type)
        #    else:
        #        self.current_selected_item.setPen(self.selected_stroke_1_type)
    def x_object_value_changed(self):
        self.scene_object_x = self.xPositionSpinBox.value()
        if self.current_selected_item != None:
            self.current_selected_item.setX(self.scene_object_x)
        return
    def y_object_value_changed(self):
        self.scene_object_y = self.yPositionSpinBox.value()
        if self.current_selected_item != None:
            self.current_selected_item.setY(self.scene_object_y)
        return
    def update_object_lock_properties(self, state=''):
        if state == 0:
            self.lockObjectCheckbox.setIcon(QtGui.QIcon("lockObject01.png"))
            if self.current_selected_item != None:
                self.current_selected_item.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
                tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
                if "ItemIsMovable" in tagData:
                    return
                else:
                    tagData.append("ItemIsMovable")
                    self.current_selected_item.setData(0,tagData)
        elif state == 2:
            self.lockObjectCheckbox.setIcon(QtGui.QIcon("lockObject02.png"))
            if self.current_selected_item != None:
                self.current_selected_item.setFlag(QtGui.QGraphicsItem.ItemIsMovable, False)
                tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
                if "ItemIsMovable" in tagData:
                    tagData.remove("ItemIsMovable")
                    self.current_selected_item.setData(0,tagData)
                else:
                    return
                
    def set_qview_zoom(self, value):
        if self.current_selected_item != None:
            self.graphicsView.centerOn(self.current_selected_item)
        else:
            self.graphicsView.centerOn(self.mainMapRect)
        if self.previous_zoom_factor != None:
            if self.previous_zoom_factor > value:
                for i in range(self.previous_zoom_factor - value):
                    self.graphicsView.scale(1/1.25, 1/1.25)
                self.previous_zoom_factor = value
                return
            else:
                for i in range(value-self.previous_zoom_factor):
                    self.graphicsView.scale(1.25, 1.25)
                self.previous_zoom_factor = value
                return
        else:
            self.previous_zoom_factor = value
            for i in range(value):
                self.graphicsView.scale(1.25, 1.25)
            return
    def cancel_button_clicked(self):
        self.drawing_polygon_status = False
        if self.current_selected_item != None:
            self.previous_selected_item = self.current_selected_item
            self.current_selected_item = None
            self.scene.clearSelection()
            self.update_item_selection()
        else:
            print "Cancel button clicked"
    def ok_button_clicked(self):
        self.drawing_polygon_status = False
        if self.current_selected_item != None:
            self.previous_selected_item = self.current_selected_item
            self.current_selected_item = None
            self.scene.clearSelection()
            self.update_item_selection()
        else:
            print "Ok button clicked"
    def scroll_event_handler(self, event):
        print "scroll event =",event
    def setup_stroke(self):
        self.myPen = QtGui.QPen()
        self.myPen.setColor(QtCore.Qt.black)
        self.strokeWidthSpinBox.setValue(5)
        self.set_stroke_width()
    def set_stroke_width(self):
        self.myPen.setWidth(self.strokeWidthSpinBox.value())
        if self.current_selected_item != None:
            tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
            if "ItemIsPolygon" in tagData:
                self.current_selected_item.setPen(self.myPen)
            else:
                self.current_selected_item.setPen(self.myPen)
                self.current_selected_item_stroke_properties = self.myPen            
    def set_stroke_type(self, index):
        style = [QtCore.Qt.NoPen, QtCore.Qt.SolidLine, QtCore.Qt.DashLine, QtCore.Qt.DotLine, QtCore.Qt.DashDotLine , QtCore.Qt.DashDotDotLine]
        print "line_style =",index
        self.myPen.setStyle(style[index])
        if self.current_selected_item != None:
            tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
            if "ItemIsPolygon" in tagData:
                self.draw_polygon_buffer["polygon1"].setPen(self.myPen)
            else:
                self.current_selected_item.setPen(self.myPen)
                self.current_selected_item_stroke_properties = self.myPen   
   
    def width_changed(self):
        if self.current_selected_item != None:
            try:
                if isinstance(self.current_selected_item, QtGui.QGraphicsRectItem):
                    rotation = self.current_selected_item.rotation()
                    position = self.current_selected_item.scenePos()
                    self.current_selected_item.setRect(0,0, int(self.widthEntry.text()), int(self.heightEntry.text()))
                    self.current_selected_item.setPos(position)
                    self.current_selected_item.setRotation(rotation)
                    self.current_selected_item.setData(1, [int(self.widthEntry.text()), int(self.heightEntry.text())])
                else:
                    pass
            except:
                self.heightEntry.setText("10")
                self.widthEntry.setText("10")
                self.display_warning("Width Error", "Could not understand width")
    def length_changed(self):
        if self.current_selected_item != None:
            try:
                value = int(self.lengthEntry.text())
                if isinstance(self.current_selected_item, QtGui.QGraphicsLineItem):
                    tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
                    if "ItemIsPolygon" in tagData:
                        self.draw_polygon_buffer["polygon1"].adjust(self.current_selected_item, value, self.current_selected_item.rotation())
                    else:
                        rotation = self.current_selected_item.rotation()
                        position = self.current_selected_item.scenePos()
                        self.current_selected_item.setLine(0,0, value*cos(0), value*sin(0))
                        self.current_selected_item.setPos(position)
                        self.current_selected_item.setRotation(rotation)
                        self.current_selected_item.setData(1, int(self.lengthEntry.text()))
                else:
                    pass
            except:
                self.lengthEntry.setText("10")
                self.display_warning("Length Error", "Could not understand length")
    def set_length(self):
        print type(self.current_selected_item)
        if isinstance(self.current_selected_item, QtGui.QGraphicsLineItem):
            try:
                initialLength = int(self.lengthEntry.text())
            except:
                initialLength = 50
            length = QtGui.QInputDialog.getInteger(self,
                    "Set Line Length", "Line Length", initialLength, 0, 5000)
            tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
            if "ItemIsPolygon" in tagData:
                self.draw_polygon_buffer["polygon1"].adjust(self.current_selected_item, length, self.current_selected_item.rotation())
            elif length[1]:
                length = int(length[0])
                rotation = self.current_selected_item.rotation()
                position = self.current_selected_item.scenePos()
                self.current_selected_item.setLine(0,0, length*cos(0), length*sin(0))
                self.current_selected_item.setPos(position)
                self.current_selected_item.setRotation(rotation)
                self.current_selected_item.setData(1, length)
                self.lengthEntry.setText(str(length))
            else:
                pass
        else:
            pass
    def radius_changed(self):
        try:
            value = int(self.radiusEntry.text())
        except:
            self.display_warning("Radius Error", "Could not understand radius")
    def height_changed(self):
        if self.current_selected_item != None:
            try:
                if isinstance(self.current_selected_item, QtGui.QGraphicsRectItem):
                    rotation = self.current_selected_item.rotation()
                    position = self.current_selected_item.scenePos()
                    self.current_selected_item.setRect(0,0, int(self.widthEntry.text()), int(self.heightEntry.text()))
                    self.current_selected_item.setPos(position)
                    self.current_selected_item.setRotation(rotation)
                    self.current_selected_item.setData(1, [int(self.widthEntry.text()), int(self.heightEntry.text())])
                else:
                    pass
            except:
                self.heightEntry.setText("10")
                self.widthEntry.setText("10")
                self.display_error("Height Error", "Could not understand height")
    def update_items_rotation(self):
        if self.current_selected_item == None:
            return
        else:
            tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
            if "ItemIsPolygon" in tagData:
                pass
                #self.draw_polygon_buffer["polygon1"].adjust(self.current_selected_item, self.current_selected_item.data(1).toInt()[0], int(self.rotationSpinBox.value()))
            else:
                self.current_selected_item.setRotation(int(self.rotationSpinBox.value()))
    def set_rotation(self):
        if isinstance(self.current_selected_item, QtGui.QGraphicsLineItem):
            angle = QtGui.QInputDialog.getInteger(self,
                    "Set Line Rotation", "Rotation", self.current_selected_item.rotation(), 0, 360)
            if angle[1]:
                angle = float(angle[0])
                tagData = [i.toString() for i in self.current_selected_item.data(0).toList()]
                if "ItemIsPolygon" in tagData:
                    self.draw_polygon_buffer["polygon1"].adjust(self.current_selected_item, self.current_selected_item.data(1).toInt()[0], int(self.rotationSpinBox.value()))
                else:
                    self.current_selected_item.setRotation(angle)
                    self.rotationSpinBox.setValue(angle)
            else:
                pass
        else:
            pass
    def set_position(self):
        if self.current_selected_item == None:
            return
        else:
            pos = PositionDialog(self, self.current_selected_item.x(), self.current_selected_item.y(),
                                 self.mapWidth, self.mapHeight)
            pos.exec_()
            pos = pos.results
            if pos[1] == True:
                if isinstance(self.current_selected_item, QtGui.QGraphicsLineItem):
                    self.current_selected_item.setPos(QtCore.QPoint(pos[0][0], pos[0][1]))
                else:
                    pass
            else:
                pass
    def setup_fill(self):
        self.myBrush = QtGui.QBrush()
        self.myBrush.setStyle(QtCore.Qt.SolidPattern)
        self.myBrush.setColor(QtCore.Qt.black)
    def set_com_port(self):
        self.bluetooth_comPort = str(self.serialPortEntry.text())
        #print "com port =",self.bluetooth_comPort
    def set_baudrate(self):
        try:
            self.bluetooth_baudrate = int(self.baudrateEntry.text())
        except:
            print "Invalid Baudrate"
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
        if self.current_selected_item != None:
            self.current_selected_item.setBrush(self.myBrush)
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
        if self.current_selected_item != None:
            self.current_selected_item.setPen(self.myPen)
            self.current_selected_item_stroke_properties = self.myPen
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
        if self.current_selected_item == None:
            return
        selectedItem = self.current_selected_item
        overlapItems = selectedItem.collidingItems()

        zValue = 0
        for item in overlapItems:
            if item.zValue() >= zValue:
                zValue = item.zValue() + 0.1
        selectedItem.setZValue(zValue)
    def send_to_back(self):
        if self.current_selected_item == None:
            return

        selectedItem = self.current_selected_item
        overlapItems = selectedItem.collidingItems()

        zValue = 0
        for item in overlapItems:
            if item.zValue <= zValue:
                zValue = item.zValue() - 0.1
        selectedItem.setZValue(zValue)
    def delete_item(self):
        if self.current_selected_item == None:
            return
        self.deleted_items.append(self.current_selected_item)
        self.scene.removeItem(self.current_selected_item)
        self.current_selected_item = None
        self.update_item_selection()
        self.scene.clearSelection()
        
    def disable_stroke_properties(self):
        self.strokeWidthSpinBox.setDisabled(True)
        self.strokeTypeComboBox.setDisabled(True)
        self.selectStrokeColorButton.setDisabled(True)
    def enable_stroke_properties(self):
        self.strokeWidthSpinBox.setEnabled(True)
        self.strokeTypeComboBox.setEnabled(True)
        self.selectStrokeColorButton.setEnabled(True)

    def disable_width_height_properties(self):
        self.widthEntry.setDisabled(True)
        self.heightEntry.setDisabled(True)
    def enable_width_height_properties(self):
        self.widthEntry.setEnabled(True)
        self.heightEntry.setEnabled(True)

    def disable_radius_properties(self):
        self.radiusEntry.setDisabled(True)
    def enable_radius_properties(self):
        self.radiusEntry.setEnabled(True)

    def disable_length_properties(self):
        self.lengthEntry.setDisabled(True)
    def enable_length_properties(self):
        self.lengthEntry.setEnabled(True)
    
    def undo_delete(self):
        if self.deleted_items:
            self.scene.addItem(self.deleted_items(-1))
            self.deleted_items.pop()
        else:
            self.display_warning("Warning Undo Delete", "There is no deleted item")
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
    def add_forward_distance_route(self):
        print "fd50"
    def draw_path(self):
        print "Drawing Path"
    def draw_triangle(self):
        print "Drawing Triangle"
        triangle = getTriangle(100, 100, 100, self.myPen, self.myBrush)
        self.scene.addItem(triangle)
    def draw_polygon(self):
        print "Drawing Polygon"
        self.display_message("Polygon Tutorial", "Click different points on the scene to create a new polygon point."+
                                                  " Please click the Ok or Cancel button when done to exit draw Polygon Mode")
        if self.drawing_polygon_status == True:
            self.drawing_polygon_status = False
        else:
            self.drawing_polygon_status = True
            self.previous_selected_item = self.current_selected_item
            self.current_selected_item = PolygonObject(None, self.scene, pen=self.myPen, brush=self.myBrush)
            self.scene.clearSelection()
            self.update_item_selection()
            
    def complete_polgon(self):
        print "Polygon complete"
    def draw_ellipse(self):
        print "Drawing Ellipse"
    def draw_rect(self):
        print "Drawing Rectangle"
        try:
            rectItem = getRectangle(0, 0, int(self.widthEntry.text()), int(self.heightEntry.text()), self.myPen, self.myBrush)
            rectItem.setPos(self.scene_object_x, self.scene_object_y)
            rectItem.setRotation(int(self.rotationSpinBox.value()))
            self.scene.addItem(rectItem)
            #rectItem.setFocus()
        except:
            self.display_warning("Draw Rectangle Error", "Could not draw rectangle")
        
    def draw_line(self):
        line = getLine(0,0, int(self.lengthEntry.text()), self.myPen)
        line.setPos(self.scene_object_x, self.scene_object_y)
        line.setRotation(int(self.rotationSpinBox.value()))
        self.scene.addItem(line)
        #line.setFocus()
        
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
    def open_map_file(self):
        name = QtGui.QFileDialog.getOpenFileName(self, "Open File")
        if name:
            fileName = str(name)
            with open(name, 'r') as file:
                text = file.read()
                if fileName.endswith('.txt') or fileName.endswith('.bm_script'):
                    self.textEdit.setText(text)
                    self.map_file_name = name
                    self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scripts), _translate("Blink_Box_v12", "Scripts - "+fileName.split("/")[-1], None))
                elif fileName.endswith('.b_map'):
                    pass
                else:
                    print "invalid name"
                    self.display_warning("Warning !!!", "Invalid File")
        else:
            self.display_warning("Warning !!!", "Invalid Name")
    def display_message(self, title, info):
        QtGui.QMessageBox.about(self, title, info)
    def save_current_tab(self):
        if self.tabWidget.currentWidget() == self.mapTab:
            if self.bluetooth_message_file_name == None:
                self.save_current_tab_as()
                return
            file = open(self.bluetooth_message_file_name, 'w')
            text = self.serialMessageDisplay.toPlainText()
            file.write(text)
            file.close()
        elif self.tabWidget.currentWidget() == self.Scripts:
            if self.map_file_name == None:
                self.save_current_tab_as()
                return
            file = open(self.map_file_name, 'w')
            text = self.textEdit.toPlainText()
            file.write(text)
            file.close()
        else:
            print self.tabWidget.currentWidget()
    def save_current_tab_as(self):
        self.build_map()#ask permission to build and build
        if self.tabWidget.currentWidget() == self.mapTab:
            name = QtGui.QFileDialog.getSaveFileName(self, "Save File")
            if name:
                file = open(name, 'w')
                text = self.serialMessageDisplay.toPlainText()
                file.write(text)
                file.close()
                self.bluetooth_message_file_name = name
            else:
                return
        elif self.tabWidget.currentWidget() == self.Scripts:
            name = QtGui.QFileDialog.getSaveFileName(self, "Save File")
            if name:
                file = open(name, 'w')
                text = self.textEdit.toPlainText()
                file.write(text)
                file.close()
                self.map_file_name = name
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.Scripts), _translate("Blink_Box_v12", "Scripts - "+name.split("/")[-1], None))
            else:
                return
        else:
            print self.tabWidget.currentWidget()
    def evaluate_map(self):
        print "Evaluating Map"
    def excute_map(self):
        print "Excuting Map"
        if self.excuteAction.data().toInt()[0] == 1:
            self.excuteAction.setIcon(QtGui.QIcon('excuteButton01.png'))
            self.excuteAction.setData(0)
            self.send_bluetooth_message_message("tqe")
        else:
            self.excuteAction.setIcon(QtGui.QIcon("pauseIcon01.ico"))
            self.excuteAction.setData(1)
            self.send_bluetooth_message_message("tqe")
    def upload_map(self):
        print "Uploading Map"
        text = str(self.textEdit.toPlainText())
        print text
        p = text.split(',')
        p.insert(0, "iq")
        progressCounter = 0
        countLength = len(p)
        self.progressbar.setHidden(False)
        for i in p:
            self.send_bluetooth_message_message(i)
            progressCounter += 100/countLength
            self.progressbar.setValue(progressCounter)
        self.progressbar.setHidden(True)
        print p
    def build_map(self):
        print "Building Map"
        self.update_route()
    def update_route(self):
        #self.route.append()
        print "update_route"
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
                self.create_color_menu(self.item_color_changed, QtCore.Qt.black))
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
    def display_warning(self, title, text):
        choice = QtGui.QMessageBox.warning(self, title, text)
    def close_application(self):
        choice = QtGui.QMessageBox.question(self, "Close Window",
                                            "Do you want to exit?",
                                            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if choice == QtGui.QMessageBox.Yes:
            if self.bluetooth_connected:
                try:
                    self.bluetooth_connectedDevices[0].close()
                except:
                    print "Could not print"
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ui = Ui_Blink_Box_v12()
    sys.exit(app.exec_())





p = ['toBitArray', 'toBool', 'toByteArray', 'toChar', 'toDate', 'toDateTime', 'toDouble', 'toEasingCurve', 'toFloat', 'toHash', 'toInt',
     'toLine', 'toLineF', 'toList', 'toLocale', 'toLongLong', 'toMap', 'toPoint', 'toPointF','toPyObject', 'toReal', 'toRect', 'toRectF',
     'toRegExp', 'toSize', 'toSizeF', 'toString', 'toStringList', 'toTime', 'toUInt', 'toULongLong', 'toUrl']
