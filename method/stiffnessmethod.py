from typing import List, Tuple
import numpy as np

from creator.bo.joints import Joint
from creator.bo.webs import Web
from creator.bo.vectors import EffortVector, DeformationVector
from method.auxiliarfunct import fillmatrix as fill
from method.auxiliarfunct import nodaldisplacements as nodal
from method.auxiliarfunct import finalvectors as vec
from assistant import convert


def stiffness_method(joints: List[Joint], webs: List[Web], effort_vectors: List[EffortVector],
                     deformation_vectors: List[DeformationVector]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:

    k_g: np.ndarray = np.zeros((3 * len(joints), 3 * len(joints)))

    k_g = fill.fill_diagonal(k_g, joints, webs)
    k_g = fill.fill_up_diagonal(k_g, joints, webs)
    k_g = fill.fill_down_diagonal(k_g, joints, webs)

    effort_list, deformation_list = convert.convert_to_list(effort_vectors, deformation_vectors)

    unknown_deformations = nodal.nodal_displacements(k_g, joints, effort_list)

    final_efforts_vector, final_deformations_vector = vec.final_vectors(k_g, unknown_deformations, deformation_list)
    
    return k_g, final_efforts_vector, final_deformations_vector
