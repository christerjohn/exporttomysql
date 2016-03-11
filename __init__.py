"""
/***************************************************************************
                     ExportToMySQL - A QGIS plugin
                     
 Export vector layer geometries and their attributes direct to MySQL tables
 or to an .sql file on this computer. 
                             -------------------
 begin     : 2009-12-15 
 copyright : (C) 2009 by tantos
 email     : dek.tantos@gmail.com 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
    return "Export To MySQL" 
def description():
    return "Export vector layer geometries and their attributes direct to MySQL tables or to an .sql file on this computer."
def version(): 
    return "Version 0.2" 
def qgisMinimumVersion():
    return "1.0"
def classFactory(iface): 
    # load ExportToMySQL class from file ExportToMySQL
    from ExportToMySQL import ExportToMySQL 
    return ExportToMySQL(iface)
