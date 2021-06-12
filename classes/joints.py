# -*- coding: utf-8 -*-
"""
Created on Mon May 24 13:02:47 2021

@author: Guillermo
"""

from typing import List
import sys


# Definicón de la clase para la creación de los objetos nudos de la estructura
class JointClass(object):
    def __init__(self, number: int, x: float, y: float, fx: float, fy: float,
                 mz: float, dx: float, dy: float, fi: float,
                 joints_list: List[object], efforts_list: List[object],
                 deformations_list: List[object], force_unit: str,
                 length_unit: str, spin_unit: str, structure_type: str) -> None:
        
        # Definición del nudo
        self.number: int = number
        self.x: float = x
        self.y: float = y
        # Esfuerzos
        self.fx: float = fx
        self.fy: float = fy
        self.mz: float = mz
        # Deformaciones
        self.dx: float = dx
        self.dy: float = dy
        self.fi: float = fi
        
        self.force_unit = force_unit
        self.length_unit = length_unit
        self.spin_unit = spin_unit
        self.structure_type = structure_type
        
        try:
            mz_modified = float(self.mz)
            fi_modified = float(self.fi)
        except:
            mz_modified = str(self.mz)
            fi_modified = str(self.fi)
            pass
        if self.structure_type=="articulada" and (mz_modified!=0.0 or fi_modified!=0.0):
            print("ERROR! En estructuras articuladas no puede haber momentos o giros en los nudos")
            sys.exit()
        
        joints_list.append(self)
        efforts_list.extend([self.fx, self.fy, self.mz])
        deformations_list.extend([self.dx, self.dy, self.fi])

    def __str__(self) -> str:
        return ("""\t{}\tCoord. globales ({},{}) {}
        Vector de esfuerzos ({},{},{}) {}|{}·{}
        Vector de deformaciones ({},{},{}) {}|{}\n""").format(
        self.number, self.x, self.y, self.length_unit, self.fx, self.fy,
        self.mz, self.force_unit, self.force_unit, self.length_unit, self.dx,
        self.dy, self.fi, self.length_unit, self.spin_unit)