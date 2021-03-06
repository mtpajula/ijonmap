#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .project import Project

class Projects(object):
    
    def __init__(self, messages):
        
        # TODO if current() and if current.filepath
        
        self.messages = messages
        self.p = []
        self.current_index = None
        
    def current(self):
        if self.current_index is None:
            return None
        if not self.is_in_range(self.current_index):
            return None
        
        return self.p[self.current_index]
        
    def set_current(self, num):
        m = self.messages.add("set current", "Projects")
        if self.is_in_range(num, m):
            self.current_index = num
        
    def new_project(self):
        new = Project(self.messages)
        self.p.append(new)
        self.current_index = len(self.p) - 1
        self.messages.add("new project created", "Projects")
        return new
        
    def open(self, num):
        m = self.messages.add("open project", "Projects")
        if self.is_in_range(num, m):
            project = self.p[num]
            self.current_index = num
            return project
        return None
        
    def is_in_range(self, num, m = None):
        if num >= 0 and len(self.p) > num:
            return True
            
        if m is not None:
            self.messages.set_message_status(m, False, "out of range")
        return False
        
    def delete(self, num):
        m = self.messages.add("delete project", "Projects")
        if self.is_in_range(num):
            del self.p[num]
            
            if self.current_index == num:
                self.current_index = None
            
            return True
        return False
        
    def delete_all(self):
        for i, p in enumerate(self.p):
            self.delete(i)
            
    def is_empty(self):
        empty = True
        for p in self.p:
            if p.is_empty() is False:
                empty = False
        return empty
        
    def get_all(self):
        return self.p
