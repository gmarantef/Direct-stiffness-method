# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:01:56 2021

@author: Guillermo
"""

from typing import List


# Definicicón de la clase para la creación de los objetos de materiales
class MaterialClass(object):
    def __init__(self, name: str, condition: str, elastic_modulus: float, 
                 materials_list: List[object], pressure_unit: str) -> None:
        self.name: str = name
        self.condition: str = condition
        self.elastic_modulus: float = elastic_modulus
        self.pressure_unit = pressure_unit
        
        materials_list.append(self)
            
    def __str__(self) -> str:
        return ("\t{} / {} -> E = {} {}\n").format(self.name, 
                                                   self.condition,
                                                   self.elastic_modulus, 
                                                   self.pressure_unit)