from abc import abstractmethod


class FuzzyAggregator(object):
    payoff_collections: dict
    weight_vectors: dict
    subjective_probability: list
    num_attributes: int

    def __init__(self, payoff_collections, weight_vectors, subjective_probability=None, num_states=None):
        self.payoff_collections = payoff_collections
        self.weight_vectors = weight_vectors
        self.subjective_probability = subjective_probability
        self.num_attributes = num_states

    @abstractmethod
    def aggregate(self):
        pass
