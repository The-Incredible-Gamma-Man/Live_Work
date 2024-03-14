import unittest
from Decorator import your_decorator_function

class TestDecorator(unittest.TestCase):

    def test_decorator(self):
        # Example test case for your decorator
        @your_decorator_function
        def sample_function():
            return "Original Function Executed"

        result = sample_function()
        # Replace 'Expected Result' with the expected outcome of your decorator
        self.assertEqual(result, "Expected Result")

if __name__ == '__main__':
    unittest.main()
