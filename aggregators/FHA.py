from aggregators.abstract import FuzzyAggregator
from fuzzy_numbers.triangular_fuzzy_number import TriangularFuzzyNumber as TFN


class FuzzyHybridAverageAggregator(FuzzyAggregator):
    def aggregate(self):
        result = {}
        for alternative_key, focal_collections in self.payoff_collections.items():
            for focal_elem_key, payoffs in focal_collections.items():
                aggregated_payoff = TFN()
                weight_vector = self.weight_vectors.get(len(payoffs))
                payoffs = self.get_sorted_payoffs(payoffs)
                for index, weight in enumerate(weight_vector):
                    product = payoffs[index].multiply_by_const(weight)
                    aggregated_payoff += product
                result.setdefault(alternative_key, {})[focal_elem_key] = aggregated_payoff

        return result

    def get_sorted_payoffs(self, payoffs):
        weighted_values = []
        for index, payoff in enumerate(payoffs):
            weighted_value = payoff.multiply_by_const(self.num_attributes * self.subjective_probability[index])
            weighted_values.append(weighted_value)
        weighted_values.sort()

        return weighted_values
