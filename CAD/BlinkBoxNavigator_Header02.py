import sys, serial, time, math
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

def getRectangle(x, y, width, height, pen, brush):
    rectItem = QtGui.QGraphicsRectItem()
    rectItem.setRect(x,y,width,height)
    rectItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    rectItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    rectItem.setVisible(True)
    rectItem.setData(0, ["ItemIsMovable", "ItemIsSelectable", "ItemIsVisible"])
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
    lineItem.setData(0, ["ItemIsMovable", "ItemIsSelectable", "ItemIsVisible"])
    lineItem.setData(1, length)
    lineItem.setPen(pen)
    return lineItem

def getLineP(x1, y1, x2, y2, pen):
    print "Line =",(x1, y1, x2, y2)
    lineItem = QtGui.QGraphicsLineItem()
    lineItem.setLine(x1, y1, x2, y2)
    lineItem.setFlag(QtGui.QGraphicsItem.ItemIsMovable, True)
    lineItem.setFlag(QtGui.QGraphicsItem.ItemIsSelectable, True)
    lineItem.setVisible(True)
    lineItem.setData(0, ["ItemIsMovable", "ItemIsSelectable", "ItemIsVisible"])
    lineItem.setData(1, ["ItemIsPoygon"])
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
    def __init__(self, parent=None, scene=None, pen=None, brush=None):
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
            if ( point[0] < self._points[0][0]+8 and point[0] > self._points[0][0]-8 ) and ( point[1] < self._points[0][1]+8 and point[1] > self._points[0][1]-8 ):
                self._points.append(self._points[0])#End the shape
                print "Complete"
            else:
                self._points.append((int(point[0]),int(point[1])))
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
        self.redraw()
    def redraw(self):
        self.removeFromScene()
        if len(self._points) > 1:
            for i in range(len(self._points)-1):
                line = getLine(0,0, self._lengths[i], self._pen)
                line.setRotation(self._angles[i])
                line.setPos(self._points[i][0], self._points[i][1])
                #line.setFlag(QtGui.QGraphicsItem.ItemIsMovable, False)
                #line.setData(0, ["ItemIsPolygon", "ItemIsSelectable", "ItemIsVisible"])
                self._item_ids[line] = i
                self._scene.addItem(line)
        if len(self._points) >  2 and self._points[0] == self._points[-1]:
            points = []
            for i in self._points:
                points.append(QtCore.QPointF(i[0], i[1]))
            self._polygon.setPolygon(QtGui.QPolygonF(points))
            self._scene.addItem(self._polygon)
        
    def updatePaint(self):
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
        self.redraw()
    def setPen(self, pen):
        self._pen = pen
        self.redraw()
    def setBrush(self, brush):
        self._brush = brush
        self.updatePaint()
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
