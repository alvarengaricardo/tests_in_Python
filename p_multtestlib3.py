import time
import functions
import multtestlib3 as mtl

# Exemplo de chamada da função test_equal com parâmetros inteiros e cpus como um inteiro

cpus = 4
'''
start_time = time.time()
functions.now()
params = []
#for a in range(0, 20):
for b in range(50, 151):
#        params.append(b)
    functions.slow_function(b)
    print(b)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")
'''

# ///////////////////////////////

start_time = time.time()
functions.now()
params = []
# for a in range(0, 20):
for b in range(50, 151):
    params.append(b)

print(params)

mtl.test_equal(functions.slow_function, params, params, cpus)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")

print("*****************************************************************")
start_time = time.time()
functions.now()
for x in range(1, 31):
    print(f"{x} - {functions.factorial_rec(x)}")
end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")


start_time = time.time()
functions.now()
params = []
# for a in range(0, 20):
for b in range(1, 31):
    params.append(b)

print(params)

mtl.test_equal(functions.factorial_rec, params, params, cpus)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")


