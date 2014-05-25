#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

class mCsv(object):
    
    def __init__(self):
        
        self.title = "read csv files"
        self.file_extension = '.txt'
        
        #self.columns = ['surface_id','line_id','code','id','x','y','z']
        self.columns = ['x','y','z']
        
        self.delimiter = ' '
        self.line_id_column = None
        self.polygon_id_column = None
        self.elements = []
        
    def load(self, m, settings, project):
        
        self.get_multielement_columns()
        
        try:
            
            with open(project.filepath, 'rb') as csvfile:
                
                dialect = csv.excel
                dialect.delimiter = self.delimiter
                dialect.skipinitialspace = True
                
                reader = csv.reader(csvfile, dialect)
                
                for row in reader:
                    self.read_row(project, row)
                
            for e in self.elements:
                project.save(e)
            self.elements[:] = []
            
            project.messages.set_message_status(m, True)
            return m
        except Exception, e:
            project.messages.set_message_status(m, False, str(e))
            return m
            
    def read_row(self, project, row):
        
        try:
            if len(row) == len(self.columns):
                
                p = project.new_point()
                
                for i, column in enumerate(self.columns):
                    if column == 'x':
                        p.add_x(row[i])
                    elif column == 'y':
                        p.add_y(row[i])
                    elif column == 'z':
                        p.add_z(row[i])
                    elif column == 'id':
                        p.id = row[i]
                    elif column == 'title':
                        p.title = row[i]
                    elif column == 'table_id':
                        p.table_id = row[i]
                    else:
                        p.features[column] =  row[i]
                
                if self.manage_multielement(project, row, p) is False:
                    self.elements.append(p)
                
            else:
                project.messages.error("column count is wrong", "read_row", 'row: '+str(row)+')')
            
        except Exception, e:
            project.messages.error("load row", "read_row", str(e)+' (row: '+str(row)+')')
        
    def manage_multielement(self, project, row, p):
        
        multielement_id = None
        
        if self.polygon_id_column is not None:
            if row[self.polygon_id_column] != '0':
                multielement_id = row[self.polygon_id_column]
                multielement_type = 'polygon'
        
        if self.line_id_column is not None:
            if row[self.line_id_column] != '0':
                multielement_id = row[self.line_id_column]
                multielement_type = 'line'
            
        if multielement_id is None:
            return False
            
        for e in self.elements:
            if e.id == multielement_id and e.type == multielement_type:
                e.add(p)
                return True
        
        e = project.new(multielement_type)
        e.id = multielement_id
        e.add(p)
        self.elements.append(e)
        return True
        
    def get_multielement_columns(self):
        
        for i, col in enumerate(self.columns):
            if col == 'line_id':
                self.line_id_column = i
            elif col == 'polygon_id':
                self.polygon_id_column = i
            
            
        
    def save(self, m, settings, project):
                
        try:
            
            
            
            project.messages.set_message_status(m, True)
            return m
        except Exception, e:
            project.messages.set_message_status(m, False, str(e))
            return m
