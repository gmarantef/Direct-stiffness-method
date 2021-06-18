from typing import List, Tuple
import numpy as np

from creator.bo.vectors import PositionVector, EffortVector, DeformationVector
from creator.bo.materials import Material
from creator.bo.sections import Section


def convert_to_list(effort_vectors: List[EffortVector],
                    deformation_vectors: List[DeformationVector]) -> Tuple[List[float], List[float]]:

    effort_list: List[float] = []
    deformation_list: List[float] = []

    for value in effort_vectors:
        effort_list.extend([value.fx, value.fy, value.mz])

    for value in deformation_vectors:
        deformation_list.extend([value.dx, value.dy, value.phi])

    return effort_list, deformation_list


def convert_to_vector(row_efforts: np.ndarray, joints_positions: List[PositionVector]) -> List[EffortVector]:

    list_index: List[int] = list(range(0, len(joints_positions) * 3, 3))
    iter_efforts: List[EffortVector] = []
    for i in list_index:
        iter_efforts.append(EffortVector(row_efforts[i], row_efforts[i+1], row_efforts[i+2]))

    return iter_efforts


def convert_to_elastic_modulus(iter_materials: List[Material]) -> List[float]:

    iter_elastic_modulus: List[float] = []
    for value in iter_materials:
        iter_elastic_modulus.append(value.elastic_modulus)

    return iter_elastic_modulus


def convert_to_area_inertia(iter_sections: List[Section]) -> List[float]:

    iter_area_inertia: List[float] = []
    for value in iter_sections:
        iter_area_inertia.extend([value.area, value.inertia_x])

    return iter_area_inertia
