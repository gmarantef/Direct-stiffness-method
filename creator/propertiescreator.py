from typing import List
import pandas as pd

from creator.bo.vectors import WebMaterialVector, WebSectionVector
from creator.bo.materials import Material
from creator.bo.sections import Section


class PropertiesCreator:

    def __init__(self, work_materials_dataset: pd.DataFrame = None, work_sections_dataset: pd.DataFrame = None,
                 web_materials: List[WebMaterialVector] = None, web_sections: List[WebSectionVector] = None) -> None:

        self.work_materials_dataset = work_materials_dataset
        self.work_sections_dataset = work_sections_dataset
        self.web_materials = web_materials
        self.web_sections = web_sections

        self.materials = self.create_materials()
        self.sections = self.create_sections()

    def create_materials(self) -> List[Material]:

        materials: List[Material] = []

        for value in self.web_materials:
            for index, row in self.work_materials_dataset.iterrows():
                if row.iloc[0] == value.material_name and row.iloc[1] == value.material_condition:
                    materials.append(Material(row.iloc[0], row.iloc[1], row.iloc[2]))

        return materials

    def create_sections(self) -> List[Section]:

        sections: List[Section] = []

        for value in self.web_sections:
            for index, row in self.work_sections_dataset.iterrows():
                if row.iloc[0] == value.section_name:
                    sections.append(Section(row.iloc[0], row.iloc[1], row.iloc[2]))

        return sections
