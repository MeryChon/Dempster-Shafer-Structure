from aggregators.abstract import FuzzyAggregator
from fuzzy_numbers.triangular_fuzzy_number import TriangularFuzzyNumber as TFN


class FuzzyOrderedWeightedAverageAggregator(FuzzyAggregator):
    def aggregate(self):
        result = {}
        for alternative_key, focal_collections in self.payoff_collections.items():
            for focal_elem_key, payoffs in focal_collections.items():
                aggregated_payoff = TFN()
                weight_vector = self.weight_vectors.get(len(payoffs))
                payoffs.sort()
                for index, weight in enumerate(weight_vector):
                    product = payoffs[index].multiply_by_const(weight)
                    aggregated_payoff += product
                result.setdefault(alternative_key, {})[focal_elem_key] = aggregated_payoff

        return result
