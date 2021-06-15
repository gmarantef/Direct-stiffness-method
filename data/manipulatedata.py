import pandas as pd

from properties import PRESSURE_UNIT, AREA_UNIT, INERTIA_UNIT


def manipulate_materials_dataset(materials_dataset: pd.DataFrame) -> pd.DataFrame:

    name_elastic_modulus = "Elastic Modulus (psi)"
    work_materials_dataset: pd.DataFrame = materials_dataset.loc[:, ["Material",
                                                                     "Condition",
                                                                     name_elastic_modulus]]

    modifier: float = 0.0
    if PRESSURE_UNIT == "kg/cm^2":
        modifier = 1 / 14.22
    elif PRESSURE_UNIT == "N/m^2" or PRESSURE_UNIT == "Pa":
        modifier = 6894.76
    elif PRESSURE_UNIT == "kN/m^2" or PRESSURE_UNIT == "kPa":
        modifier = 6894.76e-3
    elif PRESSURE_UNIT == "N/mm^2" or PRESSURE_UNIT == "MPa":
        modifier = 6894.76e-6
    elif PRESSURE_UNIT == "kN/mm^2" or PRESSURE_UNIT == "GPa":
        modifier = 6894.76e-9
    elif PRESSURE_UNIT == "atm":
        modifier = 1 / 14.70
    elif PRESSURE_UNIT == "bar":
        modifier = 1 / 14.50
    elif PRESSURE_UNIT == "psi":
        modifier = 1 / 1.00
    elif PRESSURE_UNIT == "kpsi":
        modifier = 1 / 1000.00

    work_materials_dataset.loc[:, name_elastic_modulus] *= modifier

    work_materials_dataset = work_materials_dataset.rename(columns={
                                                        name_elastic_modulus: f"Elastic Modulus ({PRESSURE_UNIT})"
                                                    }, inplace=False)

    return work_materials_dataset


def manipulate_sections_dataset(sections_dataset: pd.DataFrame) -> pd.DataFrame:

    name_section = "Términos de sección"
    name_area = "A (cm2)"
    name_inertia = "Ix (cm4)"
    work_sections_dataset: pd.DataFrame = sections_dataset.loc[:, [("Perfil", "Unnamed: 0_level_1"),
                                                                   (name_section, name_area),
                                                                   (name_section, name_inertia)]]

    modifier: float = 0.0
    if AREA_UNIT == "km^2":
        modifier = 1 / 1.00e10
    elif AREA_UNIT == "m^2":
        modifier = 1 / 1.00e4
    elif AREA_UNIT == "dm^2":
        modifier = 1 / 1.00e2
    elif AREA_UNIT == "cm^2":
        modifier = 1.00
    elif AREA_UNIT == "mm^2":
        modifier = 1.00e2

    work_sections_dataset.loc[:, (name_section, name_area)] *= modifier

    if INERTIA_UNIT == "km^4":
        modifier = 1 / 1.00e12
    elif INERTIA_UNIT == "m^4":
        modifier = 1 / 1.00e8
    elif INERTIA_UNIT == "dm^4":
        modifier = 1 / 1.00e4
    elif INERTIA_UNIT == "cm^4":
        modifier = 1.00
    elif INERTIA_UNIT == "mm^4":
        modifier = 1.00e4

    work_sections_dataset.loc[:, (name_section, name_inertia)] *= modifier

    work_sections_dataset = work_sections_dataset.rename(columns={
                                                        name_area: f"A ({AREA_UNIT})",
                                                        name_inertia: f"Ix ({INERTIA_UNIT})"
                                                    }, inplace=False)

    return work_sections_dataset
