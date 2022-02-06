from abc import abstractmethod


class FuzzyAggregator(object):
    def __init__(self, payoff_collections, weight_vectors):
        self.payoff_collections = payoff_collections
        self.weight_vectors = weight_vectors

    @abstractmethod
    def aggregate(self):
        pass
