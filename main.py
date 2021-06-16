from typing import List
import numpy as np
import pandas as pd

from data import readdata as rd
from data import manipulatedata as md
from properties import joints_positions, effort_vectors, deformation_vectors, web_locations, web_materials, web_sections
from creator import propertiescreator as pc
from creator import structurecreator as sc
from creator.bo.materials import Material
from creator.bo.sections import Section
from creator.bo.joints import Joint
from creator.bo.webs import Web
from assistant import showobjects as show
from assistant import dimension as dim
from method import stiffnessmethod as smet

# Asegurar que los datos de entrada de las articulaciones son coherentes
dim.dimension_problem(joints_positions, effort_vectors, deformation_vectors)

# Lectura de los Datasets de materiales y perfiles procedentes de .xlsx
materials_dataset: pd.DataFrame = rd.read_materials_dataset()
sections_dataset: pd.DataFrame = rd.read_sections_dataset()

# Modificación de los Datasets anteriores de cara a poder usarlos más adelante
work_materials_dataset: pd.DataFrame = md.manipulate_materials_dataset(materials_dataset)
work_sections_dataset: pd.DataFrame = md.manipulate_sections_dataset(sections_dataset)

# Creo los objetos de materiales y perfiles contenidos en la estructura
materials: List[Material] = pc.PropertiesCreator(work_materials_dataset, work_sections_dataset,
                                                 web_materials, web_sections).materials
sections: List[Section] = pc.PropertiesCreator(work_materials_dataset, work_sections_dataset,
                                               web_materials, web_sections).sections

# Creo los objetos de nudos y barras
joints: List[Joint] = sc.StructureCreator(joints_positions, effort_vectors, deformation_vectors, web_locations,
                                          materials, sections).joints
webs: List[Web] = sc.StructureCreator(joints_positions, effort_vectors, deformation_vectors, web_locations,
                                      materials, sections).webs

# Muestro los objetos creados
show.show_materials(materials)
show.show_sections(sections)
show.show_joints(joints)
show.show_webs(webs)
show.bandwidth(webs)

# Método de la rigidez
k_g: np.ndarray
final_efforts_vector: List[float]
final_deformations_vector: List[float]
k_g, final_efforts_vector, final_deformations_vector = smet.stiffness_method(joints, webs, effort_vectors,
                                                                             deformation_vectors)

""""# Iteraciones de estados de carga, materiales y perfiles distintos
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
                     joints_positions, deformation_array)"""
