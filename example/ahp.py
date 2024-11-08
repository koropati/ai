import sys
import os
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import AHP

# Matriks perbandingan berpasangan contoh untuk 7 kriteria
criteria_matrix = np.array([
    [1,   3,   5,   7,   4,   2,   6],
    [1/3, 1,   4,   6,   3,   2,   5],
    [1/5, 1/4, 1,   3,   2,   4,   6],
    [1/7, 1/6, 1/3, 1,   5,   3,   4],
    [1/4, 1/3, 1/2, 1/5, 1,   6,   7],
    [1/2, 1/2, 1/4, 1/3, 1/6, 1,   8],
    [1/6, 1/5, 1/6, 1/4, 1/7, 1/8, 1]
])

# Label untuk setiap kriteria
criteria_labels = [
    "Kecerdasan",
    "Perencanaan",
    "Ketergantungan",
    "Perilaku Reaksi",
    "Kegagalan Kerja",
    "Kuantitas Pekerjaan",
    "Pengetahuan tentang Pekerjaan"
]

# Membuat objek AHP
ahp = AHP(criteria_matrix, criteria_labels)

# Normalisasi dan hitung bobot kriteria
normalized_matrix = ahp.normalize_matrix()
criteria_weights = ahp.calculate_weights()

# Cek konsistensi dan tampilkan hasil hanya sekali
if ahp.is_consistent(threshold=0.3):  # Gunakan threshold lebih tinggi
    print("Matriks konsisten")
    print("Bobot Kriteria:", criteria_weights)
else:
    print("Matriks tidak konsisten. Harap revisi perbandingan berpasangan.")