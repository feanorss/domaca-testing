import unittest
class IntegerSet:
    def __init__(self):
        self.elements = [1, 5, 10]


    def sum_elements(self):
        return sum(self.elements)

    def mean_element(self):
        if self.elements:
            return sum(self.elements) / len(self.elements)
        else:
            return 0

    def max_element(self):
        if self.elements:
            return max(self.elements)
        else:
            None

    def min_element(self):
        if self.elements:
            return min(self.elements)
        else:
            None


class TestIntegerSet(unittest.TestCase):
    def setUp(self):
        # Setup runs before each test method
        self.test_set = IntegerSet()

    def test_sum_elements(self):
        self.assertEqual(self.test_set.sum_elements(), 16)

    def test_mean_element(self):
        self.assertAlmostEqual(self.test_set.mean_element(), 5.333, places=3)

    def test_max_element(self):
        self.assertEqual(self.test_set.max_element(), 10)

    def test_min_element(self):
        self.assertEqual(self.test_set.min_element(), 1)

integer_set = IntegerSet()

print(integer_set.sum_elements())
print(integer_set.mean_element())
print(integer_set.max_element())
print(integer_set.min_element())

if __name__ == '__main__':
    unittest.main()

