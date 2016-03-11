#/***************************************************************************
#                     ExportToMySQL - A QGIS plugin
#                     
# Export vector layer geometries and their attributes direct to MySQL tables
# or to an .sql file on this computer. 
#                             -------------------
# begin     : 2009-12-15 
# copyright : (C) 2009 by tantos
# email     : dek.tantos@gmail.com 
# ***************************************************************************/
#
#/***************************************************************************
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU General Public License as published by  *
# *   the Free Software Foundation; either version 2 of the License, or     *
# *   (at your option) any later version.                                   *
# *                                                                         *
# ***************************************************************************/

# Makefile for the PyQGIS plugin 'ExportToMySQL'. 

UI_FILES = Ui_ExportToMySQL.py

RESOURCE_FILES = resources.py

default: compile
	
compile: $(UI_FILES) $(RESOURCE_FILES)

%.py : %.qrc
	pyrcc4 -o $@  $<

%.py : %.ui
	pyuic4 -o $@ $<
