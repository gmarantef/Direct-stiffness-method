from typing import List
import numpy as np

from properties import STRUCTURE_TYPE
from creator.bo.joints import Joint


def nodal_displacements(k_g: np.ndarray, joints: List[Joint], effort_list: List[float]) -> List[float]:

    known_efforts: List[float] = []
    index_list: List[int] = []
    ban_list: np.ndarray = np.empty(len(joints) * 3)

    if STRUCTURE_TYPE == "articulada":
        ban_list: np.ndarray = np.arange(2, len(joints) * 3, 3)

    for index, value in enumerate(effort_list):
        if value is not None and index not in ban_list:
            known_efforts.append(value)
            index_list.append(index)

    k_min: np.ndarray = np.zeros((len(index_list), len(index_list)))
    for a, i in enumerate(index_list):
        for b, j in enumerate(index_list):
            k_min[a, b] = k_g[i, j]

    unknown_deformations: List[float] = list(np.dot(np.linalg.inv(k_min), np.transpose(np.array(known_efforts))))

    return unknown_deformations
