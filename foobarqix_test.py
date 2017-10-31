import unittest


def is_divisible(number, divisor):
    return number % divisor == 0


def foobarquix(number):
    result = ""
    if is_divisible(number, 3):
        result += "Foo"
    if is_divisible(number, 5):
        result += "Bar"
    if is_divisible(number, 7):
        result += "Qix"
return = result


class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarquix(3), "Foo")
        self.assertEqual(foobarquix(15), "FooBar")

    def test_return_Bar_when_number_is_divisible_by_5(self):
        self.assertEqual(foobarquix(5), "Bar")


    def test_return_Qix_when_number_is_divisible_by_7(self):
        self.assertEqual(foobarquix(7), "Qix")

        def test_return_Qix_when_number_is_divisible_by_5_and_3(self):
            self.assertEqual(foobarquix(15), "FooBar")


unittest.main()
