import multtestlib2
import functions
from concurrent.futures import ThreadPoolExecutor

# Criar a lista "values" usando um loop "for"
values = []
for i in range(0, 20):
    for x in range(1, 101):
        values.append((functions.slow_function, x, '', x))

with ThreadPoolExecutor(max_workers=4) as executor:
    # Usando executor.map para iterar a função em paralelo
    executor.map(lambda args: multtestlib2.test_func(*args), values)



