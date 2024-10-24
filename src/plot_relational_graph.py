"""Create a bar graph of the quantitive percent difference of nucleobases relative to homo sapiens"""

import matplotlib.pyplot as plt
import numpy as np
from utils import data_analysis, data_retrieve, data_transform, data_set
from typing import List

genes_dictionary = data_retrieve.create_gene_dictionary("section1")
descriptive_nucleobases_count_dictionary = data_retrieve.create_nucleobases_count_dictionary(genes_dictionary)
nucleobases_count_dictionary = data_transform.simplify_dictionary(descriptive_nucleobases_count_dictionary)

reference_sample_name = "Homo sapiens"
reference_sample, samples = data_retrieve.get_reference_and_other_samples(
     nucleobases_count_dictionary, reference_sample_name
)

percent_diff = data_analysis.create_percent_difference_array(reference_sample, samples)
sample_names = list(samples.keys())

 
def plot_relational_percent_differences(percent_diff: np.ndarray, sample_names: List[str]):
    """Plot percent differences of nucleobases relative to Homo sapiens."""
    x = np.arange(len(sample_names)) 
    width = 0.15  

    fig, ax = plt.subplots(figsize=(10, 6))

    for i, base in enumerate(data_set.nucleobases):
        ax.bar(x + i * width, percent_diff[:, i], width, label=base)

    ax.set_xlabel("Animals")
    ax.set_ylabel("Percent Difference (%)")
    ax.set_title("Percent Difference of Nucleobases Relative to Homo sapiens")
    ax.set_xticks(x + width * 1.5)
    ax.set_xticklabels(sample_names, rotation=45, ha='right') 
    ax.legend(title="Nucleobases")

    plt.tight_layout()
    plt.show()

def main():
     plot_relational_percent_differences(percent_diff, sample_names)
 
if __name__ == "__main__":
    main()