import functions
import unittest
from unittest_parallel import ConcurrentTestSuite, fork_for_tests

class TestSlowFunction(unittest.TestCase):
    def test_slow_function(self):
        for i in range(0, 20):
            for n in range(1, 101):
                result = functions.slow_function(n)
                self.assertEqual(result, n)

def create_test_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSlowFunction)
    concurrent_suite = ConcurrentTestSuite(suite, fork_for_tests(2))  # Define o número de processos (2)
    return concurrent_suite

if __name__ == '__main__':
    concurrent_suite = create_test_suite()
    unittest.TextTestRunner(verbosity=2).run(concurrent_suite)
