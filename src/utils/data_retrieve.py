import os
import json
from typing import Dict
from . import data_transform, data_set

data_path = os.path.join("data", "data.json")

def create_gene_dictionary(section: str) -> Dict[str, str]:
     """Load and process the gene data from the JSON file."""
     with open(data_path, "r") as file:
         sections = json.load(file)

     return {
          data["description"]: data_transform.stringify(data["genes"]) 
          for data in sections[section]
     }

def create_nucleobases_count_dictionary(genes_dictionary: Dict[str, str]) -> Dict[str, Dict[str, int]]:
     """Count occurrences of nucleobases for each carrier."""
     nucleobases_count_dictionary = dict()
     for carrier, gene in genes_dictionary.items():
          nucleobases_count: Dict[str, int] = {nucleobase : 0 for nucleobase in data_set.nucleobases}
          for nucleobase in gene:
               nucleobases_count[nucleobase] += 1
          nucleobases_count_dictionary[carrier] = nucleobases_count
     return nucleobases_count_dictionary

def get_reference_and_other_samples(
     samples_nucleobases_count_dictionary: Dict[str, Dict[str, int]], reference_name: str
) -> Dict[str, Dict[str, int]]:
     """Extract reference sample and other animal samples."""
     reference_nucleobases_count_dictionary = samples_nucleobases_count_dictionary.get(reference_name, None)
     if not reference_nucleobases_count_dictionary:
          raise KeyError(f"Unable to find {reference_name} in counted nucleotide dictionary")
     
     del samples_nucleobases_count_dictionary[reference_name]
     return reference_nucleobases_count_dictionary, samples_nucleobases_count_dictionary