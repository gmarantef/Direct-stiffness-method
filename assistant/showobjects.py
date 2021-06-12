# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:30:46 2021

@author: Guillermo
"""

from typing import List


# Funciones para mostrar los nudos, materiales, perfiles, barras y 
# ancho de banda de una estructura
def show_materials(materials_list: List[object]):
    print("\nLista de materiales\n")
    for material in materials_list:
        print(material)


def show_sections(sections_list: List[object]):
    print("\nLista de perfiles\n")
    for section in sections_list:
        print(section)


def show_joints(joints_list: List[object]):
    print("\nLista de nudos\n")
    for joint in joints_list:
        print(joint)


def show_webs(webs_list: List[object]):
    print("\nLista de barras\n")
    for web in webs_list:
        print(web)

   
def bandwidth(webs_list: List[object]):
    bandwidth_list: List[int] = []
    
    for web in webs_list:
        bandwidth_list.append(web.joint_end.number - web.joint_start.number)
    
    bandwidth: int = max(bandwidth_list)
    print("El ancho de banda de la estructura es = {}".format(bandwidth))