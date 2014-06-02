#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elements.point import Point
from elements.line import Line
from elements.polygon import Polygon
import os

class Project(object):
    
    def __init__(self, messages):
        
        self.messages = messages
        
        self.points = []
        self.lines = []
        self.polygons = []
        
        self.title = None
        self.filepath = None
        self.users = []
        self.saved = True
        self.draw = True
        
    def get_title(self):
        if self.title is not None:
            return self.title
        if self.filepath is not None:
            filename, file_extension = os.path.splitext(self.filepath)
            return filename + file_extension
        return '...'
        
    def is_empty(self):
        if len(self.points) > 0:
            return False
        if len(self.lines) > 0:
            return False
        if len(self.polygons) > 0:
            return False
        return True
        
    def get(self, element_type):
        if element_type == 'point':
            return self.points
        elif element_type == 'line':
            return self.lines
        elif element_type == 'polygon':
            return self.polygons
        else:
            return False
            
    def get_id(self, element_type, id):
        for element in self.get(element_type):
            if element.id == id:
                return element
        return False
        
    def new_point(self):
        return Point()
        
    def new_line(self):
        return Line()
        
    def new_polygon(self):
        return Polygon()
        
    def new(self, element_type):
        if element_type == 'point':
            return self.new_point()
        elif element_type == 'line':
            return self.new_line()
        elif element_type == 'polygon':
            return self.new_polygon()
        else:
            return False
        
    def save(self, element):
        m = self.messages.add("save " + element.type, "Project")
        
        if element.is_valid() is not True:
            self.messages.set_message_status(m, False, element.type + " is not valid")
            return False
        
        self.get(element.type).append(element)
        
        self.messages.set_message_status(m, True)
        self.saved = False
        return True
        
    def edit(self, element):
        m = self.messages.add("edit " + element.type, "Project")
        
        self.messages.set_message_status(m, True)
        self.saved = False
        return True
        
    def delete(self, element):
        m = self.messages.add("delete " + element.type, "Project")
        
        elements = self.get(element.type)
        if element in elements:
                elements.remove(element)
        
        self.messages.set_message_status(m, True)
        self.saved = False
        return True
        
    def is_in_range(self, elements, num):
        try:
            elements[num]
            return True
        except:
            return False
        
    def get_dictionary(self):
        
        data = {
            'title' : self.title
            }
        
        d = {
            'data' : data,
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
        
    def set_dictionary(self, d):
        
        if 'data' in d:
            if 'title' in d['data']:
                self.title = d['data']['title']
        
        for data in d['points']:
            p = self.new_point()
            p.set_dictionary(data)
            self.get('point').append(p)
        for data in d['lines']:
            l = self.new_line()
            l.set_dictionary(data)
            self.get('line').append(l)
        for data in d['polygons']:
            pl = self.new_polygon()
            pl.set_dictionary(data)
            self.get('polygon').append(pl)
        
        
