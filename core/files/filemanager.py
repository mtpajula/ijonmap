#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mxml import mXML
from mjson import mJson
import os

class Filemanager(object):
    
    def __init__(self, messages, settings, projects):
        
        self.messages = messages
        self.settings = settings
        self.projects = projects
        
        self.filetypes = {
                    "mxml" : mXML(self.messages),
                    "json" : mJson(self.messages)
                    }
                    
    def current_filetype(self):
        return self.filetypes[self.settings.get("current_filetype")]
    
    def load(self, filepath):
        m = self.messages.add("load", "Filemanager")
        
        filename, file_extension = os.path.splitext(filepath)
        
        current_filetype_found = False
        for filetype in self.filetypes:
            if file_extension == self.filetypes[filetype].file_extension:
                self.settings.set("current_filetype", filetype)
                current_filetype_found = True
                break
                
        if not current_filetype_found:
            self.messages.set_message_status(m, False, "unknown filetype")
            return m
        
        self.messages.add("Filetype set to " + self.current_filetype().title, "Filemanager")
        project = self.projects.new_project()
        project.filepath = filepath
        
        return self.current_filetype().load(m, self.settings, project)
        
    def save(self):
        m = self.messages.add("save", "Filemanager")
        
        if self.projects.current.filepath is None:
            self.messages.set_message_status(m, False, "Filepath missing")
            return m
        
        filename, file_extension = os.path.splitext(self.projects.current.filepath)
        self.projects.current.filepath = filename + self.current_filetype().file_extension
        
        self.messages.add("Saving file to: " + self.projects.current.filepath, "Filemanager")
        
        return self.current_filetype().save(m, self.settings, self.projects.current)
        
    def get_filepath(self, filename, folder = None):
        if folder is None:
            filepath = self.settings.get_default_folder()
        else:
            filepath = folder
            
        filepath += filename
        filepath += self.current_filetype().file_extension
        
        return filepath


