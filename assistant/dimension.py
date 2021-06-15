from typing import List
import sys


def dimension_problem(joints_positions: List[float], effort_vectors: List[float], deformation_vectors: List[float]):

    if len(joints_positions) == len(effort_vectors) == len(deformation_vectors):
        print("Ha introducido los datos de la estructura coherentes")
    else:
        print("Los datos de la estructura son incoherentes")
        sys.exit()
