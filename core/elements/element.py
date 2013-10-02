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
                    'code' : None,
                    'table_id' : self.table_id
                    }
                    
        if self.code is not None:
            d['code'] = self.code.get_dictionary()
                    
        return d

