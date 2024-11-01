import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import PROMETHEE
from utils import ExcelReader

filepath = "data/saw-thk-aneka.xlsx"

# Membaca data dari Excel
excel_reader = ExcelReader(filepath)
data = excel_reader.read_excel()

alternatives = data['alternatives']
criteria = data['criteria_values']
weights = data['weights']
preference_type = data['criteria_type']
alternative_labels = data['alternative_labels']

promethee = PROMETHEE(alternatives, criteria, weights, preference_type, alternative_labels)
ranking = promethee.rank_alternatives()

print("Peringkat Alternatif:")
for alt, label, score in ranking:
    print(f"{label}: Dominance Score = {score}")
