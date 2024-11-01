import numpy as np


class SAW:
    def __init__(self, alternatives, criteria, weights, criteria_type, alternative_labels):
        self.alternatives = alternatives
        self.criteria = criteria
        self.weights = weights
        self.criteria_type = criteria_type
        self.alternative_labels = alternative_labels
        self.normalized_matrix = None
        self.scores = None

    def normalize(self):
        normalized_matrix = np.zeros_like(self.criteria, dtype=float)
        
        for j in range(len(self.criteria[0])):
            column = self.criteria[:, j]
            if self.criteria_type[j] == "benefit":
                normalized_matrix[:, j] = column / column.max()
            elif self.criteria_type[j] == "cost":
                normalized_matrix[:, j] = column.min() / column

        self.normalized_matrix = normalized_matrix
        return normalized_matrix

    def calculate_scores(self):
        if self.normalized_matrix is None:
            self.normalize()
            
        scores = np.dot(self.normalized_matrix, self.weights)
        self.scores = scores
        return scores

    def rank_alternatives(self):
        if self.scores is None:
            self.calculate_scores()

        ranked_alternatives = sorted(
            zip(self.alternatives, self.scores),
            key=lambda x: x[1], reverse=True
        )
        # Gantikan kode alternatif dengan label yang sebenarnya
        ranked_with_labels = [(alt, self.alternative_labels[alt], score) for alt, score in ranked_alternatives]
        
        return ranked_with_labels
