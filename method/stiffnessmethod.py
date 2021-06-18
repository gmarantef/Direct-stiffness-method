from typing import List, Tuple
import numpy as np

from creator.bo.vectors import EffortVector, DeformationVector
from creator.bo.joints import Joint
from creator.bo.webs import Web
from method.auxiliarfunct.fillmatrix import fill_diagonal, fill_up_diagonal, fill_down_diagonal
from method.auxiliarfunct.nodaldisplacements import nodal_displacements
from method.auxiliarfunct.finalvectors import final_vectors
from assistant.convert import convert_to_list


def stiffness_method(joints: List[Joint], webs: List[Web], effort_vectors: List[EffortVector],
                     deformation_vectors: List[DeformationVector]) -> Tuple[np.ndarray, np.ndarray]:

    k_g: np.ndarray = np.zeros((3 * len(joints), 3 * len(joints)))

    k_g = fill_diagonal(k_g, joints, webs)
    k_g = fill_up_diagonal(k_g, joints, webs)
    k_g = fill_down_diagonal(k_g, joints, webs)

    effort_list: List[float]
    deformation_list: List[float]
    effort_list, deformation_list = convert_to_list(effort_vectors, deformation_vectors)

    unknown_deformations: List[float] = nodal_displacements(k_g, joints, effort_list)

    final_efforts_vector: np.ndarray
    final_deformations_vector: np.ndarray
    final_efforts_vector, final_deformations_vector = final_vectors(k_g, unknown_deformations, deformation_list)
    
    return final_efforts_vector, final_deformations_vector
