#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Cli_Template(object):
    
    def __init__(self):
        
        self.title = "Template"
        self.level = 0
        self.commands = {
                    "lopeta" : self.exit_system,
                    "komennot" : self.print_commands
                    }
                    
    def add_level(self, level = None):
        if level is None:
            self.level += 1
        else:
            self.level = level
        
    def start(self):
        
        while (True):
            
            syote = input("[ " + str(self.level) + " ]: ")
            
            if syote in self.commands:
                
                if self.commands[syote] is None:
                    break
                else:
                    self.commands[syote]()
            else:
                print("\n ! tuntematon komento")
    
    def exit_system(self):
        sys.exit()
    
    def print_commands(self):
        print("\n == " + self.title + ". Komennot ==> ")
        first = False
        for s in self.commands:
            if first is True:
                print(", ", end=' ')
            print(s, end=' ')
            first = True
            
        print("")
        
