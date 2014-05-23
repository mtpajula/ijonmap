#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui


class PaintWidget(QtGui.QWidget):
    '''
    QWidged where paint happens
    '''
    
    def __init__(self, calc, projects):
        QtGui.QWidget.__init__(self)
        self.calc = calc
        self.projects = projects
        
        self.show_all = True
        
    def set_project(self, project):
        self.project = project
        self.repaint()
        
    def paintEvent(self, event):
        '''
        Event in painter
        '''
        qp = QtGui.QPainter()
        qp.begin(self)
        qp.setRenderHint(QtGui.QPainter.Antialiasing)
        
        self.set_center(qp)
        
        if self.show_all is True:
            self.show_all_scale(qp)
        else:
            qp.scale(self.calc.scale_factor,self.calc.scale_factor)
        
        qp.setFont(QtGui.QFont('Decorative', 10))
        
        qp.setPen(QtGui.QColor(168, 34, 3))
        self.drawPoints(qp)
        qp.setPen(QtGui.QColor(5, 34, 100))
        self.drawLines(qp)
        qp.setPen(QtGui.QColor(10, 100, 3))
        self.drawPolygons(qp)

        qp.end()

    def drawPoints(self, qp):
        
        for p in self.projects.current().points:
            self.drawPoint(qp, p)
            
    def drawLines(self, qp):
        for l in self.projects.current().lines:
            self.drawMultiElement(qp, l)
            
    def drawPolygons(self, qp):
        for element in self.projects.current().polygons:
            #self.drawMultiElement(qp, l)
            
            polygon = QtGui.QPolygon()
            
            for p in element.points:
                point = self.drawPoint(qp, p)
                polygon.append(point)
                
            qp.drawPolygon(polygon)
            
    def drawMultiElement(self, qp, element, polygon = False):
        
        last_point = None
        first_point = None
        
        for i, p in enumerate(element.points):
            point = self.drawPoint(qp, p)
            
            if i == 0:
                first_point = point
            
            if last_point:
                qp.drawLine(last_point, point)
                
            last_point = point
            
        if polygon is True:
            qp.drawLine(last_point, first_point)
        
    def drawPoint(self, qp, p):
        ( x, y ) = self.get_point_xy(p)
        point = QtCore.QPoint(x, y)
        size = 5
        qp.drawText(x-15, y-15, p.id)     
        qp.drawEllipse(point, size, size)
        return point
        
    def show_all_scale(self, qp):
        s1 = (qp.device().width()/2)/float(self.calc.center_x)
        s2 = (qp.device().height()/2)/float(self.calc.center_y)
        
        if s1 > s2:
            self.calc.scale_factor = s2
        else:
            self.calc.scale_factor = s1
            
        print self.calc.scale_factor, self.calc.center_x, self.calc.center_y
    
    def set_center(self, qp):
        
        cx = qp.device().width() / 2
        cy = qp.device().height() / 2
        
        cx = cx - self.calc.center_x
        cy = cy + self.calc.center_y
        
        qp.translate(cx, cy)

    def get_point_xy(self, p):
        return ( int(  + p.x ), int(  - p.y ) )


