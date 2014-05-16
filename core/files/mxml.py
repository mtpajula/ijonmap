#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.dom.minidom as dom
from lxml import etree
from itertools import groupby

class mXML(object):
    
    def __init__(self):
        
        self.title = "custom xml filetype"
        self.file_extension = '.xml'
    
    def load(self, m, settings, projects):
        m = self.messages.add("load", "mXML")
        
        try:
            '''
            # xml parse to DOM
            doc = dom.parse(settings.files["filepath"])
            
            # Get settings
            root = doc.getElementsByTagName("settings")[0]
            self.get_settings(root)
            self.set_source(self.settings["source"])
            '''
            self.messages.set_message_status(m, True)
            return m
        except Exception, e:
            self.messages.set_message_status(m, False, str(e))
            return m
        
    def save(self, m, settings, project):
        m = self.messages.add("load", "mXML")
        
        '''
        # Generate DOM
        doc = self.generate()
        
        # Pretty xml :)
        docString = doc.toprettyxml("    ", "\n", "utf-8")
        '''
        # Write file
        d = {'mxml' : {
                'settings' : settings.__dict__,
                'elements' : project.elements.get_dictionary()
                }}
        
        #print etree.tostring(self.d2xml(d))
        doc = dom.parseString(etree.tostring(self.d2xml(d)))
        docString = doc.toprettyxml("    ", "\n", "utf-8")
        print docString
        
        try:
            d = {'mxml' : {
                    'settings' : settings.__dict__,
                    'elements' : elements.get_dictionary()
                    }}
            
            doc = dom.parseString(etree.tostring(self.d2xml(d)))
            docString = doc.toprettyxml("    ", "\n", "utf-8")
            
            f = open(settings.get_filepath(), "w")
            f.write(docString)
            f.close()
            
            self.messages.set_message_status(m, True)
            return m
        except Exception, e:
            self.messages.set_message_status(m, False, str(e))
            return m
            
        
    
    @staticmethod
    def xml2d(e):
        """Convert an etree into a dict structure

        @type  e: etree.Element
        @param e: the root of the tree
        @return: The dictionary representation of the XML tree
        """
        def _xml2d(e):
            kids = dict(e.attrib)
            if e.text:
                kids['__text__'] = e.text
            if e.tail:
                kids['__tail__'] = e.tail
            for k, g in groupby(e, lambda x: x.tag):
                g = [ _xml2d(x) for x in g ] 
                kids[k]=  g
            return kids
        return { e.tag : _xml2d(e) }

    @staticmethod
    def d2xml(d):
        """convert dict to xml

           1. The top level d must contain a single entry i.e. the root element
           2.  Keys of the dictionary become sublements or attributes
           3.  If a value is a simple string, then the key is an attribute
           4.  if a value is dict then, then key is a subelement
           5.  if a value is list, then key is a set of sublements

           a  = { 'module' : {'tag' : [ { 'name': 'a', 'value': 'b'},
                                        { 'name': 'c', 'value': 'd'},
                                     ],
                              'gobject' : { 'name': 'g', 'type':'xx' },
                              'uri' : 'test',
                           }
               }
        >>> d2xml(a)
        <module uri="test">
           <gobject type="xx" name="g"/>
           <tag name="a" value="b"/>
           <tag name="c" value="d"/>
        </module>

        @type  d: dict 
        @param d: A dictionary formatted as an XML document
        @return:  A etree Root element
        """
        def _d2xml(d, p):
            for k,v in d.items():
                if isinstance(v,dict):
                    node = etree.SubElement(p, k)
                    _d2xml(v, node)
                elif isinstance(v,list):
                    for item in v:
                        node = etree.SubElement(p, k)
                        _d2xml(item, node)
                elif k == "__text__":
                        p.text = v
                elif k == "__tail__":
                        p.tail = v
                else:
                    if v is None:
                        v = 'None'
                    p.set(k, v)

        k,v = d.items()[0]
        node = etree.Element(k)
        _d2xml(v, node)
        return node
