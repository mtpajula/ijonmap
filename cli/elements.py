#!/usr/bin/env python
# -*- coding: utf-8 -*-
from template import Cli_Template

class Cli_Elements(Cli_Template):
    
    def __init__(self, controller):
        super(Cli_Elements, self).__init__()
        
        self.controller = controller
        
        self.title = "Elementit"
                
        self.commands["takaisin"] = None
        self.commands["piste"] = self.new_point
        self.commands["viiva"] = self.new_line
        self.commands["polygoni"] = self.new_polygon
        self.commands["kaikki"] = self.print_elements
        self.commands["poista"] = self.delete_element
        
    def print_elements(self):
        self.print_element_list(self.controller.projects.current.points)
        self.print_element_list(self.controller.projects.current.lines)
        self.print_element_list(self.controller.projects.current.polygons)
            
    def print_element_list(self, elements):
        print ""
        for i, e in enumerate(elements):
            print '[' + str(i)  + '] ' + e.get_str()
    
    def delete_element(self):
        print 'point, line vai polygon?'
        t = raw_input("tyyppi: ")
        elements = self.controller.projects.current.get(t)
        if elements is False:
            print " ! tyyppi ei ole kelvollinen, yritä uudelleen"
            return self.new_single_point()
            
        print ''
        print 'valitse poistettava elementti'
        self.print_element_list(elements)
        num = int(raw_input("numero: "))
        if self.controller.projects.current.is_in_range(elements, num):
            self.controller.projects.current.delete(elements[num])
        else:
            print " ! numeroa " + str(num) + ' ei löydy listalta'

    def select_from_list(self, list):
        for i, item in enumerate(list):
            print 
    
    def new_point(self):
        point = self.new_single_point()
        self.controller.projects.current.save(point)
    
    def new_single_point(self):
        point = self.controller.projects.current.new_point()
        point.id = raw_input(point.type + " id: ")
        x = raw_input("x: ")
        y = raw_input("y: ")
        z = raw_input("z: ")
        point.add_coordinates(x,y,z)
        if point.is_valid():
            return point
        else:
            print " ! Piste ei ole kelvollinen, yritä uudelleen"
            return self.new_single_point()

    def new_line(self):
        line = self.controller.projects.current.new_line()
        self.new_multielement(line)
        self.controller.projects.current.save(line)
        
    def new_multielement(self, m_element):
        
        m_element.id = raw_input(m_element.type + " id: ")
        
        while (True):
            if m_element.enough_points() is True:
                q = raw_input("Uusi piste? (k/e): ")
            else:
                q = "k"
            
            if q == "k":
                point = self.new_single_point()
                m_element.add(point)
            elif q == "e":
                break
        
    def new_polygon(self):
        polygon = self.controller.projects.current.new_polygon()
        self.new_multielement(polygon)
        self.controller.projects.current.save(polygon)
