#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .template import Cli_Template
from .project import Cli_Project

class Cli_Projects(Cli_Template):
    
    def __init__(self, projects):
        super(Cli_Projects, self).__init__()
        
        self.projects = projects
        
        self.title = "Projektit"
                
        self.commands["takaisin"] = None
        self.commands["projekti"] = self.project
        self.commands["uusi"] = self.new
        self.commands["kaikki"] = self.print_projects
        self.commands["aktiivinen"] = self.print_current
        self.commands["valitse"] = self.select_current
        self.commands["uusi"] = self.new
        self.commands["poista"] = self.delete
        
    def project(self):
        
        if self.projects.current() is None:
            print(" ! Ei valittuna aktiivista projektia")
        
        cli = Cli_Project(self.projects.current())
        cli.add_level(2)
        cli.start()
        
    def delete(self):
        print('valitse projekti poistettavaksi')
        self.print_projects()
        num = int(input("numero: "))
        self.projects.delete(num)
        
    def new(self):
        self.projects.new_project()
        
    def select_current(self):
        print('valitse projekti aktiiviseksi')
        self.print_projects()
        num = int(input("numero: "))
        self.projects.set_current(num)
        
    def print_projects(self):
        print('')
        for i, p in enumerate(self.projects.get_all()):
            print('[' + str(i)  + '] ', end=' ')
            self.print_project(p)
            print('')
            
    def print_current(self):
        self.print_project(self.projects.current())
            
    def print_project(self, p):
        
        if p is None:
            print(" ! ei projektia")
            return
        
        print('=== projekti: ' + str(p.title) + ' ===')
        print(p.filepath)
        print('pisteitä: ' + str(len(p.points)))
        print('viivoja: ' + str(len(p.lines)))
        print('polygoneja: ' + str(len(p.polygons)))
        print('tallennettu: ' + str(p.saved))
        print('========')
        
        
