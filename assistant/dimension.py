from typing import List
import sys

from creator.bo.vectors import PositionVector, EffortVector, DeformationVector


def dimension_problem(joints_positions: List[PositionVector], effort_vectors: List[EffortVector],
                      deformation_vectors: List[DeformationVector]) -> str:

    message: str
    if len(joints_positions) == len(effort_vectors) == len(deformation_vectors):
        message = "Ha introducido los datos de la estructura coherentes"
    else:
        message = "Los datos de la estructura son incoherentes"
        sys.exit()

    return message
