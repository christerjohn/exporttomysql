# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui_ExportToMySQL.ui'
#
# Created: Wed Jul 18 17:23:20 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ExportToMySQL(object):
    def setupUi(self, ExportToMySQL):
        ExportToMySQL.setObjectName(_fromUtf8("ExportToMySQL"))
        ExportToMySQL.resize(462, 391)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ExportToMySQL.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(ExportToMySQL)
        self.buttonBox.setGeometry(QtCore.QRect(10, 350, 441, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.exportToMySQLDataCheckBox = QtGui.QGroupBox(ExportToMySQL)
        self.exportToMySQLDataCheckBox.setGeometry(QtCore.QRect(10, 10, 441, 121))
        self.exportToMySQLDataCheckBox.setAutoFillBackground(False)
        self.exportToMySQLDataCheckBox.setCheckable(True)
        self.exportToMySQLDataCheckBox.setObjectName(_fromUtf8("exportToMySQLDataCheckBox"))
        self.labelMySQLHost = QtGui.QLabel(self.exportToMySQLDataCheckBox)
        self.labelMySQLHost.setGeometry(QtCore.QRect(20, 30, 56, 22))
        self.labelMySQLHost.setObjectName(_fromUtf8("labelMySQLHost"))
        self.mysqlHost = QtGui.QLineEdit(self.exportToMySQLDataCheckBox)
        self.mysqlHost.setGeometry(QtCore.QRect(100, 30, 131, 22))
        self.mysqlHost.setObjectName(_fromUtf8("mysqlHost"))
        self.labelMySQLUsername = QtGui.QLabel(self.exportToMySQLDataCheckBox)
        self.labelMySQLUsername.setGeometry(QtCore.QRect(20, 60, 71, 22))
        self.labelMySQLUsername.setObjectName(_fromUtf8("labelMySQLUsername"))
        self.mysqlUsername = QtGui.QLineEdit(self.exportToMySQLDataCheckBox)
        self.mysqlUsername.setGeometry(QtCore.QRect(100, 60, 131, 22))
        self.mysqlUsername.setObjectName(_fromUtf8("mysqlUsername"))
        self.labelMySQLPassword = QtGui.QLabel(self.exportToMySQLDataCheckBox)
        self.labelMySQLPassword.setGeometry(QtCore.QRect(20, 90, 56, 22))
        self.labelMySQLPassword.setObjectName(_fromUtf8("labelMySQLPassword"))
        self.mysqlPassword = QtGui.QLineEdit(self.exportToMySQLDataCheckBox)
        self.mysqlPassword.setGeometry(QtCore.QRect(100, 90, 131, 22))
        self.mysqlPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.mysqlPassword.setObjectName(_fromUtf8("mysqlPassword"))
        self.labelMySQLPort = QtGui.QLabel(self.exportToMySQLDataCheckBox)
        self.labelMySQLPort.setGeometry(QtCore.QRect(270, 30, 31, 22))
        self.labelMySQLPort.setObjectName(_fromUtf8("labelMySQLPort"))
        self.mysqlPort = QtGui.QSpinBox(self.exportToMySQLDataCheckBox)
        self.mysqlPort.setGeometry(QtCore.QRect(310, 30, 61, 22))
        self.mysqlPort.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.mysqlPort.setMinimum(1)
        self.mysqlPort.setMaximum(999999999)
        self.mysqlPort.setObjectName(_fromUtf8("mysqlPort"))
        self.mysqlDatabaseName = QtGui.QLineEdit(ExportToMySQL)
        self.mysqlDatabaseName.setGeometry(QtCore.QRect(90, 250, 171, 22))
        self.mysqlDatabaseName.setObjectName(_fromUtf8("mysqlDatabaseName"))
        self.mysqlTableName = QtGui.QLineEdit(ExportToMySQL)
        self.mysqlTableName.setGeometry(QtCore.QRect(90, 280, 171, 22))
        self.mysqlTableName.setObjectName(_fromUtf8("mysqlTableName"))
        self.labelTableName = QtGui.QLabel(ExportToMySQL)
        self.labelTableName.setGeometry(QtCore.QRect(10, 280, 71, 22))
        self.labelTableName.setObjectName(_fromUtf8("labelTableName"))
        self.labelMySQLDatabaseName = QtGui.QLabel(ExportToMySQL)
        self.labelMySQLDatabaseName.setGeometry(QtCore.QRect(10, 250, 56, 22))
        self.labelMySQLDatabaseName.setObjectName(_fromUtf8("labelMySQLDatabaseName"))
        self.line = QtGui.QFrame(ExportToMySQL)
        self.line.setGeometry(QtCore.QRect(10, 120, 441, 22))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.exportToSQLFileCheckBox = QtGui.QGroupBox(ExportToMySQL)
        self.exportToSQLFileCheckBox.setGeometry(QtCore.QRect(10, 140, 441, 91))
        self.exportToSQLFileCheckBox.setCheckable(True)
        self.exportToSQLFileCheckBox.setObjectName(_fromUtf8("exportToSQLFileCheckBox"))
        self.labelSQLFilename = QtGui.QLabel(self.exportToSQLFileCheckBox)
        self.labelSQLFilename.setGeometry(QtCore.QRect(20, 30, 91, 22))
        self.labelSQLFilename.setObjectName(_fromUtf8("labelSQLFilename"))
        self.sqlFilename = QtGui.QLineEdit(self.exportToSQLFileCheckBox)
        self.sqlFilename.setGeometry(QtCore.QRect(100, 30, 261, 22))
        self.sqlFilename.setReadOnly(False)
        self.sqlFilename.setObjectName(_fromUtf8("sqlFilename"))
        self.replaceFileContentCheckBox = QtGui.QCheckBox(self.exportToSQLFileCheckBox)
        self.replaceFileContentCheckBox.setGeometry(QtCore.QRect(100, 60, 151, 22))
        self.replaceFileContentCheckBox.setObjectName(_fromUtf8("replaceFileContentCheckBox"))
        self.browseButton = QtGui.QPushButton(self.exportToSQLFileCheckBox)
        self.browseButton.setGeometry(QtCore.QRect(370, 30, 61, 22))
        self.browseButton.setObjectName(_fromUtf8("browseButton"))
        self.line_2 = QtGui.QFrame(ExportToMySQL)
        self.line_2.setGeometry(QtCore.QRect(10, 220, 441, 22))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.addDropDatabaseCheckBox = QtGui.QCheckBox(ExportToMySQL)
        self.addDropDatabaseCheckBox.setGeometry(QtCore.QRect(270, 250, 151, 22))
        self.addDropDatabaseCheckBox.setObjectName(_fromUtf8("addDropDatabaseCheckBox"))
        self.addDropTableCheckBox = QtGui.QCheckBox(ExportToMySQL)
        self.addDropTableCheckBox.setGeometry(QtCore.QRect(270, 280, 131, 22))
        self.addDropTableCheckBox.setObjectName(_fromUtf8("addDropTableCheckBox"))
        self.zoomFullButton = QtGui.QPushButton(ExportToMySQL)
        self.zoomFullButton.setEnabled(False)
        self.zoomFullButton.setGeometry(QtCore.QRect(360, 310, 84, 22))
        self.zoomFullButton.setObjectName(_fromUtf8("zoomFullButton"))
        self.labelFeatures = QtGui.QLabel(ExportToMySQL)
        self.labelFeatures.setGeometry(QtCore.QRect(10, 310, 71, 22))
        self.labelFeatures.setObjectName(_fromUtf8("labelFeatures"))
        self.featureComboBox = QtGui.QComboBox(ExportToMySQL)
        self.featureComboBox.setGeometry(QtCore.QRect(90, 310, 171, 22))
        self.featureComboBox.setObjectName(_fromUtf8("featureComboBox"))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.featureComboBox.addItem(_fromUtf8(""))
        self.selectAllButton = QtGui.QPushButton(ExportToMySQL)
        self.selectAllButton.setGeometry(QtCore.QRect(270, 310, 84, 22))
        self.selectAllButton.setObjectName(_fromUtf8("selectAllButton"))

        self.retranslateUi(ExportToMySQL)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), ExportToMySQL.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), ExportToMySQL.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportToMySQL)

    def retranslateUi(self, ExportToMySQL):
        ExportToMySQL.setWindowTitle(QtGui.QApplication.translate("ExportToMySQL", "Export To MySQL", None, QtGui.QApplication.UnicodeUTF8))
        self.exportToMySQLDataCheckBox.setTitle(QtGui.QApplication.translate("ExportToMySQL", "Export to MySQL data", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMySQLHost.setText(QtGui.QApplication.translate("ExportToMySQL", "Host", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlHost.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "MySQL host name. Default : localhost", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlHost.setText(QtGui.QApplication.translate("ExportToMySQL", "test", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMySQLUsername.setText(QtGui.QApplication.translate("ExportToMySQL", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlUsername.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "MySQL username. Default : root", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlUsername.setText(QtGui.QApplication.translate("ExportToMySQL", "test", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMySQLPassword.setText(QtGui.QApplication.translate("ExportToMySQL", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlPassword.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "MySQL password. Default : empty", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMySQLPort.setText(QtGui.QApplication.translate("ExportToMySQL", "Port", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlPort.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "MySQL port. Default : 3306", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlDatabaseName.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "Database name", None, QtGui.QApplication.UnicodeUTF8))
        self.mysqlTableName.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "Table name where data will be stored.", None, QtGui.QApplication.UnicodeUTF8))
        self.labelTableName.setText(QtGui.QApplication.translate("ExportToMySQL", "Table name", None, QtGui.QApplication.UnicodeUTF8))
        self.labelMySQLDatabaseName.setText(QtGui.QApplication.translate("ExportToMySQL", "Database", None, QtGui.QApplication.UnicodeUTF8))
        self.exportToSQLFileCheckBox.setTitle(QtGui.QApplication.translate("ExportToMySQL", "Export to SQL file", None, QtGui.QApplication.UnicodeUTF8))
        self.labelSQLFilename.setText(QtGui.QApplication.translate("ExportToMySQL", "Filename", None, QtGui.QApplication.UnicodeUTF8))
        self.sqlFilename.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "Fullpath to the filename where queries will be stored.", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceFileContentCheckBox.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "Checked : Replace the contents with new contents.\n"
"Unchecked : Append its contents.", None, QtGui.QApplication.UnicodeUTF8))
        self.replaceFileContentCheckBox.setText(QtGui.QApplication.translate("ExportToMySQL", "Replace file contents", None, QtGui.QApplication.UnicodeUTF8))
        self.browseButton.setText(QtGui.QApplication.translate("ExportToMySQL", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.addDropDatabaseCheckBox.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "Force to drop database if exists.", None, QtGui.QApplication.UnicodeUTF8))
        self.addDropDatabaseCheckBox.setText(QtGui.QApplication.translate("ExportToMySQL", "Add drop database", None, QtGui.QApplication.UnicodeUTF8))
        self.addDropTableCheckBox.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "Force to drop table if exists.", None, QtGui.QApplication.UnicodeUTF8))
        self.addDropTableCheckBox.setText(QtGui.QApplication.translate("ExportToMySQL", "Add drop table", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomFullButton.setToolTip(QtGui.QApplication.translate("ExportToMySQL", "Zoom full the active layers", None, QtGui.QApplication.UnicodeUTF8))
        self.zoomFullButton.setText(QtGui.QApplication.translate("ExportToMySQL", "Zoom Full", None, QtGui.QApplication.UnicodeUTF8))
        self.labelFeatures.setText(QtGui.QApplication.translate("ExportToMySQL", "Features", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(0, QtGui.QApplication.translate("ExportToMySQL", "Selected as geometry", None, QtGui.QApplication.UnicodeUTF8))
        self.featureComboBox.setItemText(1, QtGui.QApplication.translate("ExportToMySQL", "Current view as text (legacy)", None, QtGui.QApplication.UnicodeUTF8))
        self.selectAllButton.setText(QtGui.QApplication.translate("ExportToMySQL", "Select All", None, QtGui.QApplication.UnicodeUTF8))
