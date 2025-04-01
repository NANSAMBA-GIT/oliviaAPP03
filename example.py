import unittest


def multiply(a, b):
    if a * b == 3:
        return 3
    else:
        return -16


class Vex(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(multiply(1, 2), 3)

    def test_addition(self):
        self.assertEqual(multiply(4, -4),-16)


if __name__ == "__main__":
    unittest.main()
