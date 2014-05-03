#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Element(object):
    
    def __init__(self):
        self.id = None
        self.type = None
        self.table_id = None
        self.features = {}
        
    def get_str(self):
        s = self.type + " id: "
        s += str(self.id)
        s += " features: "
        s += str(self.features)
        return s
        
    def get_dictionary(self):
        d = {
                    'id' : self.id,
                    'type' : self.type,
                    'table_id' : self.table_id,
                    'features' : self.features
                    }
        return d
        
    def set_dictionary(self, d):
        self.id = d['id']
        self.type = d['type']
        self.table_id = d['table_id']
        self.features = d['features']
        
        

