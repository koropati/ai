import numpy as np

class ELECTRE:
    def __init__(self, alternatives, criteria, weights, alternative_labels):
        self.alternatives = alternatives
        self.criteria = criteria
        self.weights = weights
        self.alternative_labels = alternative_labels
        self.normalized_matrix = None
        self.weighted_normalized_matrix = None
        self.concordance_matrix = None
        self.discordance_matrix = None
        self.aggregate_dominance_matrix = None

    def normalize(self):
        # Langkah 1: Normalisasi Matriks Keputusan
        norm_matrix = np.zeros_like(self.criteria, dtype=float)
        for j in range(len(self.criteria[0])):
            column = self.criteria[:, j]
            norm_matrix[:, j] = column / np.sqrt(np.sum(column**2))
        self.normalized_matrix = norm_matrix
        return norm_matrix

    def weighted_normalization(self):
        # Langkah 2: Matriks Normalisasi Terbobot
        self.weighted_normalized_matrix = self.normalized_matrix * self.weights
        return self.weighted_normalized_matrix

    def calculate_concordance_discordance(self):
        # Langkah 3 & 4: Matriks Concordance dan Discordance
        num_alternatives = len(self.alternatives)
        concordance_matrix = np.zeros((num_alternatives, num_alternatives))
        discordance_matrix = np.zeros((num_alternatives, num_alternatives))

        for i in range(num_alternatives):
            for j in range(num_alternatives):
                if i != j:
                    # Subset Concordance dan Discordance
                    concordance_indices = [
                        k for k in range(len(self.criteria[0]))
                        if self.weighted_normalized_matrix[i, k] >= self.weighted_normalized_matrix[j, k]
                    ]
                    discordance_indices = [
                        k for k in range(len(self.criteria[0]))
                        if self.weighted_normalized_matrix[i, k] < self.weighted_normalized_matrix[j, k]
                    ]
                    
                    # Matriks Concordance
                    concordance_value = sum([self.weights[k] for k in concordance_indices])
                    concordance_matrix[i, j] = concordance_value

                    # Matriks Discordance
                    if discordance_indices:
                        discordance_value = max(
                            [abs(self.weighted_normalized_matrix[i, k] - self.weighted_normalized_matrix[j, k]) 
                             for k in discordance_indices]
                        ) / max(
                            [abs(self.weighted_normalized_matrix[a, k] - self.weighted_normalized_matrix[b, k])
                             for a in range(num_alternatives) for b in range(num_alternatives) if a != b for k in range(len(self.criteria[0]))]
                        )
                        discordance_matrix[i, j] = discordance_value

        self.concordance_matrix = concordance_matrix
        self.discordance_matrix = discordance_matrix
        return concordance_matrix, discordance_matrix

    def dominance_matrix(self):
        # Langkah 5: Matriks Dominan Concordance dan Discordance
        c_threshold = np.sum(self.concordance_matrix) / (len(self.alternatives) * (len(self.alternatives) - 1))
        d_threshold = np.sum(self.discordance_matrix) / (len(self.alternatives) * (len(self.alternatives) - 1))

        concordance_dominant = (self.concordance_matrix >= c_threshold).astype(int)
        discordance_dominant = (self.discordance_matrix <= d_threshold).astype(int)
        
        # Langkah 6: Matriks Dominan Agregat (Aggregate Dominance Matrix)
        self.aggregate_dominance_matrix = concordance_dominant * discordance_dominant
        return self.aggregate_dominance_matrix

    def rank_alternatives(self):
        # Langkah 7: Eliminasi Alternatif dan Ranking
        dominance_count = np.sum(self.aggregate_dominance_matrix, axis=1)
        ranked_alternatives = sorted(
            zip(self.alternatives, dominance_count),
            key=lambda x: x[1], reverse=True
        )
        ranked_with_labels = [(alt, self.alternative_labels[alt], score) for alt, score in ranked_alternatives]

        return ranked_with_labels