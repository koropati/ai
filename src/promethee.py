import numpy as np

class PROMETHEE:
    def __init__(self, alternatives, criteria, weights, preference_type, alternative_labels):
        self.alternatives = alternatives
        self.criteria = criteria
        self.weights = weights
        self.preference_type = preference_type
        self.alternative_labels = alternative_labels

    def calculate_preference_matrix(self):
        num_alternatives = len(self.alternatives)
        preference_matrix = np.zeros((num_alternatives, num_alternatives))

        for i in range(num_alternatives):
            for j in range(num_alternatives):
                if i != j:
                    preference_score = 0
                    for k in range(len(self.criteria[0])):
                        diff = self.criteria[i, k] - self.criteria[j, k]
                        if self.preference_type[k] == "benefit" and diff > 0:
                            preference_score += self.weights[k]
                        elif self.preference_type[k] == "cost" and diff < 0:
                            preference_score += self.weights[k]
                    preference_matrix[i, j] = preference_score

        return preference_matrix

    def calculate_flows(self):
        preference_matrix = self.calculate_preference_matrix()
        positive_flow = np.sum(preference_matrix, axis=1) / (len(self.alternatives) - 1)
        negative_flow = np.sum(preference_matrix, axis=0) / (len(self.alternatives) - 1)
        net_flow = positive_flow - negative_flow
        return net_flow

    def rank_alternatives(self):
        net_flows = self.calculate_flows()
        ranked_alternatives = sorted(
            zip(self.alternatives, net_flows),
            key=lambda x: x[1], reverse=True
        )
        
        ranked_with_labels = [(alt, self.alternative_labels[alt], score) for alt, score in ranked_alternatives]
        return ranked_with_labels