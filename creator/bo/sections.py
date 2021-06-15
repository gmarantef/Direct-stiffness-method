import sys

from properties import AREA_UNIT, INERTIA_UNIT, STRUCTURE_TYPE


class Section:

    def __init__(self, name: str, area: float, inertia_x: float) -> None:

        self.name = name
        self.area = area
        if STRUCTURE_TYPE == "articulada":
            self.inertia_x = 0.0
        elif STRUCTURE_TYPE == "no articulada":
            self.inertia_x = inertia_x
        else:
            print("ERROR! Ha introducido incorrectamente el tipo de estructura")
            sys.exit()

    def __str__(self) -> str:
        return (
            f"\t{self.name} -> A = {self.area} {AREA_UNIT}"
            f"/ Ix = {self.inertia_x} {INERTIA_UNIT}\n"
        )
