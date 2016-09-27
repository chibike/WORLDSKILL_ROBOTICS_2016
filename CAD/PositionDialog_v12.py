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

class PositionDialog(QtGui.QDialog):
    results = []
    def __init__(self, parent=None):
        super(PositionDialog, self).__init__(parent)
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
        self.xPositionSpinbox.setMaximum(5000)
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
        self.yPositionSpinbox.setMaximum(5000)
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
        self.results.append(True)
        self.results.append((self.xPositionSpinbox.value(), self.yPositionSpinbox.value()))
        self.accept()
    def cancel(self):
        self.results.append(False)
        self.results.append((self.xPositionSpinbox.value(), self.yPositionSpinbox.value()))
        self.reject()
    def done(self, i):
        super(PositionDialog, self).done(i)


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = PositionDialog()
    app.exec_()
    print "-"+str(ui.results)+"-"

