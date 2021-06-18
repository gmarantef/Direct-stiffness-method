import numpy as np

from properties import STRUCTURE_TYPE


def ban(joints: any) -> np.ndarray:
    ban_list: np.ndarray = np.empty(len(joints) * 3)

    if STRUCTURE_TYPE == "articulada":
        ban_list: np.ndarray = np.arange(2, len(joints) * 3, 3)

    return ban_list
