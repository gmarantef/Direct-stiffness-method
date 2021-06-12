# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:00:11 2021

@author: Guillermo
"""

from typing import List
import sys


# Definición de la clase para la creación de los objetos de secciones
class SectionClass(object):
    def __init__(self, name: str, area: float, inertia_x: float, 
                 sections_list: List[object], area_unit: str,
                 inertia_unit: str, structure_type: str) -> None:
        self.name: str = name
        self.area: float = area
        self.inertia_x: float
        
        self.area_unit = area_unit
        self.inertia_unit = inertia_unit
        self.structure_type = structure_type
        
        if self.structure_type == "articulada":
            self.inertia_x = 0.0
        elif self.structure_type == "no articulada":
            self.inertia_x = inertia_x
        else:
            print("ERROR! Ha introducido incorrectamente el tipo de estructura")
            sys.exit()
        
        
        
        sections_list.append(self)
        
    def __str__(self) -> str:
        return ("\t{} -> A = {} {} / Ix = {} {}\n").format(self.name, 
                                                           self.area,
                                                           self.area_unit,
                                                           self.inertia_x,
                                                           self.inertia_unit)