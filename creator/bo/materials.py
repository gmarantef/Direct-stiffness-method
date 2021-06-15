from properties import PRESSURE_UNIT


class Material:

    def __init__(self, name: str, condition: str, elastic_modulus: float) -> None:

        self.name = name
        self.condition = condition
        self.elastic_modulus = elastic_modulus

    def __str__(self) -> str:
        return (
            f"\t{self.name} en condición {self.condition} "
            f"-> E = {self.elastic_modulus} {PRESSURE_UNIT}\n"
        )
