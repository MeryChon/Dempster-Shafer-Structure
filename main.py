from aggregators.FWA import FuzzyWeightedAverageAggregator
from dempster_shafer_structure import DempsterShafer


def get_alternatives():
    return {
        "A1": "computer company",
        "A2": "chemical company",
        "A3": "car company",
        "A4": "TV company",
        "A5": "food company",
    }


def get_states_of_nature():
    return {
        "S1": "Negative growth rate",
        "S2": "Growth rate near 0",
        "S3": "Low growth rate",
        "S4": "Medium growth rate",
        "S5": "High growth rate",
        "S6": "Very high growth rate",
    }


def get_focal_elements():
    return {
        "B1": {
            "states": ["S1", "S2", "S3", "S4"],
            "bpa": 0.4
        },
        "B2": {
            "states": ["S4", "S5", "S6"],
            "bpa": 0.3
        },
        "B3": {
            "states": ["S1", "S3", "S5"],
            "bpa": 0.3
        }
    }


def get_weight_vectors():
    return {
        3: [0.3, 0.3, 0.4],
        4: [0.2, 0.2, 0.3, 0.3]
    }


def get_payoff_matrix_data():
    return {
        "A1": {
            "S1": [50, 60, 70],
            "S2": [40, 50, 60],
            "S3": [20, 40, 60],
            "S4": [50, 60, 70],
            "S5": [70, 80, 90],
            "S6": [70, 80, 90],
        },
        "A2": {
            "S1": [40, 50, 60],
            "S2": [60, 70, 80],
            "S3": [70, 80, 90],
            "S4": [30, 40, 50],
            "S5": [20, 30, 40],
            "S6": [70, 80, 90],
        },
        "A3": {
            "S1": [60, 70, 80],
            "S2": [60, 70, 80],
            "S3": [60, 70, 80],
            "S4": [50, 60, 70],
            "S5": [50, 60, 70],
            "S6": [40, 50, 60],
        },
        "A4": {
            "S1": [10, 20, 30],
            "S2": [10, 20, 30],
            "S3": [60, 70, 80],
            "S4": [60, 70, 80],
            "S5": [70, 80, 90],
            "S6": [70, 80, 90],
        },
        "A5": {
            "S1": [30, 40, 50],
            "S2": [60, 70, 80],
            "S3": [40, 50, 60],
            "S4": [40, 50, 60],
            "S5": [60, 70, 80],
            "S6": [60, 70, 80],
        }
    }


if __name__ == '__main__':
    ds_structure = DempsterShafer(alternatives=get_alternatives(),
                                  states_of_nature=get_states_of_nature(),
                                  focal_elements=get_focal_elements(),
                                  weight_vectors=get_weight_vectors(),
                                  payoff_matrix_data=get_payoff_matrix_data())
    ds_structure.run(FuzzyWeightedAverageAggregator)
    ds_structure.print_report()
