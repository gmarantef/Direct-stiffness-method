from typing import List
import numpy as np

from assistant.convert import convert_to_vector
from assistant.convert import convert_to_elastic_modulus
from assistant.convert import convert_to_area_inertia
from creator.bo.vectors import PositionVector, DeformationVector, WebVector, EffortVector
from creator.bo.materials import Material
from creator.bo.sections import Section
from creator.bo.joints import Joint
from creator.bo.webs import Web
from creator.structurecreator import StructureCreator
from method.stiffnessmethod import stiffness_method


def iterations(joints_positions: List[PositionVector], deformation_vectors: List[DeformationVector],
               web_locations: List[WebVector], state_efforts_array: np.ndarray, state_materials_array: np.ndarray,
               state_sections_array: np.ndarray) -> np.ndarray:

    iteration: int = 0
    max_iter: int = state_efforts_array.shape[0] * state_materials_array.shape[0] * state_sections_array.shape[0]
    final_list: List[float] = []

    for row_efforts in state_efforts_array:
        iter_efforts: List[EffortVector] = convert_to_vector(row_efforts, joints_positions)
        for row_materials in state_materials_array:
            iter_materials: List[Material] = list(row_materials)
            iter_elastic_modulus: List[float] = convert_to_elastic_modulus(iter_materials)
            for row_sections in state_sections_array:
                iter_sections: List[Section] = list(row_sections)
                iter_area_inertia: List[float] = convert_to_area_inertia(iter_sections)
                iter_joints: List[Joint] = StructureCreator(joints_positions=joints_positions,
                                                            effort_vectors=iter_efforts,
                                                            deformation_vectors=deformation_vectors).joints
                iter_webs: List[Web] = StructureCreator(web_locations=web_locations, materials=iter_materials,
                                                        sections=iter_sections, joints=iter_joints).webs

                final_efforts_vector: List[float]
                final_deformations_vector: List[float]
                final_efforts_vector, final_deformations_vector = stiffness_method(iter_joints, iter_webs,
                                                                                   iter_efforts, deformation_vectors)

                final_list += list(row_efforts) + iter_elastic_modulus + iter_area_inertia + \
                    final_efforts_vector + final_deformations_vector

                iteration += 1
                print("Iteración ", iteration, "de", max_iter)

    final_array: np.ndarray = np.array(final_list).reshape((max_iter, len(final_list) / max_iter))

    return final_array
