import functions
import unittest
import time


class TestSlowFunction(unittest.TestCase):
    def test_slow_function(self):
        for i in range(0, 20):
            for n in range(1, 101):
                result = functions.slow_function(n)
                self.assertEqual(result, n)


if __name__ == '__main__':
    start_time = time.time()
    unittest.main()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
