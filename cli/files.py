#!/usr/bin/env python
# -*- coding: utf-8 -*-
from template import Cli_Template

class Cli_Files(Cli_Template):
    
    def __init__(self, controller):
        super(Cli_Files, self).__init__()
        
        self.controller = controller
        
        self.title = "Tiedostot"
                
        self.commands["takaisin"] = None
        self.commands["tallenna"] = self.save
        self.commands["avaa"] = self.load
        self.commands["valitse"] = self.select_filetype
           
    def save(self):
        
        if self.controller.projects.current().filepath is None:
            self.save_as()
            return
        
        self.controller.filemanager.save()
    
    def save_as(self):
        print "tallennetaan kansioon: " + self.controller.settings.get_default_folder()
        print "Tiedostomuoto: " + self.controller.filemanager.current_filetype().title
        
        ans = raw_input("Anna tiedoston nimi: ")
        if ans == "":
            ans = "test"
        
        self.controller.projects.current().filepath = self.controller.filemanager.get_filepath(ans)
        self.controller.filemanager.save()
        
    def load(self):
        filepath = self.controller.filemanager.get_filepath("test")
        print "tiedosto: " + filepath
        self.controller.filemanager.load(filepath)
        
    def select_filetype(self):
        print "tiedostomuoto nyt: " + self.controller.settings.get("current_filetype")
        print "tiedostomuodot: ",
        for filetype in self.controller.filemanager.filetypes:
            print filetype,
        print ""
        while (True):
            ans = raw_input("Anna tiedostomuoto: ")
            if ans in self.controller.filemanager.filetypes:
                self.controller.settings.set("current_filetype", ans)
                break
            print " ! Tiedostomuotoa ei ole olemassa"
