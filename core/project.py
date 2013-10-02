#!/usr/bin/env python
# -*- coding: utf-8 -*-
from elements.elements import Elements


class Project(object):
    
    def __init__(self):
        
        self.title = None
        self.users = []
        
        self.elements = Elements()
