from typing import List
import numpy as np

from creator.bo.joints import Joint
from creator.bo.webs import Web


def fill_diagonal(k_g: np.ndarray, joints: List[Joint], webs: List[Web]) -> np.ndarray:

    for joint in joints:
        kn: np.ndarray = np.zeros((3, 3))
        for web in webs:
            if web.joint_start.number == joint.number:
                kn += web.kg_aa
            elif web.joint_end.number == joint.number:
                kn += web.kg_bb
        row: int = (joint.number - 1) * 3
        for n in range(3):
            column: int = row - n
            for m in range(3):
                k_g[row, column] = kn[n, m]
                column += 1
            row += 1

    return k_g


def fill_up_diagonal(k_g: np.ndarray, joints: List[Joint], webs: List[Web]) -> np.ndarray:

    for joint in joints:
        for web in webs:
            if web.joint_start.number == joint.number:
                column: int = (web.joint_end.number - 1) * 3
                for m in range(3):
                    row: int = (web.joint_start.number - 1) * 3
                    for n in range(3):
                        k_g[row, column] = web.kg_ab[n, m]
                        row += 1
                    column += 1

    return k_g


def fill_down_diagonal(k_g: np.ndarray, joints: List[Joint], webs: List[Web]) -> np.ndarray:

    for joint in joints:
        for web in webs:
            if web.joint_start.number == joint.number:
                row: int = (web.joint_end.number - 1) * 3
                for n in range(3):
                    column: int = (web.joint_start.number - 1) * 3
                    for m in range(3):
                        k_g[row, column] = web.kg_ba[n, m]
                        column += 1
                    row += 1

    return k_g
