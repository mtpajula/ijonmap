#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Element(object):
    
    def __init__(self):
        self.id = None
        self.type = None
        self.code = None
        self.table_id = None
        
    def get_str(self):
        s = self.type + " id: "
        s += str(self.id)
        s += " code: "
        s += str(self.code)
        return s
        
    def get_dictionary(self):
        d = {
                    'id' : self.id,
                    'type' : self.type,
                    'code' : self.code,
                    'table_id' : self.table_id
                    }
        return d
        
    def set_dictionary(self, d):
        self.id = d['id']
        self.type = d['type']
        self.code = d['code']
        self.table_id = d['table_id']
        
        

