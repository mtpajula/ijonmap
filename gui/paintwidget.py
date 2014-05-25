#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide import QtCore, QtGui

class PaintPoint(object):
    def __init__(self, x, y, title):
        self.x = x
        self.y = y
        self.title = title


class PaintWidget(QtGui.QWidget):
    '''
    QWidged where paint happens
    '''
    
    def __init__(self, calc, project):
        QtGui.QWidget.__init__(self)
        self.calc = calc
        self.project = project
        
        self.show_all = False
        
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
        
        if self.show_all is True:
            self.calc.center_in_project(self.project)
            self.calc.get_scale_factor(qp.device().width(), qp.device().height())
            # Marginal
            self.calc.scale_factor = self.calc.scale_factor * 0.9
            
        (cx,cy) = self.set_center(qp)
        
        qp.setFont(QtGui.QFont('Decorative', 10))
        
        qp.setPen(QtGui.QColor(168, 34, 3))
        self.drawPoints(qp)
        qp.setPen(QtGui.QColor(5, 34, 100))
        self.drawLines(qp)
        qp.setPen(QtGui.QColor(10, 100, 3))
        self.drawPolygons(qp)
        qp.end()

    def drawPoints(self, qp):
        
        for p in self.project.points:
            self.drawPoint(qp, p)
            
    def drawLines(self, qp):
        for l in self.project.lines:
            self.drawLine(qp, l)
            
    def drawPolygons(self, qp):
        for element in self.project.polygons:
            polygon = QtGui.QPolygon()
            
            for p in element.points:
                point = self.drawPoint(qp, p)
                polygon.append(point)
                
            qp.drawPolygon(polygon)
            
    def drawLine(self, qp, element):
        
        last_point = None
        
        for i, p in enumerate(element.points):
            point = self.drawPoint(qp, p)
            
            if last_point:
                qp.drawLine(last_point, point)
                
            last_point = point
        
    def drawPoint(self, qp, p):
        ( x, y ) = self.calc.scale_point(p)
        point = QtCore.QPoint(x, y)
        size = 5
        qp.drawText(x+15, y-10, p.id)     
        qp.drawEllipse(point, size, size)
        return point
    
    def set_center(self, qp):
        
        cx = qp.device().width() / 2
        cy = qp.device().height() / 2
        
        cx = cx - self.calc.center_x * self.calc.scale_factor
        cy = cy + self.calc.center_y * self.calc.scale_factor
        
        qp.translate(cx, cy)
        return (cx, cy)
