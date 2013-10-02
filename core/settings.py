#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class Settings(object):
    
    def __init__(self):
        
        self.project_folder = os.getcwd()
        
        self.controller = {
                        "test" : "setting"
                    }
        
        self.files = {
                        "current_filetype" : "json",
                        "folder" : self.project_folder + "/testdata/",
                        "filename" : "test.json"
                    }
                    
    def get_all(self):
        d = dict(self.files.items() + self.controller.items())
        return d
        
    def get(self, title):
        d = self.get_all()
        return d[title]
        
    def get_filepath(self):
        return self.files["folder"] + self.files["filename"]
