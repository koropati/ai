import numpy as np

class VIKOR:
    def __init__(self, alternatives, criteria, weights, alternative_labels):
        self.alternatives = alternatives
        self.criteria = criteria
        self.weights = weights
        self.alternative_labels = alternative_labels
        self.scores = None

    def normalize(self):
        # Normalisasi matriks keputusan
        norm_matrix = np.zeros_like(self.criteria, dtype=float)
        for j in range(len(self.criteria[0])):
            column = self.criteria[:, j]
            norm_matrix[:, j] = (column - column.min()) / (column.max() - column.min())
        return norm_matrix

    def calculate_vikor(self):
        norm_matrix = self.normalize()
        S = np.sum(norm_matrix * self.weights, axis=1)
        R = np.max(norm_matrix * self.weights, axis=1)
        
        S_min, S_max = S.min(), S.max()
        R_min, R_max = R.min(), R.max()
        
        # Hitung nilai Q untuk setiap alternatif
        Q = [
            0.5 * ((S[i] - S_min) / (S_max - S_min)) + 
            0.5 * ((R[i] - R_min) / (R_max - R_min)) for i in range(len(S))
        ]
        
        self.scores = Q
        return Q

    def rank_alternatives(self):
        if self.scores is None:
            self.calculate_vikor()
        
        ranked_alternatives = sorted(
            zip(self.alternatives, self.scores),
            key=lambda x: x[1]
        )
        
        ranked_with_labels = [(alt, self.alternative_labels[alt], score) for alt, score in ranked_alternatives]
        return ranked_with_labels