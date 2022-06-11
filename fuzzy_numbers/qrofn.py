import decimal


class QROFN(object):
    _m = None
    _n = None
    _q = None
    _score = None
    _accuracy = None

    def __init__(self, m, n, q=None):
        self.validate(m, n, q)
        self._m = decimal.Decimal(str(m))
        self._n = decimal.Decimal(str(n))
        self._q = decimal.Decimal(str(q)) if q else QROFN.calculate_rung(self._m, self._n)
        self._score = self.calculate_score()
        self._accuracy = self.calculate_accuracy()

    @property
    def m(self):
        return float(self._m)

    @property
    def n(self):
        return float(self._n)

    @property
    def q(self):
        return float(self._q)

    @property
    def score(self):
        return float(self._score)

    @property
    def accuracy(self):
        return float(self._accuracy)

    def validate(self, m, n, q):
        if m < 0 or m > 1 or n < 0 or n > 1:
            raise ValueError("Membership grades must be positive numbers from [0, 1] interval")

        if q is not None and (not isinstance(q, int) or q < 0):
            raise ValueError("Rung must be a positive integer")

        if q is not None and self.calculate_rung(m, n) > q:
            raise ValueError(f"{q} is not a valid rung for provided membership grades")

    def __str__(self):
        return f"<{self.m}, {self.n}, {self.q}>"

    def __add__(self, other):
        rung = int(max(self.q, other.q))
        m_sum = (self._m ** rung + self._n ** rung - self._m ** rung * self._n ** rung) ** decimal.Decimal(
            str(1 / rung))
        n_sum = self._n * self._m
        return QROFN(m_sum, n_sum, rung)

    def __mul__(self, other):
        if isinstance(other, QROFN):
            rung = max(self._q, other._q)
            m_product = self._m * other._m
            n_product = (1 - (1 - self._n ** rung) * (1 - other._n ** rung)) ** (1 / rung)
            product = QROFN(m_product, n_product, rung)
        elif type(other) in [int, float, decimal.Decimal]:
            if other < 0:
                raise ValueError("Multiplication by negative scalar is not defined")
            m_product = (1 - (1 - self._m ** self._q) ** other) ** (1 / self._q)
            n_product = self._n ** self._q
            product = QROFN(m_product, n_product)
        else:
            raise TypeError

        return product

    def __gt__(self, other):
        # Total ordering
        if self.score > other.score:
            return True
        if self.score == other.score:
            return self.accuracy > other.accuracy

        return False

    def __eq__(self, other):
        # Total ordering equality
        return self.score == other.score and self.accuracy == other.accuracy

    @classmethod
    def calculate_rung(cls, m, n):
        rung = 1
        power_sum = m + n
        while power_sum > 1:
            rung += 1
            power_sum = m ** rung + n ** rung
        return rung

    def calculate_score(self):
        return self._m ** self._q + self._n ** self._q

    def calculate_accuracy(self):
        return self._m ** self._q - self._n ** self._q
