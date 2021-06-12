# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:02:55 2021

@author: Guillermo
"""

from typing import List
import numpy as np
import math
import sys


# Definición de la clase para la creación de los objetos de barras
class WebClass(object):
    def __init__(self, number: int, joint_start: object, joint_end: object,
                 material: object, section: object, webs_list: List[object],
                 area_unit: str, inertia_unit: str, pressure_unit: str) -> None:
        
        # Definición de las barras
        self.number: int = number
        self.joint_start: object = joint_start
        self.joint_end: object = joint_end       
        self.material: object = material
        self.section: object = section
        
        # Unidades empleadas
        self.area_unit = area_unit
        self.inertia_unit = inertia_unit
        self.pressure_unit = pressure_unit
        
        if self.joint_start.number > self.joint_end.number:    # Asegurar la lógica de nudos
            print("ERROR!!! El nudo incial debe ser menor que el nudo final en todas las barras")
            sys.exit()
        
        # Cálculo sobre barras
        self.delta_x: float = self.joint_end.x - self.joint_start.x
        self.delta_y: float = self.joint_end.y - self.joint_start.y
        self.lenght: float = np.sqrt((self.delta_x**2) + (self.delta_y**2))
        self.alfa: float
        
        if self.delta_x==0 and self.delta_y>0:
            self.alfa = math.pi / 2
        elif self.delta_x==0 and self.delta_y<0:
            self.alfa = - math.pi / 2
        else:
            self.alfa = math.atan(self.delta_y / self.delta_x)
        
        # Llamada a las matrices local, transformación y global
        self.local_stiffness_matrix()
        self.transformation_matrix()
        self.global_stiffness_matrix()
        
        webs_list.append(self)
        
    def __str__(self) -> str:
        return ("""\t{}\tNudo inicio {} -> nudo final {}
        Material {} en condición {} -> E = {} {}
        Perfil {} -> Área={} {} | Inercia={} {}\n""").format(
        self.number,self.joint_start.number, self.joint_end.number, 
        self.material.name, self.material.condition,
        self.material.elastic_modulus, self.pressure_unit,self.section.name,
        self.section.area, self.area_unit, self.section.inertia_x, 
        self.inertia_unit)
        
    def local_stiffness_matrix(self) -> None:
        self.k_aa: np.ndarray = np.zeros((3,3))
        self.k_ab: np.ndarray = np.zeros((3,3))
        self.k_ba: np.ndarray = np.zeros((3,3))
        self.k_bb: np.ndarray = np.zeros((3,3))
        
        # Matriz Kaa
        self.k_aa[0,0] = self.material.elastic_modulus*self.section.area / self.lenght
        self.k_aa[1,1] = 12 * self.material.elastic_modulus*self.section.inertia_x / (self.lenght**3)
        self.k_aa[1,2] = 6 * self.material.elastic_modulus*self.section.inertia_x / (self.lenght**2)
        self.k_aa[2,1] = self.k_aa[1,2]
        self.k_aa[2,2] = 4 * self.material.elastic_modulus*self.section.inertia_x / self.lenght
        
        # Matriz Kab
        self.k_ab[0,0] = - self.k_aa[0,0]
        self.k_ab[1,1] = - self.k_aa[1,1]
        self.k_ab[1,2] = self.k_aa[1,2]
        self.k_ab[2,1] = - self.k_aa[2,1]
        self.k_ab[2,2] = 2 * self.material.elastic_modulus*self.section.inertia_x / self.lenght
        
        # Matriz Kba (transpuesta Kab)
        self.k_ba = np.transpose(self.k_ab)
        
        # Matriz Kbb (simétrica Kaa)
        self.k_bb[0,0] = self.k_aa[0,0]
        self.k_bb[1,1] = self.k_aa[1,1]
        self.k_bb[1,2] = - self.k_aa[1,2]
        self.k_bb[2,1] = - self.k_aa[2,1]
        self.k_bb[2,2] = self.k_aa[2,2]
        
    def transformation_matrix(self) -> None:
        self.t: np.ndarray = np.zeros((3,3))
        # Matriz Transformación
        self.t[0,0] = math.cos(self.alfa)
        self.t[0,1] = - math.sin(self.alfa)
        self.t[1,0] = - self.t[0,1]
        self.t[1,1] = self.t[0,0]
        self.t[2,2] = 1.0
        
    def global_stiffness_matrix(self) -> None:
        # Matriz global = T·Kij·Tt
        self.kg_aa: np.ndarray = np.dot(self.t, np.dot(self.k_aa, np.transpose(self.t)))
        self.kg_ab: np.ndarray = np.dot(self.t, np.dot(self.k_ab, np.transpose(self.t)))
        self.kg_ba: np.ndarray = np.dot(self.t, np.dot(self.k_ba, np.transpose(self.t)))
        self.kg_bb: np.ndarray = np.dot(self.t, np.dot(self.k_bb, np.transpose(self.t)))