import numpy as np
class AHP:
    def __init__(self, criteria_matrix, criteria_labels):
        """
        Inisialisasi kelas AHP dengan matriks perbandingan berpasangan dan label kriteria.
        """
        self.criteria_matrix = criteria_matrix
        self.criteria_labels = criteria_labels
        self.normalized_matrix = None
        self.criteria_weights = None
        self.consistency_ratio = None

        # Verifikasi matriks perbandingan berpasangan
        if not self.verify_pairwise_comparison_matrix():
            raise ValueError("Matriks perbandingan berpasangan tidak konsisten.")

    def verify_pairwise_comparison_matrix(self):
        """
        Verifikasi matriks perbandingan berpasangan untuk simetri dan konsistensi dasar.
        """
        n = len(self.criteria_matrix)
        for i in range(n):
            for j in range(i + 1, n):
                if not np.isclose(self.criteria_matrix[i, j], 1 / self.criteria_matrix[j, i]):
                    print(f"Konsistensi gagal antara elemen {i+1} dan {j+1}")
                    return False
        return True

    def normalize_matrix(self):
        """
        Langkah 1: Normalisasi matriks perbandingan berpasangan.
        """
        # Normalisasi matriks berdasarkan kolom
        column_sums = np.sum(self.criteria_matrix, axis=0)
        self.normalized_matrix = self.criteria_matrix / column_sums
        return self.normalized_matrix

    def calculate_weights(self):
        """
        Langkah 2: Menghitung bobot kriteria berdasarkan nilai rata-rata setiap baris matriks yang dinormalisasi.
        """
        if self.normalized_matrix is None:
            self.normalize_matrix()
        self.criteria_weights = np.mean(self.normalized_matrix, axis=1)
        return self.criteria_weights

    def calculate_consistency_ratio(self):
        """
        Langkah 3: Menghitung Rasio Konsistensi (Consistency Ratio - CR) untuk memastikan bahwa matriks perbandingan berpasangan konsisten.
        """
        # Menghitung Consistency Index (CI)
        weighted_sum_vector = np.dot(self.criteria_matrix, self.criteria_weights)
        lambda_max = np.mean(weighted_sum_vector / self.criteria_weights)
        n = len(self.criteria_matrix)
        ci = (lambda_max - n) / (n - 1)

        # Nilai Random Index (RI) untuk berbagai ukuran matriks
        ri_values = {1: 0.00, 2: 0.00, 3: 0.58, 4: 0.90, 5: 1.12,
                     6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45, 10: 1.49}
        
        # Menghitung Consistency Ratio (CR)
        ri = ri_values.get(n, 1.49)  # Mengambil RI berdasarkan ukuran matriks
        self.consistency_ratio = ci / ri if ri != 0 else 0
        return self.consistency_ratio

    def is_consistent(self, threshold=0.1):
        """
        Memeriksa apakah matriks konsisten berdasarkan threshold.
        
        Parameters:
        - threshold (float): Batas maksimum untuk Consistency Ratio (default: 0.1)
        
        Returns:
        - bool: True jika konsisten, False jika tidak.
        """
        if self.consistency_ratio is None:
            self.calculate_consistency_ratio()
        return self.consistency_ratio < threshold

    def get_criteria_weights(self):
        """
        Mengembalikan bobot kriteria setelah memastikan konsistensi.
        """
        if self.criteria_weights is None:
            self.calculate_weights()
        return self.criteria_weights
