# -*- coding: utf-8 -*-
"""
Created on Tue May 25 20:08:35 2021

@author: Guillermo
"""

from typing import Union, List
import numpy as np
import sys

from assistant import readdata as rd
from assistant import createstructure as cs
from assistant import showobjects as so
from assistant import convert as cv
from method import stiffnessmethod as sm
import iterate as it

# Sistema de unidades
force_unit: str = "N"
length_unit: str = "m"
spin_unit: str = "rd"
pressure_unit: str = "N/m^2"
area_unit: str = "m^2"
inertia_unit: str = "m^4"

# Tipología estructural articulada o no articulada
structure_type: str = "articulada"

# Creo los materiales y los perfiles
materials_list: List[object] = rd.read_materials(pressure_unit)
sections_list: List[object] = rd.read_sections(area_unit, inertia_unit,
                                               structure_type)

# Defino la estructura (Entradas manuales)
# La posición de nudos debe ir en orden con la numeración de los nudos
# Las listas de esfuerzos y deformaciones deben ir en orden con la numeración de los nudos
# El momento positivo es el que sale del plano
# Las direcciones de barras relacionan los nudos de inicio y fin que se ordenan igual que las posiciones de nudos
# Los materiales y perfiles se organizan en arrays en el mismo orden que hasta ahora
#
# Nudos estado inicial de carga
joints_number: int = 6
joints_positions: np.ndarray = np.array([(0.0, 0.0), (2.0, 3.46),
                                         (4.0, 6.92), (4.0, 0.0),
                                         (6.0, 3.46), (8.0, 0.0)])
effort_array: np.ndarray = np.array([(0.0, "desc", 0.0),
                                     (0.0, 0.0, 0.0),
                                     (0.0, 0.0, 0.0),
                                     (0.0, -10000.0, 0.0),
                                     (0.0, 0.0, 0.0),
                                     ("desc", "desc", 0.0)])
deformation_array: np.ndarray = np.array([("desc", 0.0, 0.0),
                                          ("desc", "desc", 0.0),
                                          ("desc", "desc", 0.0),
                                          ("desc", "desc", 0.0),
                                          ("desc", "desc", 0.0),
                                          (0.0, 0.0, 0.0)])
# Barras
webs_number: int = 10
webs_directions: np.ndarray = np.array([(1, 2), (2, 3), (3, 4), (1, 4), (2, 4),
                                        (2, 5), (3, 5), (4, 5), (4, 6), (5, 6)])
webs_materials: np.ndarray = np.array([("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50"), 
                                       ("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50"),
                                       ("ASTM A572", "Grade 50")])
webs_sections: np.ndarray = np.array(["IPN 220", "IPN 220", "IPN 220",
                                      "IPN 220", "IPN 220", "IPN 220",
                                      "IPN 220", "IPN 220", "IPN 220",
                                      "IPN 220"])

# Comprobación de la dimensionalidad en los datos de entrada de la estructura
if joints_positions.shape[0] == effort_array.shape[0] == deformation_array.shape[0]:
    print("Ha introducido los datos de la estructura coherentes")
else:
    print("Los datos de la estructura son incoherentes")
    sys.exit()

# Creo los nudos y barras de la estructura
joints_list: List[object]
efforts_list: List[object]
deformations_list: List[object]
joints_list, efforts_list, deformations_list = cs.create_joints(joints_number, 
                                                                joints_positions,
                                                                effort_array,
                                                                deformation_array,
                                                                force_unit,
                                                                length_unit,
                                                                spin_unit,
                                                                structure_type)
webs_list: List[object] = cs.create_webs(webs_number, webs_directions,
                                         webs_materials, webs_sections,
                                         joints_list, materials_list,
                                         sections_list, area_unit,
                                         inertia_unit, pressure_unit)

# Convierto las listas de esfuerzos y deformaciones de objetos a float/str
efforts_list_modified: List[Union[float, str]]
deformations_list_modified: List[Union[float, str]]
efforts_list_modified, deformations_list_modified = cv.convert(efforts_list,
                                                               deformations_list)

# Muestro nudos y barras creadas
so.show_joints(joints_list)
so.show_webs(webs_list)
# Muestro el ancho de banda de la estructura
so.bandwidth(webs_list)

# Método de la rigidez
global_matrix: np.ndarray
effort_vector: np.ndarray
deformation_vector: np.ndarray
(global_matrix, effort_vector,
 deformation_vector) = sm.stiffness_method(joints_list, webs_list,
                                           efforts_list_modified,
                                           deformations_list_modified,
                                           structure_type, joints_number)

# Iteraciones de estados de carga, materiales y perfiles distintos
number_state_efforts = 100    # Número de estados de carga
number_materials = 10    # Número de materiales a escoger
number_sections = 10    # Número de secciones a escoger
effort_max = 500.0    # Máximo esfuerzo que pueda aparecer
(global_matrix_iter, effort_vector_iter,
 deformation_vector_iter) = it.state_iterations(number_state_efforts, number_materials,
                     number_sections, joints_number,
                     effort_max, force_unit, length_unit,
                     spin_unit, area_unit, inertia_unit,
                     pressure_unit, structure_type, webs_number,
                     webs_directions,
                     efforts_list_modified,
                     deformations_list_modified,
                     materials_list, sections_list,
                     joints_positions, deformation_array)
