import unittest


# This function calculates the factorial of a non negative integer
def factorial(a):
    # a:
    # return
    # factorial (a)
    # ""
    if a==0:
        return 1
    else:
        return a*factorial((a-1))
    # # this function calculates the factorial of two numbers
    # def factorial_of_two_numbers(a,b): 
    #     a*factorial_of_two_numbers((a-1))
    #     b*factorial_of_two_numbers((b-1))
    #     returns:
    #     factorial(a), factorial (b)
        



class testfactorial(unittest.TestCase):
    def test_factorial_of_one_number(self):
        self.assertEqual(factorial(5), 120)
    def test_factorial_of_one_number(self):
        self.assertEqual(factorial(0), 1)


if __name__ == "__main__":
    unittest.main()
