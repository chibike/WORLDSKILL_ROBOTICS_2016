import sys, serial, time, math, json, pyttsx
engine = pyttsx.init()
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig,
                                            _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

def getRectangle(x, y, width, height, pen, brush):
    rectItem = QtGui.QGraphicsRectItem()
    rectItem.setRect(x,y,width,height)
    rectItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    rectItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    rectItem.setVisible(True)
    rectItem.setData(0, ["ItemIsMovable", "ItemIsSelectable",
                         "ItemIsVisible"])
    rectItem.setData(1, [width, height]) 
    rectItem.setBrush(brush)
    rectItem.setPen(pen)
    return rectItem

def getLine(x1, y1, length, pen):
    lineItem = QtGui.QGraphicsLineItem()
    lineItem.setLine(x1, y1, x1+(length*cos(0)), y1+(length*sin(0)))
    lineItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    lineItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    lineItem.setVisible(True)
    lineItem.setData(0, ["ItemIsMovable", "ItemIsSelectable",
                         "ItemIsVisible"])
    lineItem.setData(1, length)
    lineItem.setPen(pen)
    return lineItem

def getForwardDistanceItem(length, pen, brush):
    polygonItem = QtGui.QGraphicsPolygonItem()
    polygonItem.setBrush(brush)
    polygonItem.setPen(QtGui.QPen(QtCore.Qt.black, 5, QtCore.Qt.SolidLine,
                QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
    path = QtGui.QPainterPath()
    path.moveTo(0, 0)
    path.lineTo(0, length)
    path.lineTo(-10, length-5)
    path.lineTo(10, length-5)
    path.lineTo(0, length)
    myPolygon = path.toFillPolygon()
    polygonItem.setPolygon(myPolygon)
    polygonItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    polygonItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    polygonItem.setVisible(True)
    polygonItem.setData(0, ["ItemIsMovable", "ItemIsSelectable",
                            "ItemIsVisible", "ItemIsForwardDistance"])
    return polygonItem

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

def sin(x):
    return math.sin(math.radians(x))

def asin(x):
    print "x=",x
    return math.degrees(math.asin(x))

def cos(x):
    return math.cos(math.radians(x))

def acos(x):
    print "x=",x
    return math.degrees(math.acos(x))

def tan(x):
    return math.tan(math.radians(x))

class PolygonObject():
    def __init__(self, scene=None, pen=None, brush=None):
        self._pen = pen
        self._brush = brush
        self._scene = scene
        self._points = []
        self._angles = []
        self._lengths = []
        self._quadrants = []
        self._item_ids = {}
        self._polygon = QtGui.QGraphicsPolygonItem()
        self._polygon.setBrush(self._brush)
        self._polygon.setPen(self._pen)
        self._polygon.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self._polygon.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    def addPoint(self, point):
        if len(self._points) < 1:
            self._points.append(point)
            return
        #prevent addition of equal succesive points
        if self._points[-1] != point:
            #print self._points[0],"vs",point
            if ( point[0] < self._points[0][0]+5 and point[0] > self._points[0][0]-5 ) and ( point[1] < self._points[0][1]+5 and point[1] > self._points[0][1]-5 ):
                self._points.append(self._points[0])#End the shape
            else:
                self._points.append((int(point[0]),int(point[1])))
                print "complete"
        else:
            return
        previousPoint = self._points[-2]
        dx = point[0]-previousPoint[0]
        dy = -1*( point[1]-previousPoint[1] )#mulitipy by -1 to convert the screen's coordinates to cartesian
        length = math.sqrt( pow(dx,2) + pow(dy,2) )
        angle = acos(abs(dx)/abs(length))
        p = self.getAlpha4Quadrant(dx, dy, angle)
        angle = p#because angle is clock wise
        self._angles.append(angle)
        self._lengths.append(length)
        self.update()
    def update(self):
        self.removeFromScene()
        if len(self._points) > 1:
            for i in range(len(self._points)-1):
                line = getLine(0,0, self._lengths[i], self._pen)
                line.setRotation(self._angles[i])
                line.setPos(self._points[i][0], self._points[i][1])
                line.setFlag(QtGui.QGraphicsItem.ItemIsMovable, False)
                line.setData(0, ["ItemIsPolygon", "ItemIsSelectable", "ItemIsVisible"])
                self._item_ids[line] = i
                self._scene.addItem(line)
        if len(self._points) >  2 and self._points[0] == self._points[-1]:
            points = []
            for i in self._points:
                points.append(QtCore.QPointF(i[0], i[1]))
            self.myPolygon = QtGui.QPolygonF(points)
            self._polygon.setPolygon(self.myPolygon)
            self._scene.addItem(self._polygon)
        
    def updatePoint(self):
        if len(self._points) > 1:
            if self._points[0] == self._points[-1]:
                p = self._points + self._points[0]
    def adjust(self, item, length, angle):
        print "length,angle =",(length,angle)
        item_id = self._item_ids[item]
        previous_points = self._points[item_id]
        dy = -1*( length * sin(angle) )
        dx = length * cos(angle)
        x2 = previous_points[0]+dx
        y2 = previous_points[1]-dy
        self._points[item_id+1] = (int(x2),int(y2))
        self._angles[item_id] = angle
        self._lengths[item_id] = length
        if len(self._points) > item_id+2:
            next_points = self._points[item_id+2]
            dx = next_points[0] - x2
            dy = -1*( next_points[1]-y2 )#mulitipy by -1 to convert the screen's coordinates to cartesian
            length = math.sqrt( pow(dx,2) + pow(dy,2) )
            angle = acos(abs(dx)/abs(length))
            p = self.getAlpha4Quadrant(dx, dy, angle)
            self._angles[item_id+1] = p
            self._lengths[item_id+1] = length
        self.update()
    def setPen(self, pen):
        self._pen = pen
        self.update()
    def setBrush(self, brush):
        self._brush = brush
        #self.updatePaint()
    def removeFromScene(self):
        for i in self._item_ids.keys():
            self._scene.removeItem(i)
        self._item_ids.clear()
        if self._polygon != None:
            self._scene.removeItem(self._polygon)
        return
    def getAlpha4Quadrant(self, dx, dy, angle):
        if dx > 0 and dy == 0:
            return 0
        elif dx > 0 and dy < 0:
            return angle
        elif dx == 0 and dy < 0:
            return 90
        elif dx < 0 and dy < 0:
            return 180 - angle
        elif dx < 0 and dy == 0:
            return 180
        elif dx < 0 and dy > 0:
            return 180+angle
        elif dx == 0 and dy > 0:
            return 270
        elif dx > 0 and dy > 0:
            return 360 - angle
        elif dx == 0 and dy == 0:
            return 0
        else:
            return 0
    def getQuadrant4Alpha(self, dx, dy, quadrant):
        if quadrant == 0:
            return [dx, 0]
        elif quadrant == 1:
            return [dx, -1*dy]
        elif quadrant == 2:
            return [0, -1*dy]
        elif quadrant == 3:
            return [-1*dx, -1*dy]
        elif quadrant == 4:
            return [-1*dx, 0]
        elif quadrant == 5:
            return [-1*dx, dy]
        elif quadrant == 6:
            return [0, dy]
        elif quadrant == 7:
            return [dx, dy]
        elif quadrant == 8:
            return [0, 0]
        else:
            return [0, 0]
    def calculateNewQuadrant(self, quadrant, angle):
        angle_quad = angle/90
        angle = angle/4 
        new_quad = quadrant + (2*angle_quad)
        if quadrant < 1 or quadrant > 8:
            return [0,0]
        elif new_quad == 0:
            return [0,0]
        elif new_quad == 1:
            return [1,0]
        elif new_quad == 2:
            return [2,0]
        elif new_quad == 3:
            return [3,0]
        elif new_quad == 4:
            return [4,0]
        elif new_quad == 5:
            return [5,0]
        elif new_quad == 6:
            return [6,0]
        elif new_quad == 7:
            return [7,0]
        elif new_quad == 8:
            return [8,0]
        elif new_quad == 9:
            return [0,0]
        elif new_quad == 10:
            return [1,0]
        elif new_quad == 11:
            return [2,0]
        elif new_quad == 12:
            return [3,0]
        

class PolygonItem(QtGui.QGraphicsPolygonItem):
    def __init__(self, parent=None, scene=None, pen=None, brush=None):
        super(PolygonItem, self).__init__(parent)
        self.setBrush(brush)
        self.setPen(pen)
        self._scene = scene
        self._points = []
        self._angles = []
        self._lengths = []
        self._quadrants = []
        self._item_ids = {}
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    def addPoint(self, point):
        if len(self._points) < 1:
            self._points.append(point)
            return
        #prevent addition of equal succesive points
        if self._points[-1] != point:
            #print self._points[0],"vs",point
            if ( point[0] < self._points[0][0]+5 and point[0] > self._points[0][0]-5 ) and ( point[1] < self._points[0][1]+5 and point[1] > self._points[0][1]-5 ):
                self._points.append(self._points[0])#End the shape
            else:
                self._points.append((int(point[0]),int(point[1])))
                print "complete"
        else:
            return
        previousPoint = self._points[-2]
        dx = point[0]-previousPoint[0]
        dy = -1*( point[1]-previousPoint[1] )#mulitipy by -1 to convert the screen's coordinates to cartesian
        length = math.sqrt( pow(dx,2) + pow(dy,2) )
        angle = acos(abs(dx)/abs(length))
        p = self.getAlpha4Quadrant(dx, dy, angle)
        angle = p#because angle is clock wise
        self._angles.append(angle)
        self._lengths.append(length)
        self.updatePolygon()
    def updatePolygon(self):
        self.removeFromScene()
        if len(self._points) > 1:
            for i in range(len(self._points)-1):
                line = getLine(0,0, self._lengths[i], self._pen)
                line.setRotation(self._angles[i])
                line.setPos(self._points[i][0], self._points[i][1])
                line.setFlag(QtGui.QGraphicsItem.ItemIsMovable, False)
                line.setData(0, ["ItemIsPolygon", "ItemIsSelectable", "ItemIsVisible"])
                self._item_ids[line] = i
                self._scene.addItem(line)
        if len(self._points) >  2 and self._points[0] == self._points[-1]:
            points = []
            for i in self._points:
                points.append(QtCore.QPointF(i[0], i[1]))
            polygon = QtGui.QPolygonF(points)
            self.setPolygon(polygon)
            self._scene.addItem(self)
    def updatePoint(self):
        if len(self._points) > 1:
            if self._points[0] == self._points[-1]:
                p = self._points + self._points[0]
    def adjust(self, item, length, angle):
        print "length,angle =",(length,angle)
        item_id = self._item_ids[item]
        previous_points = self._points[item_id]
        dy = -1*( length * sin(angle) )
        dx = length * cos(angle)
        x2 = previous_points[0]+dx
        y2 = previous_points[1]-dy
        self._points[item_id+1] = (int(x2),int(y2))
        self._angles[item_id] = angle
        self._lengths[item_id] = length
        if len(self._points) > item_id+2:
            next_points = self._points[item_id+2]
            dx = next_points[0] - x2
            dy = -1*( next_points[1]-y2 )#mulitipy by -1 to convert the screen's coordinates to cartesian
            length = math.sqrt( pow(dx,2) + pow(dy,2) )
            angle = acos(abs(dx)/abs(length))
            p = self.getAlpha4Quadrant(dx, dy, angle)
            self._angles[item_id+1] = p
            self._lengths[item_id+1] = length
        self.updatePolygon()
    def setPen(self, pen):
        self._pen = pen
        #self.updatePaint()
        super(PolygonItem, self).setPen(pen)
    def setBrush(self, brush):
        self._brush = brush
        #self.updatePaint()
        super(PolygonItem, self).setBrush(brush)
    def removeFromScene(self):
        for i in self._item_ids.keys():
            self._scene.removeItem(i)
        self._item_ids.clear()
        #if self._polygon != None:
        #    self._scene.removeItem(self._polygon)
        self._scene.removeItem(self)
        return
    def getAlpha4Quadrant(self, dx, dy, angle):
        if dx > 0 and dy == 0:
            return 0
        elif dx > 0 and dy < 0:
            return angle
        elif dx == 0 and dy < 0:
            return 90
        elif dx < 0 and dy < 0:
            return 180 - angle
        elif dx < 0 and dy == 0:
            return 180
        elif dx < 0 and dy > 0:
            return 180+angle
        elif dx == 0 and dy > 0:
            return 270
        elif dx > 0 and dy > 0:
            return 360 - angle
        elif dx == 0 and dy == 0:
            return 0
        else:
            return 0
    def getQuadrant4Alpha(self, dx, dy, quadrant):
        if quadrant == 0:
            return [dx, 0]
        elif quadrant == 1:
            return [dx, -1*dy]
        elif quadrant == 2:
            return [0, -1*dy]
        elif quadrant == 3:
            return [-1*dx, -1*dy]
        elif quadrant == 4:
            return [-1*dx, 0]
        elif quadrant == 5:
            return [-1*dx, dy]
        elif quadrant == 6:
            return [0, dy]
        elif quadrant == 7:
            return [dx, dy]
        elif quadrant == 8:
            return [0, 0]
        else:
            return [0, 0]
    def calculateNewQuadrant(self, quadrant, angle):
        angle_quad = angle/90
        angle = angle/4 
        new_quad = quadrant + (2*angle_quad)
        if quadrant < 1 or quadrant > 8:
            return [0,0]
        elif new_quad == 0:
            return [0,0]
        elif new_quad == 1:
            return [1,0]
        elif new_quad == 2:
            return [2,0]
        elif new_quad == 3:
            return [3,0]
        elif new_quad == 4:
            return [4,0]
        elif new_quad == 5:
            return [5,0]
        elif new_quad == 6:
            return [6,0]
        elif new_quad == 7:
            return [7,0]
        elif new_quad == 8:
            return [8,0]
        elif new_quad == 9:
            return [0,0]
        elif new_quad == 10:
            return [1,0]
        elif new_quad == 11:
            return [2,0]
        elif new_quad == 12:
            return [3,0]

class PositionDialog(QtGui.QDialog):
    results = [(0,0), False]
    def __init__(self, parent=None, x_initial_val=0, y_initial_value=0, x_max_value=5000, y_max_value=5000):
        super(PositionDialog, self).__init__(parent)
        self.x_val = x_initial_val
        self.y_val = y_initial_value
        self.x_min = 0
        self.y_min = 0
        self.x_max = x_max_value
        self.y_max = y_max_value
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName(_fromUtf8("PositionDialog"))
        self.resize(579, 111)
        self.setMinimumSize(QtCore.QSize(579, 111))
        self.setMaximumSize(QtCore.QSize(579, 111))
        self.gridLayoutWidget = QtGui.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 0, 541, 102))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.gridLayout.setVerticalSpacing(10)
        #self.gridLayout.setHorizontalSpacing(10)
        self.xPositionSpinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.xPositionSpinbox.setMinimumSize(QtCore.QSize(250, 27))
        self.xPositionSpinbox.setMaximumSize(QtCore.QSize(250, 27))
        self.xPositionSpinbox.setMinimum(self.x_min)
        self.xPositionSpinbox.setMaximum(self.x_max)
        self.xPositionSpinbox.setValue(self.x_val)
        self.xPositionSpinbox.setObjectName(_fromUtf8("xPositionSpinbox"))
        self.gridLayout.addWidget(self.xPositionSpinbox, 2, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setMinimumSize(QtCore.QSize(265, 21))
        self.label.setMaximumSize(QtCore.QSize(265, 21))
        self.label.setIndent(88)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.yPositionSpinbox = QtGui.QSpinBox(self.gridLayoutWidget)
        self.yPositionSpinbox.setMinimumSize(QtCore.QSize(250, 27))
        self.yPositionSpinbox.setMaximumSize(QtCore.QSize(250, 27))
        self.yPositionSpinbox.setMinimum(self.y_min)
        self.yPositionSpinbox.setMaximum(self.y_max)
        self.yPositionSpinbox.setValue(self.y_val)
        self.yPositionSpinbox.setObjectName(_fromUtf8("yPositionSpinbox"))
        self.gridLayout.addWidget(self.yPositionSpinbox, 2, 1, 1, 1)
        self.yPositionLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.yPositionLabel.setMinimumSize(QtCore.QSize(265, 21))
        self.yPositionLabel.setMaximumSize(QtCore.QSize(265, 21))
        self.yPositionLabel.setIndent(88)
        self.yPositionLabel.setObjectName(_fromUtf8("yPositionLabel"))
        self.gridLayout.addWidget(self.yPositionLabel, 1, 1, 1, 1)
        self.okButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.okButton.setMinimumSize(QtCore.QSize(250, 34))
        self.okButton.setMaximumSize(QtCore.QSize(250, 34))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.okButton.clicked.connect(self.ok)
        self.gridLayout.addWidget(self.okButton, 3, 0, 1, 1)
        self.cancelButton = QtGui.QPushButton(self.gridLayoutWidget)
        self.cancelButton.setMinimumSize(QtCore.QSize(250, 34))
        self.cancelButton.setMaximumSize(QtCore.QSize(250, 34))
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.cancelButton.clicked.connect(self.cancel)
        self.gridLayout.addWidget(self.cancelButton, 3, 1, 1, 1)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("PositionDialog", "Position Settings", None))
        self.xPositionSpinbox.setToolTip(_translate("PositionDialog", "Set object\'s x position", None))
        self.xPositionSpinbox.setStatusTip(_translate("PositionDialog", "Set object\'s x position", None))
        self.label.setText(_translate("PositionDialog", "X Position", None))
        self.yPositionSpinbox.setToolTip(_translate("PositionDialog", "Set object\'s y position", None))
        self.yPositionSpinbox.setStatusTip(_translate("PositionDialog", "Set object\'s y position", None))
        self.yPositionLabel.setText(_translate("PositionDialog", "Y Position", None))
        self.okButton.setText(_translate("PositionDialog", "Ok", None))
        self.cancelButton.setText(_translate("PositionDialog", "Cancel", None))
    def ok(self):
        self.results[0] = (self.xPositionSpinbox.value(), self.yPositionSpinbox.value())
        self.results[1] = True
        self.accept()
    def cancel(self):
        self.results[0] = (self.xPositionSpinbox.value(), self.yPositionSpinbox.value())
        self.results[1] = False
        self.reject()
    def done(self, i):
        super(PositionDialog, self).done(i)



