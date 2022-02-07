from aggregators.abstract import FuzzyAggregator
from fuzzy_numbers.triangular_fuzzy_number import TriangularFuzzyNumber as TFN


class DempsterShafer(object):
    def __init__(self, alternatives, states_of_nature, focal_elements, weight_vectors, payoff_matrix_data,
                 subjective_probability):
        self.alternatives = alternatives
        self.states_of_nature = states_of_nature
        self.focal_elements = focal_elements
        self.weight_vectors = weight_vectors
        self.payoff_matrix = payoff_matrix_data
        self.subjective_probability = subjective_probability
        self.aggregator = None  # type: FuzzyAggregator | None
        self.payoff_collections = {}
        self.aggregated_payoffs = {}
        self.generalized_expected_values = {}

    def run(self, aggregator):
        self._calculate_payoff_collections()
        self.aggregator = aggregator(self.payoff_collections, self.weight_vectors, self.subjective_probability,
                                     len(self.states_of_nature))
        self._calculate_aggregated_payoff()
        self._calculate_generalized_expected_value()

    def print_report(self):
        values_list = [
            {
                "key": alt_key,
                "value": value
            } for alt_key, value in self.generalized_expected_values.items()
        ]
        values_list.sort(key=lambda x: x.get("value"))
        print("====================================")
        print("====== Ordered Alternatives ========")
        for alternative in values_list:
            print(f"{alternative.get('key')}: {round(alternative.get('value'), 2)}")
        best_alt = values_list[0].get("key")
        print(f"The best alternative is {best_alt} - {self.alternatives.get(best_alt)}")
        print("====================================")

    def _calculate_payoff_collections(self):
        print("---- Calculating payoff collections ----")
        for alternative_key, states_data in self.payoff_matrix.items():
            alternative_collection = {}
            for focal_element_key, focal_element_data in self.focal_elements.items():
                states = focal_element_data.get("states")
                for state_key in states:
                    alternative_collection.setdefault(focal_element_key, []).append(
                        TFN(*self.payoff_matrix[alternative_key][state_key]))
            self.payoff_collections[alternative_key] = alternative_collection
        self._print_payoff_collections(self.payoff_collections)
        print("----------------------------------------")

    @staticmethod
    def _print_payoff_collections(collections):
        for alt_key, focal_elems in collections.items():
            print(f"{alt_key}: {{")
            for focal_elem, collection_data in focal_elems.items():
                print(f"\t{focal_elem}: [{', '.join([str(cd) for cd in collection_data])}]")
            print(f"}}")

    def _calculate_aggregated_payoff(self):
        print("---- Calculating aggregated payoffs ----")
        self.aggregated_payoffs = self.aggregator.aggregate()
        self._print_aggregated_payoffs(self.aggregated_payoffs)
        print("-------------------------------------------------")

    @staticmethod
    def _print_aggregated_payoffs(payoffs: dict):
        for alternative_key, focal_elem_aggregated_payoff in payoffs.items():
            print(f"{alternative_key}: {{")
            for focal_elem, aggregated_payoff in focal_elem_aggregated_payoff.items():
                print(f"\t{focal_elem}: {aggregated_payoff}")
            print(f"}}")

    def _calculate_generalized_expected_value(self):
        print("---- Calculating generalized expected values ----")
        for alt_key, focal_elem_aggregated_payoffs in self.aggregated_payoffs.items():
            expected_value = TFN()
            for focal_elem, aggregated_payoff in focal_elem_aggregated_payoffs.items():
                expected_value += aggregated_payoff.multiply_by_const(self.focal_elements.get(focal_elem).get("bpa"))
            self.generalized_expected_values[alt_key] = expected_value
        self._print_generalized_expected_values(self.generalized_expected_values)

        print("-------------------------------------------------")

    @staticmethod
    def _print_generalized_expected_values(generalized_expected_values):
        for alt_key, expected_value in generalized_expected_values.items():
            print(f"{alt_key}: {expected_value}")
