from typing import List
import pandas as pd

from creator.bo.materials import Material
from creator.bo.sections import Section


class IterCreator:

    def __init__(self, random_materials_df: pd.DataFrame = None, random_sections_df: pd.DataFrame = None) -> None:

        self.random_materials_df = random_materials_df
        self.random_sections_df = random_sections_df

        self.iter_materials = self.create_materials()
        self.iter_sections = self.create_sections()

    def create_materials(self) -> List[Material]:

        iter_materials: List[Material] = []

        for index, row in self.random_materials_df.iterrows():
            iter_materials.append(Material(row.iloc[0], row.iloc[1], row.iloc[2]))

        return iter_materials

    def create_sections(self) -> List[Section]:

        iter_sections: List[Section] = []

        for index, row in self.random_sections_df.iterrows():
            iter_sections.append(Section(row.iloc[0], row.iloc[1], row.iloc[2]))

        return iter_sections
