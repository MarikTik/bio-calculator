import matplotlib.pyplot as plt
import numpy as np
from utils.data import data_transform
from typing import List

from utils.data import data_analysis, data_retrieve, data_set


genes_dictionary = data_retrieve.create_gene_dictionary("section2")