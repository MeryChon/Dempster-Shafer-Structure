from pandas import DataFrame


class Runner:
    frequency_matrix = None  # type: DataFrame
    large_ratio_fn = None  # function

    def __init__(self, frequency_matrix, large_ratio_fn=None):
        self.frequency_matrix = frequency_matrix
        if large_ratio_fn:
            self.large_ratio_fn = large_ratio_fn
        else:
            self.large_ratio_fn = self._default_large_ratio_function

    @staticmethod
    def _default_large_ratio_function(ratio):
        if ratio > 3:
            return 1

        if ratio < 0.1:
            return 0

        return round(0.34 * ratio - 0.034, 2)

    def _calculate_positive_discrimination(self, current_index, row):
        total = 0
        fixed_freq = row[current_index]
        for i, freq in enumerate(row):
            if i == current_index:
                continue
            total += self.large_ratio_fn(fixed_freq / row[i]) / (len(row) - 1)

        return round(total, 2)

    def _calculate_negative_discrimination(self, current_index, row):
        total = 0
        fixed_freq = row[current_index]
        for i, freq in enumerate(row):
            if i == current_index:
                continue
            total += self.large_ratio_fn(row[i] / fixed_freq) / (len(row) - 1)

        return round(total, 2)

    def get_orthopair_matrix(self):
        # TODO normalize values!!!
        data = {}
        for row_index, row in self.frequency_matrix.iterrows():
            data[row_index] = {}
            for item_index, frequency in row.iteritems():
                positive_discrimination = self._calculate_positive_discrimination(item_index, row)
                negative_discrimination = self._calculate_negative_discrimination(item_index, row)
                data[row_index][item_index] = (positive_discrimination, negative_discrimination)

        result = DataFrame(index=self.frequency_matrix.index,
                           columns=self.frequency_matrix.columns).from_dict(data, orient='index')
        return result