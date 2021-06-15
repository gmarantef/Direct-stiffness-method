from typing import Tuple
import numpy as np
import math
import sys

from creator.bo.joints import Joint
from creator.bo.materials import Material
from creator.bo.sections import Section
from properties import AREA_UNIT, PRESSURE_UNIT, INERTIA_UNIT


class Web:

    def __init__(self, name: str, joint_start: Joint, joint_end: Joint,
                 material: Material, section: Section) -> None:

        self.name = name
        self.joint_start = joint_start
        self.joint_end = joint_end
        self.material = material
        self.section = section

        if self.joint_start.number > self.joint_end.number:
            print("ERROR!!! El nudo incial debe ser menor que el nudo final en todas las barras")
            sys.exit()

        self.delta_x, self.delta_y, self.length, self.alfa = self.calculations()

        self.k_aa, self.k_ab, self.k_ba, self.k_bb = self.local_stiffness_matrix()
        self.t = self.transformation_matrix()
        self.kg_aa, self.kg_ab, self.kg_ba, self.kg_bb = self.global_stiffness_matrix()

    def __str__(self) -> str:
        return (
            f"\t{self.name}\tNudo inicio {self.joint_start.number} -> nudo final {self.joint_end.number}\n"
            f"\t\tMaterial {self.material.name} en condición {self.material.condition} -> "
            f"E = {self.material.elastic_modulus} {PRESSURE_UNIT}\n" 
            f"\t\tPerfil {self.section.name} -> Área={self.section.area} {AREA_UNIT} |" 
            f"Inercia={self.section.inertia_x} {INERTIA_UNIT}\n"
        )

    def calculations(self) -> Tuple[float, float, float, float]:

        delta_x: float = self.joint_end.x - self.joint_start.x
        delta_y: float = self.joint_end.y - self.joint_start.y
        length: float = np.sqrt((delta_x ** 2) + (delta_y ** 2))
        alfa: float

        if delta_x == 0 and delta_y > 0:
            alfa = math.pi / 2
        elif delta_x == 0 and delta_y < 0:
            alfa = - math.pi / 2
        else:
            alfa = math.atan(delta_y / delta_x)

        return delta_x, delta_y, length, alfa

    def local_stiffness_matrix(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:

        k_aa: np.ndarray = np.zeros((3, 3))
        k_ab: np.ndarray = np.zeros((3, 3))
        k_bb: np.ndarray = np.zeros((3, 3))

        k_aa[0, 0] = self.material.elastic_modulus * self.section.area / self.length
        k_aa[1, 1] = 12 * self.material.elastic_modulus * self.section.inertia_x / (self.length ** 3)
        k_aa[1, 2] = 6 * self.material.elastic_modulus * self.section.inertia_x / (self.length ** 2)
        k_aa[2, 1] = k_aa[1, 2]
        k_aa[2, 2] = 4 * self.material.elastic_modulus * self.section.inertia_x / self.length

        k_ab[0, 0] = - k_aa[0, 0]
        k_ab[1, 1] = - k_aa[1, 1]
        k_ab[1, 2] = k_aa[1, 2]
        k_ab[2, 1] = - k_aa[2, 1]
        k_ab[2, 2] = 2 * self.material.elastic_modulus * self.section.inertia_x / self.length

        k_ba = np.transpose(k_ab)

        k_bb[0, 0] = k_aa[0, 0]
        k_bb[1, 1] = k_aa[1, 1]
        k_bb[1, 2] = - k_aa[1, 2]
        k_bb[2, 1] = - k_aa[2, 1]
        k_bb[2, 2] = k_aa[2, 2]

        return k_aa, k_ab, k_ba, k_bb

    def transformation_matrix(self) -> np.ndarray:
        t: np.ndarray = np.zeros((3, 3))

        t[0, 0] = math.cos(self.alfa)
        t[0, 1] = - math.sin(self.alfa)
        t[1, 0] = - t[0, 1]
        t[1, 1] = t[0, 0]
        t[2, 2] = 1.0

        return t

    def global_stiffness_matrix(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
        kg_aa: np.ndarray = np.dot(self.t, np.dot(self.k_aa, np.transpose(self.t)))
        kg_ab: np.ndarray = np.dot(self.t, np.dot(self.k_ab, np.transpose(self.t)))
        kg_ba: np.ndarray = np.dot(self.t, np.dot(self.k_ba, np.transpose(self.t)))
        kg_bb: np.ndarray = np.dot(self.t, np.dot(self.k_bb, np.transpose(self.t)))

        return kg_aa, kg_ab, kg_ba, kg_bb
