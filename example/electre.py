import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import ELECTRE
from utils import ExcelReader

filepath = "data/promosi-jabatan.xlsx"

# Membaca data dari Excel
excel_reader = ExcelReader(filepath)
data = excel_reader.read_excel()

alternatives = data['alternatives']
criteria = data['criteria_values']
weights = data['weights']
alternative_labels = data['alternative_labels']

# Inisialisasi ELECTRE dengan data dari Excel
electre = ELECTRE(alternatives, criteria, weights, alternative_labels)

# Proses ELECTRE
electre.normalize()
electre.weighted_normalization()

# Hitung Matriks Concordance dan Discordance
concordance_matrix, discordance_matrix = electre.calculate_concordance_discordance()

# Tampilkan Matriks Concordance dan Matriks Discordance
print("Matriks Concordance:")
print(concordance_matrix)
print("\nMatriks Discordance:")
print(discordance_matrix)

# Hitung Matriks Dominan Concordance dan Dominan Discordance serta Matriks Dominasi Agregat
aggregate_dominance_matrix = electre.dominance_matrix()

# Tampilkan Matriks Dominan Concordance dan Matriks Dominan Discordance
c_threshold = np.sum(concordance_matrix) / (len(alternatives) * (len(alternatives) - 1))
d_threshold = np.sum(discordance_matrix) / (len(alternatives) * (len(alternatives) - 1))

concordance_dominant = (concordance_matrix >= c_threshold).astype(int)
discordance_dominant = (discordance_matrix <= d_threshold).astype(int)

print("\nMatriks Dominan Concordance (Threshold =", c_threshold, "):")
print(concordance_dominant)
print("\nMatriks Dominan Discordance (Threshold =", d_threshold, "):")
print(discordance_dominant)

# Tampilkan Matriks Dominasi Agregat
print("\nMatriks Dominasi Agregat:")
print(aggregate_dominance_matrix)

# Tampilkan Peringkat Alternatif Berdasarkan ELECTRE
ranking = electre.rank_alternatives()
print("\nPeringkat Alternatif:")
for alt, label, score in ranking:
    print(f"{label}: Dominance Score = {score}")
