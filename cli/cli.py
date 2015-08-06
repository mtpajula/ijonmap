#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .tur import Terminal_Ui_Reciever
from .template import Cli_Template
from .projects import Cli_Projects
from .files import Cli_Files

class Cli_Main(Cli_Template):
    
    def __init__(self, controller, argv):
        super(Cli_Main, self).__init__()
        
        self.argv = argv
        self.controller = controller
        self.controller.messages.ui.set(Terminal_Ui_Reciever(), 'cli')
        
        self.title = "Päävalikko"
        
        self.commands["viestit"] = self.print_messages
        self.commands["asetukset"] = self.print_settings
        self.commands["projektit"] = self.projects
        self.commands["tiedostot"] = self.files
            
    def print_settings(self):
        print("\n == Asetukset ==> ")
        for s in self.controller.settings.get_dictionary():
            w = " " * (30 - len(s))
            print(" > " + s + ":" + w + str(self.controller.settings.get(s)))
    
    def print_messages(self):
        print("\n == Viestit ==> ")
        self.controller.messages.ui.get('cli').print_messagelist(self.controller.messages.m)
        
    def projects(self):
        cli = Cli_Projects(self.controller.projects)
        cli.add_level()
        cli.start()
        
    def files(self):
        cli = Cli_Files(self.controller)
        cli.add_level()
        cli.start()
