#!/usr/bin/env python
# -*- coding: utf-8 -*-
from .template import Cli_Template

class Cli_Project(Cli_Template):
    
    def __init__(self, project):
        super(Cli_Project, self).__init__()
        
        self.project = project
        
        self.title = "Projekti"
                
        self.commands["takaisin"] = None
        self.commands["piste"] = self.new_point
        self.commands["viiva"] = self.new_line
        self.commands["polygoni"] = self.new_polygon
        self.commands["kaikki"] = self.print_elements
        self.commands["poista"] = self.delete_element
        
    def project_name(self):
        pass
        
    def print_elements(self):
        self.print_element_list(self.project.points)
        self.print_element_list(self.project.lines)
        self.print_element_list(self.project.polygons)
            
    def print_element_list(self, elements):
        print("")
        for i, e in enumerate(elements):
            print('[' + str(i)  + '] ' + e.get_str())
    
    def delete_element(self):
        print('point, line vai polygon?')
        t = input("tyyppi: ")
        elements = self.project.get(t)
        if elements is False:
            print(" ! tyyppi ei ole kelvollinen, yritä uudelleen")
            return self.new_single_point()
            
        print('')
        print('valitse poistettava elementti')
        self.print_element_list(elements)
        num = int(input("numero: "))
        if self.project.is_in_range(elements, num):
            self.project.delete(elements[num])
        else:
            print(" ! numeroa " + str(num) + ' ei löydy listalta')

    def select_from_list(self, list):
        for i, item in enumerate(list):
            print('')
    
    def new_point(self):
        point = self.new_single_point()
        self.project.save(point)
    
    def new_single_point(self):
        point = self.project.new_point()
        point.id = input(point.type + " id: ")
        x = input("x: ")
        y = input("y: ")
        z = input("z: ")
        point.add_coordinates(x,y,z)
        if point.is_valid():
            return point
        else:
            print(" ! Piste ei ole kelvollinen, yritä uudelleen")
            return self.new_single_point()

    def new_line(self):
        line = self.project.new_line()
        self.new_multielement(line)
        self.project.save(line)
        
    def new_multielement(self, m_element):
        
        m_element.id = input(m_element.type + " id: ")
        
        while (True):
            if m_element.enough_points() is True:
                q = input("Uusi piste? (k/e): ")
            else:
                q = "k"
            
            if q == "k":
                point = self.new_single_point()
                m_element.add(point)
            elif q == "e":
                break
        
    def new_polygon(self):
        polygon = self.project.new_polygon()
        self.new_multielement(polygon)
        self.project.save(polygon)
