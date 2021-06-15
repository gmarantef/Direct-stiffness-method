from typing import List, Tuple

from properties import EffortVector, DeformationVector


def convert_to_list(effort_vectors: List[EffortVector],
                    deformation_vectors: List[DeformationVector]) -> Tuple[List[float], List[float]]:

    effort_list: List[float] = []
    deformation_list: List[float] = []

    for value in effort_vectors:
        effort_list.extend([value.fx, value.fy, value.mz])

    for value in deformation_vectors:
        deformation_list.extend([value.dx, value.dy, value.phi])

    return effort_list, deformation_list
