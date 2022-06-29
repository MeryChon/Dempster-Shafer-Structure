from pandas import DataFrame
from discrimination_analysis.runner import Runner
from fuzzy_numbers.qrofn import QROFN

diagnoses = ['disease 1', 'disease 2', 'disease 3']
symptoms = ['symptom 1', 'symptom 2', 'symptom 3', 'symptom 4']

focal_elements = [[0, 1],  # TODO let user input this
                  [0, 3],
                  [1, 2, 3]]
focal_element_symptom_weights = [  # TODO let user input this
    [0.4, 0.6],
    [0.7, 0.3],
    [0.1, 0.5, 0.4]
]
focal_probabilities = [0.2, 0.3, 0.5]  # TODO let user input this

user_utility_matrix = [  # TODO let user input this
    [0.2, 0.5, 0.8, 0.2],
    [0.7, 0.6, 0.9, 0.3],
    [0.1, 0.8, 0.3, 0.5]
]


def pair_to_qrofn(pair):
    return QROFN(pair[0], pair[1])


def run():
    initial_utility_matrix = DataFrame(
        data=user_utility_matrix,
        index=diagnoses,
        columns=symptoms
    )

    discrimination_analysis_runner = Runner(initial_utility_matrix)
    orthopair_matrix = discrimination_analysis_runner.get_orthopair_matrix()
    print(orthopair_matrix)

    qrofn_matrix_data = {}

    for row_index, row in orthopair_matrix.iterrows():
        qrofn_matrix_data[row_index] = {}
        for item_index, item in row.iteritems():
            qrofn_matrix_data[row_index][item_index] = pair_to_qrofn(item)

    qrofn_matrix = DataFrame(
        index=orthopair_matrix.index,
        columns=orthopair_matrix.columns
    ).from_dict(qrofn_matrix_data, orient='index')

    print(qrofn_matrix)
