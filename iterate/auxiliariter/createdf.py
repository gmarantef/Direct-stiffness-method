from typing import List
import numpy as np
import pandas as pd

from creator.bo.vectors import WebVector, PositionVector
from assistant.websnames import webs_names


def create_df(final_array: np.ndarray, web_locations: List[WebVector],
              joints_positions: List[PositionVector]) -> pd.DataFrame:

    alphabet_ext: List[str] = webs_names(len(web_locations))

    columns_efforts: List[str] = []
    columns_materials: List[str] = []
    columns_sections: List[str] = []

    for i in range(len(joints_positions)):
        columns_efforts.extend(["fx_" + str(i + 1), "fy_" + str(i + 1), "Mz_" + str(i + 1)])

    for i in range(len(web_locations)):
        columns_materials.append("Material_Web_" + str(alphabet_ext[i]))
        columns_sections.append("Section_Web_" + str(alphabet_ext[i]))

    columns = columns_efforts + columns_materials + columns_sections

    final_df: pd.DataFrame = pd.DataFrame(final_array, columns=columns)

    return final_df
