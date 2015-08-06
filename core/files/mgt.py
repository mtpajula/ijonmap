#!/usr/bin/env python
# -*- coding: utf-8 -*-

class mGt(object):
    
    def __init__(self):
        
        self.title = "read GT-format files"
        self.file_extension = '.xyz'
        
        self.elements = []
        
        self.columns = [
                ['surface_id', {'from' : 0, 'to': 8}],
                ['line_id', {'from' : 8, 'to':16}],
                ['code', {'from' : 16, 'to': 24}],
                ['id', {'from' : 24, 'to': 32}],
                ['y', {'from' : 32, 'to': 46}],
                ['x', {'from' : 46, 'to': 60}],
                ['z', {'from' : 60, 'to': 74}]
            ]
        
    def load(self, m, settings, project):
        
        try:
            
            with open(project.filepath, 'rb') as gtfile:
                
                rows = gtfile.readlines()
                
                for row in rows:
                    self.read_row(project, row)
            
            
            for e in self.elements:
                project.save(e, False)
            self.elements[:] = []
            
            
            project.messages.set_message_status(m, True)
            return m
        except Exception as e:
            project.messages.set_message_status(m, False, str(e))
            return m
        
    def read_row(self, project, row):
        
        try:
            if len(row) >= 74:
                p = project.new('point')
                
                for c in self.columns:
                    self.read_cell(p, c[0], row[c[1]['from']:c[1]['to']].strip())
                    
                if p.features['line_id'] != '0':
                    for e in self.elements:
                        if e.type == 'line' and e.id == p.features['line_id']:
                            e.add(p)
                            del p.features['line_id']
                            return
                    
                    e = project.new('line')
                    e.id = p.features['line_id']
                    e.add(p)
                    self.elements.append(e)
                    del p.features['line_id']
                    return
                    
                del p.features['line_id']
                self.elements.append(p)
            else:
                project.messages.error('read row', 'read_row', 'row too short Row: ' + row)
                
        except Exception as e:
            project.messages.error('read row', 'read_row', str(e) + ' Row: ' + row)
                
    def read_cell(self, p, column, cell):
        if column == 'x':
            p.add_x(cell)
        elif column == 'y':
            p.add_y(cell)
        elif column == 'z':
            p.add_z(cell)
        elif column == 'id':
            p.id = cell
        else:
            p.features[column] = cell

    def save(self, m, settings, project):
                
        try:
            
            with open(project.filepath, 'wb') as gtfile:
                pass
            
            project.messages.set_message_status(m, True)
            return m
        except Exception as e:
            project.messages.set_message_status(m, False, str(e))
            return m
            
    def build_row(self, point):
        pass
        
