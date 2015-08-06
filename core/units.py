#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Unit(object):
    '''
    Unit actions for set unit type
    '''
    
    def __init__(self, unit_dict, unit):
        
        self.unit = unit
        self.unit_dict = unit_dict
        
    def to_unit(self, number, given_unit):
        '''
        Returns Si value in given unit form
        
        @type  number:     int/float
        @param number:     Value in Si
        @type  given_unit: String
        @param given_unit: Given unit
        @return:           float value in given unit
        '''
        return number / self.unit_dict[given_unit]
        
    def to_unit_str(self, number, given_unit):
        '''
        Returns Si value in given unit form as string with unit name
        
        @type  number:     int/float
        @param number:     Value in Si
        @type  given_unit: String
        @param given_unit: Given unit
        @return:           string value in given unit and with unit name
        '''
        return str(self.to_unit(number, given_unit)) +' '+ given_unit
        
    def str(self, number):
        '''
        Returns Si value in default unit form as string with unit name
        
        @type  number:     int/float
        @param number:     Value in Si
        @return:           string value in default unit and with unit name
        '''
        return str(self.num(number)) +' '+ self.unit
        
    def num(self, number):
        '''
        Returns Si value in default unit form
        
        @type  number:     int/float
        @param number:     Value in Si
        @return:           float value in default unit
        '''
        if number is None:
            return None
        divider = self.unit_dict[self.unit]
        return float(number) / divider
        
    def set_unit(self, given_unit):
        '''
        Sets default unit to given unit
        '''
        for unit, divider in list(self.unit_dict.items()):
            if unit == given_unit:
                self.unit = given_unit

    def si(self, number):
        '''
        Returns value in default unit as Si value
        
        @type  number:     int/float
        @param number:     Value in default unit
        @return:           float value in Si
        '''
        divider = self.unit_dict[self.unit]
        return float(number) * divider
        
    def to_si_from(self, number, given_unit):
        '''
        Returns value in given unit as Si value
        
        @type  number:     int/float
        @param number:     Value in given unit
        @type  given_unit: String
        @param given_unit: Given unit
        @return:           float value in Si
        '''
        return float(number) * self.unit_dict[given_unit]
        

class Units(object):
    '''
    Unit holder.
    Inits time, distance, mass, speed and force -units
    '''
    
    def __init__(self):
        
        self.volume_units = {}
        self.volume_units['m³'] = 1
        self.volume_units['ha'] = 10000
        self.volume_units['km³'] = 1000000
        self.default_volume_unit = 'm³'
        self.volume = Unit(self.volume_units, self.default_volume_unit)
        
        self.area_units = {}
        self.area_units['m²'] = 1
        self.area_units['km²'] = 1000000
        self.default_area_unit = 'm²'
        self.area = Unit(self.area_units, self.default_area_unit)
        
        self.lenght_units = {}
        self.lenght_units['m'] = 1
        self.lenght_units['km'] = 1000
        self.default_lenght_unit = 'm'
        self.lenght = Unit(self.lenght_units, self.default_lenght_unit)
        
        self.time_units = {}
        self.time_units['s'] = 1
        self.time_units['h'] = 3600
        self.time_units['d'] = 3600*24
        self.time_units['m'] = 3600*24*30
        self.time_units['y'] = 3600*24*365
        self.default_time_unit = 's'
        self.time = Unit(self.time_units, self.default_time_unit)
    
        self.mass_units = {}
        self.mass_units['kg'] = 1
        self.mass_units['t'] = 1000
        self.mass_units['kt'] = 1000*1000
        self.mass_units['mt'] = 1000*1000*1000
        self.default_mass_unit = 'kg'
        self.mass = Unit(self.mass_units, self.default_mass_unit)
        
        self.speed_units = {}
        self.speed_units['m/s'] = 1
        self.speed_units['km/h'] = 1/3.6
        self.speed_units['km/s'] = 1000
        self.default_speed_unit = 'km/h'
        self.speed = Unit(self.speed_units, self.default_speed_unit)
        
        
    def save_units(self):
        '''
        Gives default units for saving in file
        
        @return: Dictionary
        '''
        units = {}
        units['volume'] = self.time.unit
        units['area'] = self.dist.unit
        units['lenght'] = self.mass.unit
        units['time'] = self.speed.unit
        units['mass'] = self.force.unit
        units['speed'] = self.force.unit
        
        return units
        
    def load_units(self, units):
        '''
        Sets default units from dictionary loaded from file
        
        @type  units: Dictionary
        @param units: Default units
        '''
        
        if 'volume' in units:
            self.volume.unit = units['volume']
        if 'area' in units:
            self.area.unit = units['area']
        if 'lenght' in units:
            self.lenght.unit = units['lenght']
        if 'time' in units:
            self.time.unit = units['time']
        if 'mass' in units:
            self.mass.unit = units['mass']
        if 'speed' in units:
            self.speed.unit = units['speed']
