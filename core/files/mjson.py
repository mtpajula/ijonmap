#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class mJson(object):
    
    def __init__(self, messages):
        
        self.messages = messages
        self.title = "custom json filetype"
        self.file_extension = '.json'
    
    def load(self, settings, project):
        m = self.messages.add("load", "mJson")
        
        try:
            
            with open(project.filepath) as outfile:
                d = json.load(outfile)
                
            settings.set_dictionary(d['settings'])
            project.elements.set_dictionary(d['elements'])
            
            self.messages.set_message_status(m, True)
            return m
        except Exception, e:
            self.messages.set_message_status(m, False, str(e))
            return m
        
    def save(self, settings, project):
        m = self.messages.add("save", "mJson")
        
        try:
            d = {
                'settings' : settings.get_dictionary(),
                'elements' : project.elements.get_dictionary()
                }
            print json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
            
            with open(project.filepath, 'w') as outfile:
                json.dump(d, outfile)
            
            self.messages.set_message_status(m, True)
            return m
        except Exception, e:
            self.messages.set_message_status(m, False, str(e))
            return m
