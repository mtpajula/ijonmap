#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ui.mainwindow import Ui_MainWindow
from PySide import QtCore, QtGui
from paintwidget import PaintWidget
from viewset import Ui_ViewSet

class Ui_Main(Ui_MainWindow):
    
    def __init__(self, controller):
        self.controller = controller
     
    def startMain(self, MainWindow):
        self.setupUi(MainWindow)
        
        self.paint = PaintWidget(self.controller.mathmanager.draw, self.controller.projects.current())
        
        self.horizontalLayout.addWidget(self.paint)
        
        self.actionUusi_piste = QtGui.QAction(MainWindow)
        self.actionUusi_piste.setObjectName("actionUusi_piste")
        self.actionUusi_piste.setText('Uusi piste')
        self.toolBar.addAction(self.actionUusi_piste)
        
        QtCore.QObject.connect(self.actionAseta, QtCore.SIGNAL("triggered()"), self.open_viewset_dialog)
        QtCore.QObject.connect(self.actionAvaa, QtCore.SIGNAL("triggered()"), self.open_file)
        QtCore.QObject.connect(self.actionKeskit, QtCore.SIGNAL("triggered()"), self.center_view)
        QtCore.QObject.connect(self.actionLopeta, QtCore.SIGNAL("triggered()"), MainWindow.close)
        
        self.center_view()
        
    def center_view(self):
        self.paint.show_all = True
        self.paint.repaint()

    def open_viewset_dialog(self):
        
        new_object = QtGui.QDialog()
        new_object.uinh = Ui_ViewSet(self.controller.mathmanager.draw)
        new_object.uinh.startMain(new_object)
        new_object.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        new_object.exec_()
        
        self.paint.show_all = False
        self.paint.repaint()
        
    def new_point(self):
        pass
        
    def open_file(self):
        '''
        Open file-open dialog and load simulation from file
        '''
        filepath = QtGui.QFileDialog.getOpenFileName(self.centralwidget, "Open", self.controller.settings.get_default_folder())
        
        if filepath:
            self.controller.filemanager.load(filepath[0])
            
        self.paint.set_project(self.controller.projects.current())
        self.status_message()
        
    def status_message(self, message = None):
        
        if message is None:
            message = ""
            m = self.controller.messages.get_current()
            if m is not None:
                
                if m.success is False:
                    message += "Virhe. "
                    
                if m.reason is not None:
                    message += self.controller.messages.translate(m.reason)
                else:
                    message += self.controller.messages.translate(m)
                    
                if m.success is True:
                    message += " ok"
                
        self.statusbar.showMessage(QtGui.QApplication.translate("MainWindow", message, None, QtGui.QApplication.UnicodeUTF8))
        
