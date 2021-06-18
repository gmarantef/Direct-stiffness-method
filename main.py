from typing import List
import pandas as pd

from properties import joints_positions, effort_vectors, deformation_vectors, web_locations, web_materials, web_sections
from data.readdata import read_materials_dataset, read_sections_dataset
from data.manipulatedata import manipulate_materials_dataset, manipulate_sections_dataset
from creator.bo.materials import Material
from creator.bo.sections import Section
from creator.bo.joints import Joint
from creator.bo.webs import Web
from creator.propertiescreator import PropertiesCreator
from creator.structurecreator import StructureCreator
from assistant.showobjects import show_materials, show_sections, show_joints, show_webs, bandwidth
from assistant.dimension import dimension_problem
from method.stiffnessmethod import stiffness_method
from iterate.iterate import state_iterations

# Asegurar que los datos de entrada de las articulaciones son coherentes
dimension_problem(joints_positions, effort_vectors, deformation_vectors)

# Lectura de los Datasets de materiales y perfiles procedentes de .xlsx
materials_dataset: pd.DataFrame = read_materials_dataset()
sections_dataset: pd.DataFrame = read_sections_dataset()

# Modificación de los Datasets anteriores de cara a poder usarlos más adelante
work_materials_dataset: pd.DataFrame = manipulate_materials_dataset(materials_dataset)
work_sections_dataset: pd.DataFrame = manipulate_sections_dataset(sections_dataset)

# Creo los objetos de materiales y perfiles contenidos en la estructura
materials: List[Material] = PropertiesCreator(work_materials_dataset=work_materials_dataset,
                                              web_materials=web_materials).materials
sections: List[Section] = PropertiesCreator(work_sections_dataset=work_sections_dataset,
                                            web_sections=web_sections).sections

# Creo los objetos de nudos y barras
joints: List[Joint] = StructureCreator(joints_positions=joints_positions, effort_vectors=effort_vectors,
                                       deformation_vectors=deformation_vectors).joints
webs: List[Web] = StructureCreator(web_locations=web_locations, materials=materials, sections=sections,
                                   joints=joints).webs

# Muestro los objetos creados
show_materials(materials)
show_sections(sections)
show_joints(joints)
show_webs(webs)
bandwidth(webs)

# Método de la rigidez
final_efforts_vector: List[float]
final_deformations_vector: List[float]
final_efforts_vector, final_deformations_vector = stiffness_method(joints, webs, effort_vectors, deformation_vectors)

# Iteraciones de estados de carga, materiales y perfiles distintos
final_df: pd.DataFrame = state_iterations(effort_vectors, deformation_vectors, joints_positions, materials_dataset,
                                          sections_dataset, web_locations)
