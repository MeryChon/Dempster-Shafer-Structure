from unittest import TestCase

from fuzzy_numbers.qrofn import QROFN


class TestQROFNInitialisation(TestCase):
    def test_intuitionistic(self):
        num = QROFN(0.2, 0.3)
        self.assertEqual(num.m, 0.2)
        self.assertEqual(num.n, 0.3)
        self.assertEqual(num.q, 1)

    def test_pythagorean(self):
        num = QROFN(0.4, 0.7)
        self.assertEqual(num.m, 0.4)
        self.assertEqual(num.n, 0.7)
        self.assertEqual(num.q, 2)

    def test_high_rung(self):
        num = QROFN(0.8, 0.65)
        self.assertEqual(num.m, 0.8)
        self.assertEqual(num.n, 0.65)
        self.assertEqual(num.q, 3)

    def test_invalid_m(self):
        with self.assertRaises(ValueError) as cm:
            QROFN(-0.3, 0.2)
            self.assertEqual(str(cm.exception), "Membership grades must be positive numbers from [0, 1] interval")

        with self.assertRaises(ValueError) as cm:
            QROFN(1.0001, 0.2)
            self.assertEqual(str(cm.exception), "Membership grades must be positive numbers from [0, 1] interval")

    def test_invalid_n(self):
        with self.assertRaises(ValueError) as cm:
            QROFN(0.3, -0.2)
            self.assertEqual(str(cm.exception), "Membership grades must be positive numbers from [0, 1] interval")

        with self.assertRaises(ValueError) as cm:
            QROFN(0.45, 1.0002)
            self.assertEqual(str(cm.exception), "Membership grades must be positive numbers from [0, 1] interval")

    def test_invalid_q(self):
        with self.assertRaises(ValueError) as cm:
            QROFN(0.8, 0.5, 1)
            self.assertEqual(str(cm.exception), "1 is not a valid rung for provided membership grades")

        with self.assertRaises(ValueError) as cm:
            QROFN(0.8, 0.7, 2)
            self.assertEqual(str(cm.exception), "2 is not a valid rung for provided membership grades")

        with self.assertRaises(ValueError) as cm:
            QROFN(0.8, 0.7, 0)
            self.assertEqual(str(cm.exception), "Rung must be a positive integer")

        with self.assertRaises(ValueError) as cm:
            QROFN(0.8, 0.7, -2)
            self.assertEqual(str(cm.exception), "Rung must be a positive integer")

        with self.assertRaises(ValueError) as cm:
            QROFN(0.8, 0.7, 1.5)
            self.assertEqual(str(cm.exception), "Rung must be a positive integer")

    def test_score(self):
        num = QROFN(0.2, 0.3)
        self.assertEqual(num.score, 0.5)

        num = QROFN(0.7, 0.4)
        self.assertEqual(num.score, 0.65)

    def test_accuracy(self):
        num = QROFN(0.2, 0.3)
        self.assertEqual(num.accuracy, -0.1)

        num = QROFN(0.8, 0.3)
        self.assertEqual(num.accuracy, 0.55)

        num = QROFN(0.7, 0.4)
        self.assertEqual(num.accuracy, 0.33)


class TestQROFNSum(TestCase):
    def test_add_intuitionistic(self):
        a1 = QROFN(0.2, 0.3)
        a2 = QROFN(0.6, 0.2)
        a3 = a1 + a2

        self.assertEqual(a3.m, 0.68)
        self.assertEqual(a3.n, 0.06)
        self.assertEqual(a3.q, 1)

    def test_add_pythagorean(self):
        a1 = QROFN(0.7, 0.5)
        a2 = QROFN(0.3, 0.8)
        a3 = a1 + a2

        self.assertEqual(a3.m, 0.732)
        self.assertEqual(a3.n, 0.4)
        self.assertEqual(a3.q, 2)

    def test_add_different_rung_numbers(self):
        a1 = QROFN(0.9, 0.5)
        a2 = QROFN(0.8, 0.4)
        a3 = a1 + a2

        self.assertEqual(a3.m, 0.954)
        self.assertEqual(a3.n, 0.2)
        self.assertEqual(a3.q, 2)


class TestQROFNMultiply(TestCase):
    def test_multiply_intuitionistic_numbers(self):
        a1 = QROFN(0.2, 0.3)
        a2 = QROFN(0.6, 0.2)
        a3 = a1 * a2

        self.assertEqual(a3.m, 0.12)
        self.assertEqual(a3.n, 0.44)
        self.assertEqual(a3.q, 1)

    def test_multiply_pythagorean_numbers(self):
        a1 = QROFN(0.7, 0.5)
        a2 = QROFN(0.3, 0.8)
        a3 = a1 * a2

        self.assertEqual(a3.m, 0.21)
        self.assertEqual(a3.n, 0.854)
        self.assertEqual(a3.q, 2)

    def test_multiply_different_rung_numbers(self):
        a1 = QROFN(0.9, 0.5)
        a2 = QROFN(0.8, 0.4)
        a3 = a1 * a2

        self.assertEqual(a3.m, 0.72)
        self.assertEqual(a3.n, 0.566)
        self.assertEqual(a3.q, 2)


class TestQROFNMultiplyByScalar(TestCase):
    def test_multiply_intuitionistic_numbers(self):
        pass

    def test_multiply_pythagorean_numbers(self):
        pass

    def test_multiply_higher_order_numbers(self):
        pass

    def test_fail_multiply_by_negative(self):
        pass
