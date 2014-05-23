#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

class mJson(object):
    
    def __init__(self):
        
        self.title = "custom json filetype"
        self.file_extension = '.json'
    
    def load(self, m, settings, project):
        
        try:
            with open(project.filepath) as outfile:
                d = json.load(outfile)
                
            settings.set_dictionary(d['settings'])
            project.set_dictionary(d['project'])
            
            project.messages.set_message_status(m, True)
        except Exception, e:
            project.messages.set_message_status(m, False, str(e))
        
        return m
        
    def save(self, m, settings, project):
        
        try:
            d = {
                'settings' : settings.get_dictionary(),
                'project' : project.get_dictionary()
                }
            print json.dumps(d, sort_keys=True, indent=4, separators=(',', ': '))
            
            with open(project.filepath, 'w') as outfile:
                json.dump(d, outfile)
            
            project.messages.set_message_status(m, True)
        except Exception, e:
            project.messages.set_message_status(m, False, str(e))
        
        return m
