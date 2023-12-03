import time

import functions

start_time = time.time()

for i in range(0, 20):
    for n in range(1, 101):
        result = functions.slow_function(n)

end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")
