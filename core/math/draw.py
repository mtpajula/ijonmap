#!/usr/bin/env python
# -*- coding: utf-8 -*-

class DrawCalculator(object):
    
    def __init__(self):
        
        self.scale_factor = 1
        self.center_x = 100
        self.center_y = 100
        
        self.loop_data = {}
    
    def scale_point(self, point):
        '''
        Scales object locations for QPainter
        '''
        x = self.scale_factor * point.x
        y = self.scale_factor * point.y
        
        x = int(  + x )
        y = int(  - y )
        
        return ( x, y )
        
    def get_scale_factor(self, width, height):
        '''
        Calculates scale factor
        '''
        
        if 'max_x' not in self.loop_data:
            return
        
        dx = self.loop_data['max_x'] - self.loop_data['min_x']
        dy = self.loop_data['max_y'] - self.loop_data['min_y']
        
        sx = width / dx
        sy = height / dy
        
        if sx > sy:
            self.scale_factor = sy
            return
        self.scale_factor = sx
        
    def center_in_project(self, project):
        
        if project.is_empty():
            return
        
        d = self.loop_project(project)
        self.center_x = int((d['max_x'] + d['min_x'])/2)
        self.center_y = int((d['max_y'] + d['min_y'])/2)
        
    def loop_project(self, project):
        
        self.loop_data['max_x'] = float("-inf")
        self.loop_data['max_y'] = float("-inf")
        self.loop_data['min_x'] = float("+inf")
        self.loop_data['min_y'] = float("+inf")
        
        for p in project.points:
            self.loop_point(p)
            
        for l in project.lines:
            for p in l.points:
                self.loop_point(p)
                
        for pl in project.polygons:
            for p in pl.points:
                self.loop_point(p)
                
        return self.loop_data
        
    def loop_point(self, p):
        if p.x > self.loop_data['max_x']:
            self.loop_data['max_x'] = p.x
        if p.y > self.loop_data['max_y']:
            self.loop_data['max_y'] = p.y
            
        if p.x < self.loop_data['min_x']:
            self.loop_data['min_x'] = p.x
        if p.y < self.loop_data['min_y']:
            self.loop_data['min_y'] = p.y
    
