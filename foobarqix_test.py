import unittest

def foobarquix (number):
    return "foo"

class FooBarQixTestCase(unittest.TestCase):
    def test_return_Foo_when_number_is_divisible_by_3(self):
        self.assertEqual(foobarquix(3), "Foo")



unittest.main()
