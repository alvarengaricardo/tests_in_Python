import functions
import unittest


class TestSlowFunction(unittest.TestCase):
    def test_slow_function(self):
        for i in range(0, 20):
            for n in range(50, 151):
                result = functions.slow_function(n)
                self.assertEqual(result, n)


if __name__ == '__main__':
    unittest.main()
