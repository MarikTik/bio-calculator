import numpy as np
from typing import Dict
from .import data_analysis


def percent_difference(initial_value: float, final_value: float) -> float:
     return abs(initial_value - final_value) / initial_value * 100 


def create_percent_difference_array(reference: Dict[str, int], samples: Dict[str, Dict[str, int]]) -> np.ndarray:
     """Calculate the percent difference of nucleobases for each animal."""
     percent_differences = []
     for _, counted_bases in samples.items():
          differences = [percent_difference(reference[base], counted_bases[base]) for base in counted_bases]
          percent_differences.append(differences)
     return np.array(percent_differences)
