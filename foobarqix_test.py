import unittest
from foobarqix import foobarquix

class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarquix(3), "Foo")
        self.assertEqual(foobarquix(6), "Foo")
        self.assertEqual(foobarquix(9), "Foo")


    def test_return_Bar_when_number_is_divisible_by_5(self):
        self.assertEqual(foobarquix(5), "Bar")

    def test_return_Qix_when_number_is_divisible_by_7(self):
        self.assertEqual(foobarquix(7), "Qix")

    def test_return_FooBar_when_number_is_divisible_by_5_and_3(self):
        self.assertEqual(foobarquix(15), "FooBar")

    def test_return_number_as_a_string_otherwise(self):
        self.assertEqual(foobarquix(1), "1")
        self.assertEqual(foobarquix(2), "2")


unittest.main()
