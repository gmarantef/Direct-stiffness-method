# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 10:36:25 2021

@author: Guillermo
"""

from typing import Union, List
import numpy as np
import random
import pandas as pd
from itertools import combinations_with_replacement

from assistant import createstructure as cs
from method import stiffnessmethod as sm


def state_iterations(number_state_efforts: int, number_materials: int,
                     number_sections: int, joints_number: int,
                     effort_max: float, force_unit: str, length_unit: str,
                     spin_unit: str, area_unit: str, inertia_unit: str,
                     pressure_unit: str, structure_type: str, webs_number: int,
                     webs_directions: np.ndarray,
                     efforts_list_modified: List[Union[float, str]],
                     deformations_list_modified: List[Union[float, str]],
                     materials_list: List[object], sections_list: List[object],
                     joints_positions: np.ndarray, deformation_array: np.ndarray
                     ) -> np.ndarray:
    # Importo módulos
    from assistant import websnames as wbn
    
    # Array de iteración de los estados de carga
    state_efforts_array: np.ndarray = np.empty([number_state_efforts,
                                                len(efforts_list_modified)],
                                                dtype = object)
    ban_list: np.ndarray = np.arange(2, joints_number * 3, 3)
    for i in range(state_efforts_array.shape[0]):
        for j in range(state_efforts_array.shape[1]):
            if structure_type == "articulada":
                if type(efforts_list_modified[j]) is not str and j not in ban_list:
                    state_efforts_array[i, j] = random.randint(- effort_max,
                                                               effort_max)
                elif type(efforts_list_modified[j]) is str and j not in ban_list:
                    state_efforts_array[i, j] = efforts_list_modified[j]
                elif j in ban_list:
                    state_efforts_array[i, j] = 0.0
            elif structure_type == "no articulada":
                if type(efforts_list_modified[j]) is not str:
                    state_efforts_array[i, j] = random.randint(- effort_max,
                                                               effort_max)
                else:
                    state_efforts_array[i, j] = efforts_list_modified[j]
    
    # Conversión del array de estados de carga a dataframe
    columns: List[str] = []
    for i in range(joints_number):
        columns.extend(["fx_" + str(i+1), "fy_" + str(i+1), "Mz_" + str(i+1)])
    state_efforts_df: pd.DataFrame = pd.DataFrame(state_efforts_array,
                                                  columns = columns)
    
    # Elección aleatoria de materiales y perfiles
    mat_list_random: List[object] = np.random.choice(materials_list,
                                                     size = number_materials,
                                                     replace = False)
    sect_list_random: List[object] = np.random.choice(sections_list,
                                                      size = number_sections,
                                                      replace = False)
    
    # Importo nombres de barras
    alph_ext = wbn.webs_names(webs_number)
    
    # Array de iteración de los materiales y reducción a 100 filas
    materials_array: np.ndarray = np.array(list(combinations_with_replacement(
                                                mat_list_random, webs_number)))
    random_index = np.random.choice(materials_array.shape[0], size=100,
                                    replace=False)
    materials_array_random = materials_array[random_index, :]

    # Conversión del array de materiales a DataFrame
    columns: List[str] = []
    for i in range(webs_number):
        columns.append("Material_" + str(alph_ext[i]))
    state_materials_df: pd.DataFrame = pd.DataFrame(materials_array_random,
                                                    columns = columns)
    
    # Array de iteración de las secciones y reducción a 100 filas
    sections_array: np.ndarray = np.array(list(combinations_with_replacement(
                                          sect_list_random, webs_number)))
    random_index = np.random.choice(sections_array.shape[0], size=100,
                                    replace=False)
    sections_array_random = sections_array[random_index, :]

    # Conversión del array de las secciones a DataFrame
    columns: List[str] = []
    for i in range(webs_number):
        columns.append("Sección " + str(alph_ext[i]))
    state_sections_df: pd.DataFrame = pd.DataFrame(sections_array_random,
                                                   columns = columns)
    
    iteration: int = 0
    max_iter: int = state_efforts_array.shape[0] * materials_array_random.shape[0] * sections_array_random.shape[0]
    # Combinaciones de estados de carga, materiales y perfiles
    for row_efforts in state_efforts_array:
        row_efforts_order = row_efforts.reshape((joints_number, 3))
        for row_materials in materials_array_random:
            row_materials_order: np.ndarray = np.empty([webs_number, 2],
                                                       dtype = object)
            for i, material in enumerate(row_materials):
                row_materials_order[i, 0] = material.name
                row_materials_order[i, 1] = material.condition
            for row_sections in sections_array_random:
                row_sections_order: np.ndarray = np.empty([webs_number, 1],
                                                          dtype = object)
                for j, section in enumerate(row_sections):
                    row_sections_order[j, 0] = section.name
                
                joints_list: List[object]
                efforts_list: List[object]
                deformations_list: List[object]
                (joints_list, efforts_list,
                 deformations_list) = cs.create_joints(joints_number,
                                                       joints_positions,
                                                       row_efforts_order,
                                                       deformation_array,
                                                       force_unit, length_unit,
                                                       spin_unit, 
                                                       structure_type)
                webs_list: List[object] = cs.create_webs(webs_number,
                                                         webs_directions,
                                                         row_materials_order,
                                                         row_sections_order,
                                                         joints_list,
                                                         materials_list,
                                                         sections_list,
                                                         area_unit,
                                                         inertia_unit,
                                                         pressure_unit)
                
                global_matrix_iter: np.ndarray
                effort_vector_iter: np.ndarray
                deformation_vector_iter: np.ndarray
                (global_matrix_iter, effort_vector_iter,
                 deformation_vector_iter) = sm.stiffness_method(joints_list,
                                                           webs_list,
                                                           efforts_list_modified,
                                                           deformations_list_modified,
                                                           structure_type, joints_number)
                iteration += 1
                print("Iteración ", iteration, "de",  max_iter)
    
    return global_matrix_iter, effort_vector_iter, deformation_vector_iter