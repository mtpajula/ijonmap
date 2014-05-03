#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mxml import mXML
from mjson import mJson

class Filemanager(object):
    
    def __init__(self, messages, settings, projects):
        
        self.messages = messages
        self.settings = settings
        self.projects = projects
        
        self.filetypes = {
                    "mxml" : mXML(self.messages),
                    "json" : mJson(self.messages)
                    }
    
    def load(self):
        if self.settings.files["current_filetype"] in self.filetypes:
            self.filetypes[self.settings.files["current_filetype"]].load(self.settings, self.projects.new_project())
        
    def save(self):
        if self.settings.files["current_filetype"] in self.filetypes:
            self.filetypes[self.settings.files["current_filetype"]].save(self.settings, self.projects.current)
        
