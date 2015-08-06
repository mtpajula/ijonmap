#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .multielement import MultiElement

class Polygon(MultiElement):
    
    def __init__(self):
        super(Polygon, self).__init__()
        self.valid_points = 3
        self.type = 'polygon'

