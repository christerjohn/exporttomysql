"""
/***************************************************************************
ExportToMySQLDialog
A QGIS plugin
Export To MySQL

This plug-in based on HTML Image Map Plugin developed by Richard Duivenvoorde

                             -------------------
begin                : 2009-12-15 
copyright            : (C) 2009 by tantos
email                : dek.tantos@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4 import QtCore, QtGui 
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import QgsContextHelp
from Ui_ExportToMySQL import Ui_ExportToMySQL
# create the dialog for zoom to point
class ExportToMySQLDialog(QtGui.QDialog, Ui_ExportToMySQL):
  
    MSG_BOX_TITLE = "Export To MySQL"
    PATH_STRING = ""
  
    def __init__(self): 
        QtGui.QDialog.__init__(self) 
        # Set up the user interface from Designer. 
        # self = Ui_ExportToMySQL()
        self.setupUi(self) 

    def on_buttonBox_accepted(self):
        if (not self.exportToMySQLDataCheckBox.isChecked()) and (not self.exportToSQLFileCheckBox.isChecked()):
            QMessageBox.warning(self, self.MSG_BOX_TITLE, ("Please choose at least one output type."), QMessageBox.Ok)
            return
        self.emit(SIGNAL("getMySQLHost(QString)"), self.mysqlHost.text())
        self.emit(SIGNAL("getMySQLUsername(QString)"), self.mysqlUsername.text())
        self.emit(SIGNAL("getMySQLPassword(QString)"), self.mysqlPassword.text())
        self.emit(SIGNAL("getMySQLPort(QString)"), self.mysqlPort.text())
        self.emit(SIGNAL("getSQLFilename(QString)"), self.sqlFilename.text())
        self.emit(SIGNAL("getMySQLDatabaseName(QString)"), self.mysqlDatabaseName.text())
        self.emit(SIGNAL("getMySQLTableName(QString)"), self.mysqlTableName.text())
        self.emit(SIGNAL("go(QString)"), "ok")

    def on_exportToSQLFileCheckBox_stateChanged(self):
        self.sqlFilename.setEnabled(self.exportToSQLFileCheckBox.isChecked())

    def on_exportToMySQLDataCheckBox_stateChanged(self):
        self.mysqlHost.setEnabled(self.saveAsMySQLDataCheckBox.isChecked())
        self.mysqlUsername.setEnabled(self.saveAsMySQLDataCheckBox.isChecked())
        self.mysqlPassword.setEnabled(self.saveAsMySQLDataCheckBox.isChecked())
        self.mysqlPort.setEnabled(self.saveAsMySQLDataCheckBox.isChecked())

    def on_addDropDatabaseCheckBox_stateChanged(self):
        self.addDropTableCheckBox.setEnabled(self.addDropDatabaseCheckBox.isChecked())

    def on_zoomFullButton_clicked(self):
        self.emit(SIGNAL("zoomFull(QString)"), "ok" )

    def setMySQLHost(self, txt):
        self.mysqlHost.setText(txt)

    def setMySQLUsername(self, txt):
        self.mysqlUsername.setText(txt)

    def setMySQLPassword(self, txt):
        self.mysqlPassword.setText(txt)

    def setMySQLPort(self, txtVal):
        self.mysqlPort.setValue(txtVal)

    def setSQLFilename(self, txt):
        self.sqlFilename.setText(txt)

    def setMySQLDatabaseName(self, txt):
        self.mysqlDatabaseName.setText(txt)

    def setMySQLTableName(self, txt):
        self.mysqlTableName.setText(txt)

    @pyqtSignature("on_browseButton_clicked()")
    def on_browseButton_clicked(self):
        fileName = QFileDialog.getSaveFileName(self, self.PATH_STRING, "/", "")
        # TODO do some checks to be sure there is no extension
        self.sqlFilename.setText(fileName)

    def on_selectAllButton_clicked(self):
        self.emit(SIGNAL("selectAll(QString)"), "ok" )

    def on_featureComboBox_currentIndexChanged(self):
        if self.featureComboBox.currentIndex() == 0:
            self.selectAllButton.setEnabled(True)
            self.zoomFullButton.setEnabled(False)
        elif self.featureComboBox.currentIndex() == 1:
            self.selectAllButton.setEnabled(False)
            self.zoomFullButton.setEnabled(True)
        else:
            # Should never happen!  
            self.selectAllButton.setEnabled(True)
            self.zoomFullButton.setEnabled(True)        
      
