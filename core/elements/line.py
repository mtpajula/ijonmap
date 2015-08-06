#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .multielement import MultiElement

class Line(MultiElement):
    
    def __init__(self):
        super(Line, self).__init__()
        self.type = 'line'
