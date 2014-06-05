#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mxml import mXML
from mjson import mJson
from mcsv import mCsv
from mgt import mGt
import os

class Filemanager(object):
    
    def __init__(self, settings, projects):
        
        self.messages = projects.messages
        self.settings = settings
        self.projects = projects
        
        self.filetypes = {
                    "mxml" : mXML(),
                    "json" : mJson(),
                    "csv" : mCsv(),
                    "gt" : mGt()
                    }
                    
    def current_filetype(self):
        return self.filetypes[self.settings.get("current_filetype")]
    
    def load(self, filepath):
        m = self.messages.add("load", "Filemanager")
        
        for p in self.projects.p:
            if p.filepath == filepath:
                self.messages.set_message_status(m, False, "File is open already")
                return m
        
        filename, file_extension = os.path.splitext(filepath)
        
        current_filetype_found = False
        for filetype in self.filetypes:
            if file_extension == self.filetypes[filetype].file_extension:
                self.settings.set("current_filetype", filetype)
                self.messages.add("Filetype set to " + self.current_filetype().title, "Filemanager")
                current_filetype_found = True
                break
                
        if not current_filetype_found:
            self.messages.set_message_status(m, False, "unknown filetype")
            return m
        
        project = self.projects.new_project()
        project.filepath = filepath
        
        return self.current_filetype().load(m, self.settings, project)
        
    def save(self):
        m = self.messages.add("save", "Filemanager")
        
        if self.projects.current() is None:
            self.messages.set_message_status(m, False, "current project missing")
            return m
        
        if self.projects.current().filepath is None:
            self.messages.set_message_status(m, False, "Filepath missing")
            return m
        
        filename, file_extension = os.path.splitext(self.projects.current().filepath)
        self.projects.current().filepath = filename + self.current_filetype().file_extension
        
        self.messages.add("Saving file to: " + self.projects.current().filepath, "Filemanager")
        
        m = self.current_filetype().save(m, self.settings, self.projects.current())
        self.projects.current().saved = m.success
        return m
        
    def get_filepath(self, filename, folder = None):
        if folder is None:
            filepath = self.settings.get_default_folder()
        else:
            filepath = folder
            
        filepath += filename
        filepath += self.current_filetype().file_extension
        
        return filepath


