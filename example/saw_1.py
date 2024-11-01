import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src import SAW

# Contoh penggunaan:
# Matriks keputusan: baris adalah alternatif, kolom adalah kriteria
decision_matrix = np.array([[7, 9, 6],
                            [8, 7, 5],
                            [9, 8, 4]])

# Bobot kriteria (sesuai urutan kriteria dalam matriks keputusan)
criteria_weights = [0.4, 0.35, 0.25]

# Tipe kriteria (benefit: lebih besar lebih baik, cost: lebih kecil lebih baik)
criteria_types = ['benefit', 'benefit', 'cost']

# Inisialisasi objek SAW
saw = SAW(criteria_weights, criteria_types)

# Menghitung peringkat alternatif
ranked_alternatives, scores = saw.rank_alternatives(decision_matrix)

# Output hasil
print("Skor alternatif:", scores)
print("Urutan alternatif (mulai dari skor tertinggi):", ranked_alternatives + 1)  # +1 untuk menyesuaikan dengan urutan manusia