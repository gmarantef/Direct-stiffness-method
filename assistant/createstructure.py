# -*- coding: utf-8 -*-
"""
Created on Wed May 26 15:38:47 2021

@author: Guillermo
"""

from typing import Union, List, Tuple
import numpy as np


# Función para el diseño de los nudos de la estructura
def create_joints(joints_number: int, joints_positions: np.ndarray,
                  effort_array: np.ndarray,
                  deformation_array: np.ndarray, force_unit: str,
                  length_unit: str, spin_unit: str,
                  structure_type: str) -> Tuple[List[object],
                                                List[Union[float, str]],
                                                List[Union[float, str]]]:
    from classes import joints as jt
    
    joints_list: List[object] = []
    efforts_list: List[object] = []
    deformations_list: List[object] = []
    
    # Creo los nudos
    for index in range(joints_number):
        n: int = index + 1
        locals()["Nudo_"+str(n)] = jt.JointClass(n, joints_positions[index,0],
                                                 joints_positions[index,1], 
                                                 effort_array[index,0],
                                                 effort_array[index,1],
                                                 effort_array[index,2],
                                                 deformation_array[index,0],
                                                 deformation_array[index,1],
                                                 deformation_array[index,2],
                                                 joints_list, efforts_list,
                                                 deformations_list,
                                                 force_unit, length_unit,
                                                 spin_unit, structure_type)
        
    return joints_list, efforts_list, deformations_list


# Función para el diseño de las barras de la estructura
def create_webs(webs_number: int, webs_directions: np.ndarray,
                webs_materials: np.ndarray, webs_sections: np.ndarray,
                joints_list: List[object], materials_list: List[object],
                sections_list: List[object], area_unit: str, inertia_unit: str,
                pressure_unit: str) -> List[object]:
    from classes import webs as wb
    from assistant import websnames as wbn
    
    webs_list: List[object] = []
    
    # Importo nombres de barras
    alph_ext: List[str] = wbn.webs_names(webs_number)
    
    # Creo las barras
    for index in range(webs_number):
        for joint in joints_list:
            if joint.number == webs_directions[index,0]:
                joint_start = joint
            elif joint.number == webs_directions[index,1]:
                joint_end = joint
            else:
                False
        for material in materials_list:
            if material.name == str(webs_materials[index,0]) and material.condition == str(webs_materials[index,1]):
                material_choose = material
        for section in sections_list:
            if section.name == webs_sections[index]:
                section_choose = section
        locals()["Barra_"+str(alph_ext[index])] = wb.WebClass(alph_ext[index],
                                                              joint_start, 
                                                              joint_end,
                                                              material_choose,
                                                              section_choose,
                                                              webs_list,
                                                              area_unit,
                                                              inertia_unit,
                                                              pressure_unit)
    
    return webs_list