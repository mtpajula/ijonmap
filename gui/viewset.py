#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PySide import QtCore, QtGui
from ui.viewsetdialog import Ui_Dialog

class Ui_ViewSet(Ui_Dialog):
    
    def __init__(self, calc):
        self.calc = calc
     
    def startMain(self, MainWindow):
        self.setupUi(MainWindow)
        
        self.lineEdit.setText(str(self.calc.center_x))
        self.lineEdit_2.setText(str(self.calc.center_y))
        self.lineEdit_3.setText(str(self.calc.scale_factor))
        
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), self.set)
        
    def set(self):
        
        self.calc.center_x = int(self.lineEdit.text())
        self.calc.center_y = int(self.lineEdit_2.text())
        self.calc.scale_factor = float(self.lineEdit_3.text())
        
        
