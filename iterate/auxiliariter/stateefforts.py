from typing import List
import numpy as np
import random

from properties import NUMBER_STATE_EFFORTS, EFFORT_MAX
from creator.bo.vectors import PositionVector
from assistant.banlist import ban


def states_effort(effort_list: List[float], joints_positions: List[PositionVector]) -> np.ndarray:

    ban_list: np.ndarray = ban(joints_positions)

    state_efforts_array: np.ndarray = np.empty([NUMBER_STATE_EFFORTS, len(effort_list)], dtype=float)

    for i in range(state_efforts_array.shape[0]):
        for j in range(state_efforts_array.shape[1]):
            if effort_list[j] is not None and j not in ban_list:
                state_efforts_array[i, j] = random.randint(- EFFORT_MAX, EFFORT_MAX)
            elif effort_list[j] is None and j not in ban_list:
                state_efforts_array[i, j] = effort_list[j]
            elif j in ban_list:
                state_efforts_array[i, j] = 0.0

    return state_efforts_array
