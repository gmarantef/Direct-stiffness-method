from typing import List, Tuple
import numpy as np


def final_vectors(k_g: np.ndarray, unknown_deformations: List[float],
                  deformation_list: List[float]) -> Tuple[np.ndarray, np.ndarray]:

    n: int = 0
    final_deformations_vector: np.ndarray = np.empty((len(deformation_list)))

    for index, value in enumerate(deformation_list):
        if value is None:
            final_deformations_vector[index] = unknown_deformations[n]
            n += 1
        else:
            final_deformations_vector[index] = deformation_list[index]

    final_efforts_vector: np.ndarray = np.dot(k_g, np.transpose(np.array(final_deformations_vector)))

    return final_efforts_vector, final_deformations_vector
