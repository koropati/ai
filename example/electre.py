import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import ELECTRE

# Contoh penggunaan
alternatives = [0, 1, 2]  # Kode alternatif
criteria = np.array([[2, 3, 3, 4, 3, 4, 5], [3, 3, 2, 4, 5, 2, 3], [4, 3, 3, 2, 2, 4, 2]])  # Matriks kriteria
weights = [0.2, 0.15, 0.2, 0.1, 0.15, 0.1, 0.1]  # Bobot kriteria
alternative_labels = {0: "A1", 1: "A2", 2: "A3"}

electre = ELECTRE(alternatives, criteria, weights, alternative_labels)
electre.normalize()
electre.weighted_normalization()
electre.calculate_concordance_discordance()
electre.dominance_matrix()
ranking = electre.rank_alternatives()

print("Peringkat Alternatif:")
for alt, label, score in ranking:
    print(f"{label}: Dominance Score = {score}")
