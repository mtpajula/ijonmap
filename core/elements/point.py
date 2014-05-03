#!/usr/bin/env python
# -*- coding: utf-8 -*-
from element import Element

class Point(Element):
    
    def __init__(self):
        super(Point, self).__init__()
        self.x = 0
        self.y = 0
        self.z = 0
        self.type = 'point'
        
    def add_coordinates_revert_to_zero(self, x, y, z = 0):
        
        if self.is_num(x):
            self.x = float(x)
        if self.is_num(y):
            self.y = float(y)
        if self.is_num(z):
            self.z = float(z)
            
    def add_coordinates(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
        
    def is_valid(self):
        if self.is_num(self.x) is not True:
            return False
        
        if self.is_num(self.y) is not True:
            return False
            
        if self.is_num(self.z) is not True:
            return False
            
        return True
        
    def is_num(self, num):
        try:
            float(num)
            return True
        except ValueError:
            return False
            
    def get_str(self):
        s = Element.get_str(self)
        s += " x,y,z: "
        s += str(self.x) + ","
        s += str(self.y) + ","
        s += str(self.z)
        return s
        
    def get_dictionary(self):
        d = Element.get_dictionary(self)
        d['x'] = self.x
        d['y'] = self.y
        d['z'] = self.z
        return d
        
    def set_dictionary(self, d):
        Element.set_dictionary(self, d)
        self.x = d['x']
        self.y = d['y']
        self.z = d['z']
        
        
