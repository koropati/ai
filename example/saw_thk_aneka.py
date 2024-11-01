import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import SAW
from utils import ExcelReader

filepath = "data/saw-thk-aneka.xlsx"

# Membaca data dari Excel
excel_reader = ExcelReader(filepath)
data = excel_reader.read_excel()

# Memasukkan data ke dalam object SAW
alternatives = data['alternatives']
criteria_values = data['criteria_values']
weights = data['weights']
criteria_type = data['criteria_type']
alternative_labels = data['alternative_labels']

# Membuat object SAW
saw = SAW(alternatives, criteria_values, weights, criteria_type, alternative_labels)

# Melakukan normalisasi dan perhitungan skor
saw.normalize()
scores = saw.calculate_scores()
ranked_alternatives = saw.rank_alternatives()

# Output hasil peringkat dengan nama label
for rank, (alt, label, score) in enumerate(ranked_alternatives, start=1):
    print(f"Rank {rank}: [{alt}] {label} with score {score:.4f}")