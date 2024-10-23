"""Create a bar graph of the quantitive percent difference of nucleobases relative to homo sapiens"""

import matplotlib.pyplot as plt
import numpy as np
from utils import data_analysis, data_retrieve, data_transform, data_set
from typing import Dict


def get_reference_sample_and_other_samples(
     nucleobases_count_dictionary: Dict[str, Dict[str, int]], reference_name: str
) -> Dict[str, Dict[str, int]]:
     """Extract reference sample and other animal samples."""
     reference_nucleobases_count_dictionary = nucleobases_count_dictionary.get(reference_name, None)
     if not reference_nucleobases_count_dictionary:
          raise KeyError(f"Unable to find {reference_name} in counted nucleotide dictionary")
     
     del nucleobases_count_dictionary[reference_name]
     return reference_nucleobases_count_dictionary, nucleobases_count_dictionary


def create_percent_difference_array(reference: Dict[str, int], samples: Dict[str, Dict[str, int]]) -> np.ndarray:
     """Calculate the percent difference of nucleobases for each animal."""
     percent_differences = []
     for _, counted_bases in samples.items():
          differences = [data_analysis.percent_difference(reference[base], counted_bases[base]) for base in counted_bases]
          percent_differences.append(differences)
     return np.array(percent_differences)
         

genes_dictionary = data_retrieve.create_gene_dictionary("section1")
descriptive_nucleobases_count_dictionary = data_retrieve.create_nucleobases_count_dictionary(genes_dictionary)
nucleobases_count_dictionary = data_transform.simplify_dictionary(descriptive_nucleobases_count_dictionary)

reference_sample_name = "Homo sapiens"
reference_sample, samples = get_reference_sample_and_other_samples(
     nucleobases_count_dictionary, reference_sample_name
)

percent_diff = create_percent_difference_array(reference_sample, samples)
names = list(samples.keys())

 
def plot_relational_percent_differences(percent_diff: np.ndarray, samples: list):
    """Plot percent differences of nucleobases relative to Homo sapiens."""
    x = np.arange(len(samples)) 
    width = 0.15  

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, base in enumerate(data_set.nucleobases):
        ax.bar(x + i * width, percent_diff[:, i], width, label=base)

    ax.set_xlabel("Animals")
    ax.set_ylabel("Percent Difference (%)")
    ax.set_title("Percent Difference of Nucleobases Relative to Homo sapiens")
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(samples, rotation=45, ha='right') 
    ax.legend(title="Nucleobases")

    plt.tight_layout()
    plt.show()

 
if __name__ == "__main__":
    plot_relational_percent_differences(percent_diff, names)