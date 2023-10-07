import sys
import time
import functions
import unittest


# from recursos.program import arg1


# arg1 = int(sys.argv[1])+1
# soma = 0

# class TestFiboFunction(unittest.TestCase):
#   def test_fibo_function(self):
#      for n in range(30, 36):
# start_time = time.time()
#         fibo_rec = functions.fibonacci_rec(n)
#        fibo = functions.fibonacci(n)
#       self.assertEqual(fibo_rec, fibo)
# end_time = time.time()
# elapsed_time = end_time - start_time
# if(fibo==fibo_rec):
#    print("ok")
# print(f"Fibonacci {n}: {fibo_rec} - {elapsed_time} segundos")
# soma += elapsed_time

# print(f"Total: {soma} segundos")


class TestSlowFunction(unittest.TestCase):
    def test_slow_function(self):
        for i in range(0, 20):
            for n in range(50, 151):
                result = functions.slow_function(n)
                self.assertEqual(result, n)


if __name__ == '__main__':
    unittest.main()
