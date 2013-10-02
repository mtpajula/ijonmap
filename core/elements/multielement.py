#!/usr/bin/env python
# -*- coding: utf-8 -*-
from element import Element

class MultiElement(Element):
    
    def __init__(self):
        super(MultiElement, self).__init__()
        self.points = []
        self.valid_points = 2
        
    def add(self, point):
        self.points.append(point)
        
    def is_valid(self):
        
        for point in self.points:
            if point.is_valid() is not True:
                return False
        
        return self.enough_points()
        
    def enough_points(self):
        if len(self.points) >= self.valid_points:
            return True
        return False
        
    def get_str(self):
        s = Element.get_str(self)
        for point in self.points:
            s += "\n\t" + point.get_str()
        
        return s
    
    def get_dictionary(self):
        d = Element.get_dictionary(self)
        d['points'] = []
        for point in self.points:
            d['points'].append(point.get_dictionary())
        
        return d



