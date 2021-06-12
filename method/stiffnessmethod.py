# -*- coding: utf-8 -*-
"""
Created on Mon May 24 14:16:40 2021

@author: Guillermo
"""

from typing import Union, List, Tuple
import numpy as np


# Ensamblaje de la matriz global
def stiffness_method(joints_list: List[object], webs_list: List[object],
                     efforts_list_modified: List[Union[float, str]],
                     deformations_list_modified: List[Union[float, str]],
                     structure_type: str,
                     joints_number: int) -> Tuple[np.ndarray, 
                                                  np.ndarray, 
                                                  np.ndarray]:
    k_g: np.ndarray = np.zeros((3 * len(joints_list), 3 * len(joints_list)))
    
    # Evalúo nudo tras nudo para sacar los elementos de la diagonal
    for joint in joints_list:
        kn: np.ndarray = np.zeros((3,3))
        for web in webs_list:
            if web.joint_start == joint:
                kn += web.kg_aa
            elif web.joint_end == joint:
                kn += web.kg_bb
            else: False
        row: int = (joint.number - 1)*3
        for n in range(3):
            column: int = row - n
            for m in range(3):
                k_g[row,column] = kn[n,m]
                column += 1
            row += 1
            
    # Evalúo nudo tras nudo para sacar los elementos encima de la diagonal
    for joint in joints_list:
        for web in webs_list:
            if web.joint_start == joint:
                column: int = (web.joint_end.number - 1)*3
                for m in range(3):
                    row: int = (web.joint_start.number - 1)*3
                    for n in range(3):
                        k_g[row,column] = web.kg_ab[n,m]
                        row += 1
                    column += 1
                    
    # Genero los elementos debajo de la diagonal como simétricos a los de arriba (traspuestas)
    for joint in joints_list:
        for web in webs_list:
            if web.joint_start == joint:
                row: int = (web.joint_end.number - 1)*3
                for n in range(3):
                    column: int = (web.joint_start.number - 1)*3
                    for m in range(3):
                        k_g[row,column] = web.kg_ba[n,m]
                        column += 1
                    row += 1
    
    # Cálculo de los desplazamientos nodales
    known_efforts_list: List[float] = []
    index_list: List[int] = []
    if structure_type == "no articulada":
        for index, value in enumerate(efforts_list_modified):
            if type(value) is not str :
                known_efforts_list.append(value)
                index_list.append(index)
    elif structure_type == "articulada":
        ban_list: np.ndarray = np.arange(2, joints_number * 3, 3)
        for index, value in enumerate(efforts_list_modified):
            if type(value) is not str and index not in ban_list:
                known_efforts_list.append(value)
                index_list.append(index)
    
    k_min: np.ndarray = np.zeros((len(index_list), len(index_list)))
    for a, i in enumerate(index_list):
        for b, j in enumerate(index_list):
            k_min[a,b] = k_g[i,j]
            
    calculated_deformations_list: List[float] = list(np.dot(np.linalg.inv(k_min),
                                                     np.transpose(np.array(known_efforts_list))))
    
    # Vector de esfuerzos y deformaciones
    n: int = 0
    deformations_vector: np.ndarray = np.empty((len(deformations_list_modified)))
    for index, value in enumerate(deformations_list_modified):
        if type(value) is str:
            deformations_vector[index] = calculated_deformations_list[n]
            n += 1
        else:
            deformations_vector[index] = deformations_list_modified[index]
            
    efforts_vector: np.ndarray = np.dot(k_g,
                                          np.transpose(np.array(deformations_vector)))
    
    return k_g, efforts_vector, deformations_vector