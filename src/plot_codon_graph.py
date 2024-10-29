import matplotlib.pyplot as plt
import numpy as np
from utils.data import data_transform
from typing import List, Dict

from utils.data import data_analysis, data_retrieve, data_set


genes_dictionary = data_retrieve.create_gene_dictionary("section3")
genes_dictionary = data_transform.simplify_dictionary(genes_dictionary)

#print(genes_dictionary)
carrier_to_codon_maps = data_retrieve.create_carrier_to_codon_map(genes_dictionary)
reference_sample_name = "Homo sapiens"
reference_sample = carrier_to_codon_maps[reference_sample_name]
del carrier_to_codon_maps[reference_sample_name]

#print("Homo sapiens:", reference_sample)

def calculate_percent_difference(reference: Dict[str, int], sample: Dict[str, int]) -> Dict[str, float]:
    """Calculate percent differences for each codon between the reference and a sample."""
    percent_diff = {}
    all_codons = set(reference.keys()).union(sample.keys())  # Get all codons from both sources

    for codon in all_codons:
        ref_count = reference.get(codon, 0)
        sample_count = sample.get(codon, 0)
        if ref_count == 0 and sample_count == 0:
            percent_diff[codon] = 0  # Avoid division by zero if both counts are zero
        elif ref_count == 0:
            percent_diff[codon] = float('inf')  # Infinite percent difference if reference has 0 count
        else:
            percent_diff[codon] = abs(((sample_count - ref_count) / ref_count)) * 100

    return percent_diff

def plot_percent_differences(reference_sample: Dict[str, int], carriers: Dict[str, Dict[str, int]]):
    """Plot percent differences of codons between the reference sample and carriers."""
    all_codons = sorted(set(reference_sample.keys()).union(
        *[carrier.keys() for carrier in carriers.values()]
    ))  # Collect all unique codons

    num_codons = len(all_codons)
    num_carriers = len(carriers)

    # Create a 2D array of percent differences for each carrier and codon
    percent_diff_matrix = np.zeros((num_carriers, num_codons))
    carrier_names = list(carriers.keys())

    for i, carrier_name in enumerate(carrier_names):
        percent_diff = calculate_percent_difference(reference_sample, carriers[carrier_name])
        for j, codon in enumerate(all_codons):
            percent_diff_matrix[i, j] = percent_diff.get(codon, 0)

    # Plotting grouped bars
    fig, ax = plt.subplots(figsize=(20, 8))
    x = np.arange(num_codons)  # X-axis positions for codons
    width = 0.12  # Width of each bar

    # Plot bars for each carrier
    for i in range(num_carriers):
        ax.bar(x + i * width, percent_diff_matrix[i], width, label=carrier_names[i])

    # Add labels, title, and legend
    ax.set_xlabel("Codons")
    ax.set_ylabel("Percent Difference (%)")
    ax.set_title("Percent Difference of Codons Compared to Homo sapiens")
    ax.set_xticks(x + width * (num_carriers - 1) / 2)
    ax.set_xticklabels(all_codons, rotation=45, ha='right')
    ax.legend(title="Carriers", bbox_to_anchor=(1.05, 1), loc='upper left')

    plt.tight_layout()
    plt.show()

# Call the plotting function
plot_percent_differences(reference_sample, carrier_to_codon_maps)