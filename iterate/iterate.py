from typing import List
import numpy as np
import pandas as pd

from creator.bo.vectors import EffortVector, DeformationVector, WebVector, PositionVector
from assistant.convert import convert_to_list
from iterate.auxiliariter.stateefforts import states_effort
from iterate.auxiliariter.stateproperties import state_materials
from iterate.auxiliariter.stateproperties import state_sections
from iterate.auxiliariter.iterations import iterations
from iterate.auxiliariter.createdf import create_df


def state_iterations(effort_vectors: List[EffortVector], deformation_vectors: List[DeformationVector],
                     joints_positions: List[PositionVector], materials_dataset: pd.DataFrame,
                     sections_dataset: pd.DataFrame, web_locations: List[WebVector]) -> pd.DataFrame:

    effort_list: List[float]
    deformation_list: List[float]
    effort_list, deformation_list = convert_to_list(effort_vectors, deformation_vectors)

    state_efforts_array: np.ndarray = states_effort(effort_list, joints_positions)

    state_materials_array: np.ndarray = state_materials(materials_dataset, web_locations)

    state_sections_array: np.ndarray = state_sections(sections_dataset, web_locations)

    final_array: np.ndarray = iterations(joints_positions, deformation_vectors, web_locations, state_efforts_array,
                                         state_materials_array, state_sections_array)

    final_df: pd.DataFrame = create_df(final_array, web_locations, joints_positions)

    return final_df