class MapSettingsDialog(QtGui.QDialog):
    results = ['','',1,(0,0),'',False]
    def __init__(self, parent=None, filename='', dimensions=(1000,1000)):
        super(MapSettingsDialog, self).__init__(parent)
        self.results[0] = filename
        self.results[3] = dimensions
        self.setupUi()
        self.show()
    def setupUi(self):
        self.setObjectName(_fromUtf8("MapSettings"))
        self.resize(754, 361)
        self.setAutoFillBackground(True)
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 731, 342))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.nameEntry = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.nameEntry.setMinimumSize(QtCore.QSize(261, 27))
        self.nameEntry.setMaximumSize(QtCore.QSize(581, 27))
        self.nameEntry.setText(str(self.results[0]))
        self.nameEntry.setObjectName(_fromUtf8("nameEntry"))
        self.gridLayout.addWidget(self.nameEntry, 0, 1, 1, 1)
        self.profileLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.profileLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.profileLabel.setObjectName(_fromUtf8("profileLabel"))
        self.gridLayout.addWidget(self.profileLabel, 2, 0, 1, 1)
        self.widthSpinbox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.widthSpinbox.setMinimumSize(QtCore.QSize(261, 27))
        self.widthSpinbox.setMaximumSize(QtCore.QSize(261, 27))
        self.widthSpinbox.setMaximum(20000)
        self.widthSpinbox.setValue( int(self.results[3][0]) )
        self.widthSpinbox.setObjectName(_fromUtf8("widthSpinbox"))
        self.gridLayout.addWidget(self.widthSpinbox, 5, 1, 1, 1)
        self.heightSpinbox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.heightSpinbox.setMinimumSize(QtCore.QSize(261, 27))
        self.heightSpinbox.setMaximumSize(QtCore.QSize(261, 27))
        self.heightSpinbox.setMaximum(20000)
        self.heightSpinbox.setValue( int(self.results[3][1]) )
        self.heightSpinbox.setObjectName(_fromUtf8("heightSpinbox"))
        self.gridLayout.addWidget(self.heightSpinbox, 6, 1, 1, 1)
        self.numberOfMapsSpinbox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.numberOfMapsSpinbox.setMinimumSize(QtCore.QSize(91, 27))
        self.numberOfMapsSpinbox.setMaximumSize(QtCore.QSize(91, 27))
        self.numberOfMapsSpinbox.setValue(1)
        self.numberOfMapsSpinbox.setObjectName(_fromUtf8("numberOfMapsSpinbox"))
        self.gridLayout.addWidget(self.numberOfMapsSpinbox, 4, 1, 1, 1)
        self.widthLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.widthLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.widthLabel.setObjectName(_fromUtf8("widthLabel"))
        self.gridLayout.addWidget(self.widthLabel, 5, 0, 1, 1)
        self.numberOfMapsLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.numberOfMapsLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.numberOfMapsLabel.setObjectName(_fromUtf8("numberOfMapsLabel"))
        self.gridLayout.addWidget(self.numberOfMapsLabel, 4, 0, 1, 1)
        self.heightLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.heightLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.heightLabel.setObjectName(_fromUtf8("heightLabel"))
        self.gridLayout.addWidget(self.heightLabel, 6, 0, 1, 1)
        self.unitCombo = QtGui.QComboBox(self.verticalLayoutWidget)
        self.unitCombo.setMinimumSize(QtCore.QSize(261, 27))
        self.unitCombo.setMaximumSize(QtCore.QSize(261, 27))
        self.unitCombo.setObjectName(_fromUtf8("unitCombo"))
        self.unitCombo.addItem(_fromUtf8(""))
        self.unitCombo.addItem(_fromUtf8(""))
        self.unitCombo.addItem(_fromUtf8(""))
        self.unitCombo.addItem(_fromUtf8(""))
        self.unitCombo.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.unitCombo, 7, 1, 1, 1)
        self.unitLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.unitLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.unitLabel.setObjectName(_fromUtf8("unitLabel"))
        self.gridLayout.addWidget(self.unitLabel, 7, 0, 1, 1)
        self.profileComboBox = QtGui.QComboBox(self.verticalLayoutWidget)
        self.profileComboBox.setMinimumSize(QtCore.QSize(261, 27))
        self.profileComboBox.setMaximumSize(QtCore.QSize(261, 27))
        self.profileComboBox.setObjectName(_fromUtf8("profileComboBox"))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.profileComboBox.addItem(_fromUtf8(""))
        self.gridLayout.addWidget(self.profileComboBox, 2, 1, 1, 1)
        self.nameLabel = QtGui.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.nameLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.nameLabel.setObjectName(_fromUtf8("nameLabel"))
        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.selectMapColorButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.selectMapColorButton.setMinimumSize(QtCore.QSize(715, 34))
        self.selectMapColorButton.setMaximumSize(QtCore.QSize(715, 34))
        self.selectMapColorButton.setObjectName(_fromUtf8("selectMapColorButton"))
        self.verticalLayout.addWidget(self.selectMapColorButton)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.okButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.okButton.setMinimumSize(QtCore.QSize(181, 34))
        self.okButton.setMaximumSize(QtCore.QSize(181, 34))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.okButton.clicked.connect(self.ok)
        self.horizontalLayout.addWidget(self.okButton)
        self.templateButton = QtGui.QPushButton(self.verticalLayoutWidget)
        self.templateButton.setMinimumSize(QtCore.QSize(181, 34))
        self.templateButton.setMaximumSize(QtCore.QSize(181, 34))
        self.templateButton.setObjectName(_fromUtf8("templateButton"))
        self.horizontalLayout.addWidget(self.templateButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        self.setWindowTitle(_translate("MapSettings", "Map Settings", None))
        self.profileLabel.setText(_translate("MapSettings", "Profile:", None))
        self.widthLabel.setText(_translate("MapSettings", "Width:", None))
        self.numberOfMapsLabel.setText(_translate("MapSettings", "Number Of Maps:", None))
        self.heightLabel.setText(_translate("MapSettings", "Height:", None))
        self.unitCombo.setItemText(0, _translate("MapSettings", "Inches", None))
        self.unitCombo.setItemText(1, _translate("MapSettings", "Millimeters", None))
        self.unitCombo.setItemText(2, _translate("MapSettings", "Centimeters", None))
        self.unitCombo.setItemText(3, _translate("MapSettings", "Meters", None))
        self.unitCombo.setItemText(4, _translate("MapSettings", "Kilometers", None))
        self.unitLabel.setText(_translate("MapSettings", "Unit:", None))
        self.profileComboBox.setItemText(0, _translate("MapSettings", "Two Wheels Steering", None))
        self.profileComboBox.setItemText(1, _translate("MapSettings", "Skid Steering", None))
        self.profileComboBox.setItemText(2, _translate("MapSettings", "Tank Steering", None))
        self.profileComboBox.setItemText(3, _translate("MapSettings", "Ackerman Steering", None))
        self.profileComboBox.setItemText(4, _translate("MapSettings", "Four Wheels Steering", None))
        self.nameLabel.setText(_translate("MapSettings", "Name:", None))
        self.selectMapColorButton.setText(_translate("MapSettings", "Select Map Color", None))
        self.okButton.setToolTip(_translate("MapSettings", "Save Settings and Open", None))
        self.okButton.setStatusTip(_translate("MapSettings", "Save Settings and Open", None))
        self.okButton.setWhatsThis(_translate("MapSettings", "Save Settings and Open", None))
        self.okButton.setText(_translate("MapSettings", "Ok", None))
        self.templateButton.setToolTip(_translate("MapSettings", "Access Dozens Of Developing Template", None))
        self.templateButton.setStatusTip(_translate("MapSettings", "Access Dozens Of Developing Template", None))
        self.templateButton.setWhatsThis(_translate("MapSettings", "Access Dozens Of Developing Template", None))
        self.templateButton.setText(_translate("MapSettings", "Template", None))
    def ok(self):
        self.results[0] = str( self.nameEntry.text() )
        self.results[1] = str( self.profileComboBox.currentText() )
        self.results[2] = int( self.numberOfMapsSpinbox.value() )
        self.results[3] = ( int(self.widthSpinbox.value()), int(self.heightSpinbox.value()) )
        self.results[4] = str( self.unitCombo.currentText() )
        self.results[5] = True
        self.accept()

class QMessageBoxCustomDialog(QtGui.QMessageBox):
    def __init__(self, parent=None):
        super(QMessageBoxCustomDialog, self).__init__(parent)
    def warning(self, parent, title, text):
        engine.say(title)
        engine.runAndWait()
        engine.say(text)
        engine.runAndWait()
        super(QMessageBoxCustomDialog, self).warning(parent, title, text)
        engine.say("Thank you")
        engine.runAndWait()
    def about(self, parent, title, text):
        engine.say(title)
        engine.runAndWait()
        engine.say(text)
        engine.runAndWait()
        super(QMessageBoxCustomDialog, self).about(parent, title, text)
        engine.say("Thank you")
        engine.runAndWait()
    
class ForwardDistanceItem(QtGui.QGraphicsPolygonItem):
    def __init__(self, parent=None, scene=None):
        super(ForwardDistanceItem, self).__init__(parent, scene)
        path = QtGui.QPainterPath()
        path.moveTo(200, 50)
        path.arcTo(150, 0, 50, 50, 0, 90)
        path.arcTo(50, 0, 50, 50, 90, 90)
        path.arcTo(50, 50, 50, 50, 180, 90)
        path.arcTo(150, 50, 50, 50, 270, 90)
        path.lineTo(200, 25)
        self.myPolygon = path.toFillPolygon()
        self.setPolygon(self.myPolygon)
        self.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
        self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
