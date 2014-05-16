#!/usr/bin/env python
# -*- coding: utf-8 -*-
from project import Project

class Projects(object):
    
    def __init__(self, messages):
        
        self.messages = messages
        self.p = []
        self.current = None
        
    def new_project(self):
        new = Project(self.messages)
        self.p.append(new)
        self.current = new
        return new
        
    def open(self, num):
        if num >= 0 and len(self.p) > num:
            project = self.p[num]
            self.current = project
            return project
        return None
