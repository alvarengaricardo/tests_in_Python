import time


def fibonacci_rec(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        next_fib = fib[i - 1] + fib[i - 2]
        fib.append(next_fib)
    return fib[n]

def slow_function(n):
    time.sleep(n/10)
    return n

def factorial_rec(n):
    s = n / 10
    time.sleep(s)
    if n == 0:
        return 1
    else:
        return n * factorial_rec(n - 1)

def factorial(n):
    if n < 0:
        return None  # O fatorial de números negativos não está definido
    elif n == 0:
        return 1  # O fatorial de 0 é 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result









