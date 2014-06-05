#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from cli.cli import Cli_Main
from core.controller import Controller

def main_gui(controller):
    '''
    Function executes Qt GUI
    '''
    
    from PySide import QtCore, QtGui
    from gui.main import Ui_Main
    
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    
    ui = Ui_Main(controller)
    ui.startMain(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    '''
    Starts application.
    '''
    argv1 = None
    controller = Controller()
    
    if len(sys.argv) > 1:
        argv1 = sys.argv[1]
    
    if argv1 == "gui":
        main_gui(controller)
    elif argv1 == "read":
        from cli.tur import Terminal_Ui_Reciever
        controller.messages.ui.set(Terminal_Ui_Reciever(), 'cli')
        controller.settings.set("current_filetype", 'gt')
        filepath = controller.filemanager.get_filepath(sys.argv[2])
        print "tiedosto: " + filepath
        controller.filemanager.load(filepath)
    else:
        ui = Cli_Main(controller, sys.argv)
        ui.start()

