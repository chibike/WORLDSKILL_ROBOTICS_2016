# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BlinkBoxMapSettings_v12.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

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

class MapSettingsDialog(QtGui.QDialog):
    results = ['','',1,(0,0),'',False]
    def __init__(self, parent=None):
        super(MapSettingsDialog, self).__init__(parent)
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
        self.widthSpinbox.setObjectName(_fromUtf8("widthSpinbox"))
        self.gridLayout.addWidget(self.widthSpinbox, 5, 1, 1, 1)
        self.heightSpinbox = QtGui.QSpinBox(self.verticalLayoutWidget)
        self.heightSpinbox.setMinimumSize(QtCore.QSize(261, 27))
        self.heightSpinbox.setMaximumSize(QtCore.QSize(261, 27))
        self.heightSpinbox.setMaximum(20000)
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
        self.selectMapColorButton.setMinimumSize(QtCore.QSize(729, 34))
        self.selectMapColorButton.setMaximumSize(QtCore.QSize(729, 34))
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


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    ui = MapSettingsDialog()
    app.exec_()
    print ui.results

