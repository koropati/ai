import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import ELECTRE
from utils import ExcelReader

filepath = "data/saw-thk-aneka.xlsx"

# Membaca data dari Excel
excel_reader = ExcelReader(filepath)
data = excel_reader.read_excel()

alternatives = data['alternatives']
criteria = data['criteria_values']
weights = data['weights']
# criteria_type = data['criteria_type']
alternative_labels = data['alternative_labels']

electre = ELECTRE(alternatives, criteria, weights, alternative_labels)
electre.normalize()
electre.weighted_normalization()
electre.calculate_concordance_discordance()
electre.dominance_matrix()
ranking = electre.rank_alternatives()

print("Peringkat Alternatif:")
for alt, label, score in ranking:
    print(f"{label}: Dominance Score = {score}")
