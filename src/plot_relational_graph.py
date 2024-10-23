import matplotlib
import matplotlib.pyplot as plt
import os
import json
from utils import data_transform
from typing import Dict
data_path = os.path.join("data", "data.json")

def create_gene_dictionary() -> Dict[str, str]:
     with open(data_path, "r") as file:
         sections = json.load(file)

     return {data["description"]: data_transform.stringify(data["genes"]) for data in sections["section1"]}
