import unittest


def multiply(a, b):
    return a*b


class testmultiply(unittest.TestCase):
    def test_multiply_ones(self):
        self.assertEqual(multiply(1, 1), 1)

    def test_multiply_two(self):
        self.assertEqual(multiply(2, 2), 4)
        
    def test_addition(self):
        self.assertEqual(multiply(3, 3),9)

    def test_addition(self):
        self.assertEqual(multiply(4, 4), 16)



if __name__ == "__main__":
    unittest.main()
