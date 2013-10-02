#!/usr/bin/env python
# -*- coding: utf-8 -*-
from point import Point
from line import Line
from polygon import Polygon

class Elements(object):
    
    def __init__(self):
        self.points = []
        self.lines = []
        self.polygons = []
        
    def new_point(self):
        return Point()
        
    def new_line(self):
        return Line()
        
    def new_polygon(self):
        return Polygon()
        
    def save(self, element):
        if element.is_valid() is not True:
            return False
        
        if element.type == 'point':
            self.points.append(element)
            return True
        elif element.type == 'line':
            self.lines.append(element)
            return True
        elif element.type == 'polygon':
            self.polygons.append(element)
            return True
            
        return False
        
    def get_dictionary(self):
        d = {
            'points' : [],
            'lines' : [],
            'polygons' : []
            }
        
        for point in self.points:
            d['points'].append(point.get_dictionary())
        for line in self.lines:
            d['lines'].append(line.get_dictionary())
        for polygon in self.polygons:
            d['polygons'].append(polygon.get_dictionary())
        
        return d
        
