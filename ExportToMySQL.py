"""
/***************************************************************************
                     ExportToMySQL - A QGIS plugin
                     
 Export vector layer geometries and their attributes direct to MySQL tables
 or to an .sql file on this computer. 
   -> This plug-in based on HTML Image Map Plugin developed by Richard
      Duivenvoorde.
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
# TODO:
# 1. Can we remove the dependency on mysqldb if only writing to sql files.
# 2. utf-8 support.


# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
# Initialize Qt resources from file resources.py
import resources
# Import the MySQL library
import MySQLdb
# Import the code for the dialog
from ExportToMySQLDialog import ExportToMySQLDialog

class ExportToMySQL: 

    MSG_BOX_TITLE = "Export To MySQL"

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # Set defaults
        self.mysqlHost = "localhost"
        self.mysqlUsername = "root"
        self.mysqlPassword = ""
        self.mysqlPort = 3306
        self.sqlFilename = "/home/"
        self.mysqlDatabaseName = "test"
        self.mysqlTableName = "geometry"

    def initGui(self):  
        # Create action that will start plugin configuration
        self.action = QAction(QIcon(":/plugins/exporttomysql/icon.png"), \
                              "Export To MySQL...", self.iface.mainWindow())
        # connect the action to the run method
        QObject.connect(self.action, SIGNAL("triggered()"), self.run) 

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&Export To MySQL...", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu("&Export To MySQL...",self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self): 
        layer =  self.iface.activeLayer()
        if layer == None:
            QMessageBox.warning(self.iface.mainWindow(), self.MSG_BOX_TITLE, ("No active layer found\n" "Please make one (multi)polygon or point layer active\n" "by choosing a layer in the legend"), QMessageBox.Ok, QMessageBox.Ok)
            return
        # don't know if this is possible / needed
        if not layer.isValid():
            QMessageBox.warning(self.iface.mainWindow(), self.MSG_BOX_TITLE, ("No VALID layer found\n" "Please make one (multi)polygon or point layer active\n" "by choosing a layer in the legend"), QMessageBox.Ok, QMessageBox.Ok)
            return
        
        self.provider = layer.dataProvider()
        # self.currentExtent = self.iface.mapCanvas().extent()
        if (layer.type()>0): # 0 = vector, 1 = raster
            QMessageBox.warning(self.iface.mainWindow(), self.MSG_BOX_TITLE, ("Wrong layer type, only vector layers can be used..\n" "Please make one vector layer active\n" "by choosing a vector layer in the legend"), QMessageBox.Ok, QMessageBox.Ok)
            return
        if not(self.provider.geometryType() == QGis.WKBPolygon or self.provider.geometryType() == QGis.WKBMultiPolygon or self.provider.geometryType() == QGis.WKBPoint):
            QMessageBox.warning(self.iface.mainWindow(), self.MSG_BOX_TITLE, ("Wrong geometrytype, only (multi)polygons and points can be used.\n" "Please make one (multi)polygon or point layer active\n" "by choosing a layer in the legend"), QMessageBox.Ok, QMessageBox.Ok)
            return
        
        #QMessageBox.information(self.iface.mainWindow(), self.MSG_BOX_TITLE, ( layer.filename() ), QMessageBox.Ok)
        self.exportToMySQLGui = ExportToMySQLDialog()
        QObject.connect(self.exportToMySQLGui, SIGNAL("zoomFull(QString)"), self.doZoomFull)
        QObject.connect(self.exportToMySQLGui, SIGNAL("selectAll(QString)"), self.doSelectAll)
        QObject.connect(self.exportToMySQLGui, SIGNAL("getMySQLHost(QString)"), self.setMySQLHost)
        QObject.connect(self.exportToMySQLGui, SIGNAL("getMySQLUsername(QString)"), self.setMySQLUsername)
        QObject.connect(self.exportToMySQLGui, SIGNAL("getMySQLPassword(QString)"), self.setMySQLPassword)
        QObject.connect(self.exportToMySQLGui, SIGNAL("getMySQLPort(int)"), self.setMySQLPort)
        QObject.connect(self.exportToMySQLGui, SIGNAL("getSQLFilename(QString)"), self.setSQLFilename)
        QObject.connect(self.exportToMySQLGui, SIGNAL("getMySQLDatabaseName(QString)"), self.setMySQLDatabaseName)
        QObject.connect(self.exportToMySQLGui, SIGNAL("getMySQLTableName(QString)"), self.setMySQLTableName)
        QObject.connect(self.exportToMySQLGui, SIGNAL("go(QString)"), self.go)
        
        # remember last session
        self.exportToMySQLGui.setMySQLHost(self.mysqlHost)
        self.exportToMySQLGui.setMySQLUsername(self.mysqlUsername)
        self.exportToMySQLGui.setMySQLPassword(self.mysqlPassword)
        self.exportToMySQLGui.setMySQLPort(self.mysqlPort)
        self.exportToMySQLGui.setSQLFilename(self.sqlFilename)
        self.exportToMySQLGui.setMySQLDatabaseName(self.mysqlDatabaseName)
        self.exportToMySQLGui.setMySQLTableName(self.mysqlTableName)
        
        # show the dialog
        self.exportToMySQLGui.show()
        #result = self.exportToMySQLGui.exec_() 
        # See if OK was pressed
        #if result == 1: 
        #  self.go()

    def getSQL(self):
        # create a holder for retrieving features from the provider
        feature = QgsFeature();
        html = []
        if self.exportToMySQLGui.addDropDatabaseCheckBox.isChecked():
            html.append('DROP DATABASE IF EXISTS `' + self.exportToMySQLGui.mysqlDatabaseName.text() + '`;\n')
        html.append('CREATE DATABASE IF NOT EXISTS `' + self.exportToMySQLGui.mysqlDatabaseName.text() + '`;\n')
        html.append('USE `' + self.exportToMySQLGui.mysqlDatabaseName.text() + '`;\n')
        if self.exportToMySQLGui.addDropTableCheckBox.isChecked():
            html.append('DROP TABLE IF EXISTS `' + self.exportToMySQLGui.mysqlTableName.text() + '`;\n')
        createtable = 'CREATE TABLE IF NOT EXISTS `' + self.exportToMySQLGui.mysqlTableName.text() + '` ( '
        fields = self.provider.fields()
        for (i, field) in fields.iteritems():
            createtable += '`' + field.name().trimmed() + '` VARCHAR(255) NULL, '
        if 1==1:
            createtable += '`geom` GEOMETRY NULL);\n'
        else:
            createtable += '`geom` TEXT NULL);\n'            
        html.append(createtable)     
        # start data retrieval: fetch list all attributes
        allAttrs = self.provider.attributeIndexes()
        # now iterate through each feature
        if self.exportToMySQLGui.featureComboBox.currentIndex() == 0:
            # NOTE: This first option returns selected features as GEOMETRY var type 
            #       (requires MySQL spatial extension)
            selectedFeaturesIds = self.iface.activeLayer().selectedFeaturesIds()
            for featureId in selectedFeaturesIds:
                # load geometry and attributes into "feature"
                self.provider.featureAtId(featureId, feature, True, allAttrs)
                geom = feature.geometry()
                columnval = ""
                h = "INSERT INTO `" + self.exportToMySQLGui.mysqlTableName.text() + "` ( "
                fields = self.provider.fields()
                for (i, field) in fields.iteritems():
                    h += '`' + field.name().trimmed() + '`, '
                    columnval += "'" + self.jsEscapeString(feature.attributeMap()[i].toString()) + "', "
                h += "`geom`"
                h += ") VALUES ("
                h += columnval + "GeomFromText('" + geom.exportToWkt()
                h += "'));\n"
                if len(h)>0:
                    html.append(h)
        elif self.exportToMySQLGui.featureComboBox.currentIndex() == 1:
            # NOTE: This second option returns only the features in current view as text 
            #       (co-ordinates reset such that they start at 0,0)
            currentExtent = self.iface.mapCanvas().extent()
            # keep the current extent as a Geometry to be able to do some 'contains' tests later
            # ?? construct one first (get a pointer??)
            self.extentAsPoly = QgsGeometry()
            self.extentAsPoly = QgsGeometry.fromRect(currentExtent)
            # select features within current extent, with  ALL attributes, WITHIN currentExtent, 
            # WITH geom, AND using Intersect instead of bbox
            self.provider.select(allAttrs, currentExtent, True, True)
            while self.provider.nextFeature(feature):
                geom = feature.geometry()
                #print "GeomType: %s" % geom.wkbType()
                if geom.wkbType() == QGis.WKBPoint: # 1 = WKBPoint
                    #print "trying to buffer..."
                    buffer = self.iface.mapCanvas().mapUnitsPerPixel()*10 #(plusminus 20pixel areas)
                    #print "buffer ok..."
                    polygon = geom.buffer(buffer,0).asPolygon()
                    for ring in polygon:
                        h = self.ring2area(feature, ring, currentExtent)
                        if len(h)>0:
                            html.append(h)
                if geom.wkbType() == QGis.WKBPolygon: # 3 = WKBTYPE.WKBPolygon:
                    polygon = geom.asPolygon()  # returns a list
                    for ring in polygon:
                        h = self.ring2area(feature, ring, currentExtent)
                        if len(h)>0:
                            html.append(h)
                if geom.wkbType() == QGis.WKBMultiPolygon: # 6 = WKBTYPE.WKBMultiPolygon:
                    multipolygon = geom.asMultiPolygon() # returns a list
                    for polygon in multipolygon:
                        for ring in polygon:
                            h = self.ring2area(feature, ring, currentExtent)
                            if len(h)>0:
                                html.append(h)    
        else:
            return
        return html

    def go(self):
        msg = ""
        errMsg = ""
        if self.exportToMySQLGui.exportToSQLFileCheckBox.isChecked():
            try:
                if len(self.sqlFilename)==0:
                    raise IOError
                writeMode = "a"
                if self.exportToMySQLGui.replaceFileContentCheckBox.isChecked():
                    writeMode = "w"
                file = open(self.sqlFilename, writeMode)
                file.writelines(self.getSQL())
                file.close()
                msg += "File successfully saved to: " + self.sqlFilename + "\n"
            except IOError:
                QMessageBox.warning(self.iface.mainWindow(), self.MSG_BOX_TITLE, ( "Please give a valid filename.\n" ), QMessageBox.Ok, QMessageBox.Ok)
        if self.exportToMySQLGui.exportToMySQLDataCheckBox.isChecked():
            try:
                rowCount=0
                conn = MySQLdb.connect (host = str(self.exportToMySQLGui.mysqlHost.text()),
                                       port = int(str(self.exportToMySQLGui.mysqlPort.text())),
                                       user = str(self.exportToMySQLGui.mysqlUsername.text()),
                                       passwd = str(self.exportToMySQLGui.mysqlPassword.text()),
                                       db = str(self.exportToMySQLGui.mysqlDatabaseName.text()))
                cursor = conn.cursor ()
                items = self.getSQL()
                for item in items:
                    #QMessageBox.information(self.iface.mainWindow(), self.MSG_BOX_TITLE, ( str(item) ), QMessageBox.Ok)
                    cursor.execute (str(item))
                    rowCount += cursor.rowcount
                rowCount -= 1
                msg += "Number of rows inserted : %d " % rowCount
                cursor.close ()
                conn.close ()
                #except IOError:
            except MySQLdb.Error, e:
                QMessageBox.warning(self.iface.mainWindow(), self.MSG_BOX_TITLE, ( "Can't connect to MySQL Server using provided setting." ), QMessageBox.Ok, QMessageBox.Ok)
        if len(msg)>0:
            QMessageBox.information(self.iface.mainWindow(), self.MSG_BOX_TITLE, ( msg ), QMessageBox.Ok)
        #self.exportToMySQLGui.hide()

    def w2p(self, x, y, mupp, minx, maxy):
        pixX = (x - minx)/mupp
        pixY = (y - maxy)/mupp
        return [int(pixX), int(-pixY)]

    def ring2area(self, feature, ring, currentExtent):
        columnval = ""
        htm = "INSERT INTO `" + self.exportToMySQLGui.mysqlTableName.text() + "` ( "
        fields = self.provider.fields()
        for (i, field) in fields.iteritems():
            htm += '`' + field.name().trimmed() + '`, '
            columnval += "'" + self.jsEscapeString(feature.attributeMap()[i].toString()) + "', "

        htm += "`geom`"
        htm += ") VALUES ("
        htm += columnval + "'"

        lastPixel=[0,0]
        insideExtent = False
        coordCount = 0
        for point in ring:
            if self.extentAsPoly.contains(point):
                insideExtent = True
            pixpoint =  self.w2p(point.x(), point.y(), 
                                 self.iface.mapCanvas().mapUnitsPerPixel(),
                                 currentExtent.xMinimum(), currentExtent.yMaximum())
            if lastPixel<>pixpoint:
                coordCount = coordCount +1
                htm += (str(pixpoint[0]) + ',' + str(pixpoint[1]) + ',')
                lastPixel = pixpoint
        htm.remove(len(htm)-1,len(htm))
        # check if there are more then 2 coords: very small polygons on current map can have coordinates
        # which if rounded to pixels all come to the same pixel, resulting in just ONE x,y coordinate
        # we skip these
        if coordCount < 2:
            #print "Ring contains just one pixel coordinate pair: skipping"
            return ''
        # if at least ONE pixel of this ring is in current view extent, return the area-string, otherwise return an empty string
        if not insideExtent:
            #print "RING FULLY OUTSIDE EXTENT: %s " % ring
            return ''
        else:
            htm += "');\n"
            return htm

    # escape ' and " so string can be safely used as string javascript argument
    def jsEscapeString(self, str):
        return str.replace("'", "\\'").replace('"', '\"')
  
    def doZoomFull(self, foo):
        #zoom full. reference : http://doc.qgis.org/stable/classQgisInterface.html#22f213cfba19b4d9b5bf9ede478797df
        self.iface.zoomFull()

    def doSelectAll(self):
        self.iface.activeLayer().select([]) # we don't need the attributes at this stage
        self.iface.activeLayer().setSelectedFeatures([feat.id() for feat in self.iface.activeLayer()]) # select all

    def setMySQLHost(self, txt):
        self.mysqlHost = txt

    def setMySQLUsername(self, txt):
        self.mysqlUsername = txt

    def setMySQLPassword(self, txt):
        self.mysqlPassword = txt

    def setMySQLPort(self, txtVal):
        self.mysqlPort = txtVal

    def setSQLFilename(self, txt):
        self.sqlFilename = txt

    def setMySQLDatabaseName(self, txt):
        self.mysqlDatabaseName = txt

    def setMySQLTableName(self, txt):
        self.mysqlTableName = txt
