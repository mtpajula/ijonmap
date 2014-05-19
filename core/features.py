#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Features(object):
    
    def __init__(self):
        
        self.f = []
        
    def get(self, title):
        for f in self.f:
            if title == f.title:
                return f
        return None
        
    def new(self, title):
        
        for f in self.f:
            if title == f.title:
                return None
        
        new_f = Feature(title)
        self.f.append(new_f)
        return new_f
        
    def delete(self, title):
        del_list = []
        for i, f in enumerate(self.f):
            if title == f.title:
                del_list.append(i)
                
        for i in del_list:
            del self.f[i]
        
class Feature(object):
    
    def __init__(self, title):
        
        self.title = title
        self.data = {}
        
    def value(self, title):
        return self.data[title]
        
    def set_value(self, title, value):
        self.data[title] = value
        
        
        
