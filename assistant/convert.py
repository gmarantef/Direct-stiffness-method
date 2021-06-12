# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 11:00:34 2021

@author: Guillermo
"""

from typing import Union, List


# Convierte las listas de objetos a listas de flotantes y strings
def convert(efforts_list: List[object], deformations_list: List[object]):
    # Convertir las listas de esfuerzos y deformaciones de objetos a float/str
    efforts_list_modified: List[Union[float, str]] = []
    deformations_list_modified: List[Union[float, str]] = []
    for value in efforts_list:
        try:
            efforts_list_modified.append(float(value))
        except:
            efforts_list_modified.append(str(value))
    for value in deformations_list:
        try:
            deformations_list_modified.append(float(value))
        except:
            deformations_list_modified.append(str(value))
    
    return efforts_list_modified, deformations_list_modified