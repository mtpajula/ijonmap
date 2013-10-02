#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from cli.cli import Cli_Main
from core.controller import Controller

if __name__ == "__main__":
    '''
    Starts application.
    '''
    argv1 = None
    controller = Controller()
    
    if len(sys.argv) > 1:
        argv1 = sys.argv[1]
    
    if argv1 == "gui":
        print "no graphical user interface"
    else:
        ui = Cli_Main(controller, sys.argv)
        ui.start()

