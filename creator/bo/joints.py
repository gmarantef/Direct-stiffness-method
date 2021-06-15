import sys

from properties import FORCE_UNIT, LENGTH_UNIT, SPIN_UNIT, STRUCTURE_TYPE


class Joint:

    def __init__(self, number: int, x: float, y: float, fx: float, fy: float, mz: float,
                 dx: float, dy: float, phi: float) -> None:

        self.number = number
        self.x = x
        self.y = y
        self.fx = fx
        self.fy = fy
        self.mz = mz
        self.dx = dx
        self.dy = dy
        self.phi = phi

        if STRUCTURE_TYPE == "articulada" and (self.mz != 0.0 or self.phi != 0.0):
            print("ERROR! En estructuras articuladas no puede haber momentos o giros en los nudos")
            sys.exit()

    def __str__(self) -> str:
        return (
            f"\t{self.number}\tCoord. globales ({self.x},{self.y}) {LENGTH_UNIT}\n"
            f"\t\tVector de esfuerzos ({self.fx},{self.fy},{self.mz}) {FORCE_UNIT}|{FORCE_UNIT}·{LENGTH_UNIT}\n"
            f"\t\tVector de deformaciones ({self.dx},{self.dy},{self.phi}) {LENGTH_UNIT}|{SPIN_UNIT}\n"
        )
