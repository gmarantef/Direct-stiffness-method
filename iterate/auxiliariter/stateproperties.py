from typing import List
import pandas as pd
import numpy as np
from itertools import combinations_with_replacement


from properties import NUMBER_STATE_EFFORTS
from creator.bo.vectors import WebVector
from creator.bo.materials import Material
from creator.bo.sections import Section
from creator.itercreator import IterCreator


def state_materials(materials_dataset: pd.DataFrame, web_locations: List[WebVector]) -> np.ndarray:

    random_materials_df: pd.DataFrame = materials_dataset.sample(len(web_locations), replace=False, random_state=1993)

    iter_materials: List[Material] = IterCreator(random_materials_df=random_materials_df).iter_materials

    state_materials_array: np.ndarray = np.array(list(combinations_with_replacement(iter_materials,
                                                                                    len(web_locations))))
    random_index: List[int] = np.random.choice(state_materials_array.shape[0], size=NUMBER_STATE_EFFORTS, replace=False)
    state_materials_array = state_materials_array[random_index, :]

    return state_materials_array


def state_sections(sections_dataset: pd.DataFrame, web_locations: List[WebVector]) -> np.ndarray:

    random_sections_df: pd.DataFrame = sections_dataset.sample(len(web_locations), replace=False, random_state=1993)

    iter_sections: List[Section] = IterCreator(random_sections_df=random_sections_df).iter_sections

    state_sections_array: np.ndarray = np.array(list(combinations_with_replacement(iter_sections,
                                                                                   len(web_locations))))
    random_index: List[int] = np.random.choice(state_sections_array.shape[0], size=NUMBER_STATE_EFFORTS, replace=False)
    state_sections_array = state_sections_array[random_index, :]

    return state_sections_array
