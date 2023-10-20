import time
import functions
import multtestlib3 as mtl

# Exemplo de chamada da função test_equal com parâmetros inteiros e cpus como um inteiro

cpus = 4
'''
print("Fotoriais secos:")
start_time = time.time()
functions.now()
for x in range(1, 11):
    print(f"{x} - {functions.factorial_rec(x)}")
end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")
'''
###################################################################################################
print("*****************************************************************************")
print("teste de fatoriais usando array:")
start_time = time.time()
functions.now()
params = []
# for a in range(0, 20):
for b in range(1, 11):
    params.append(b)
print(params)
mtl.test_equal(cpus, params, params, functions.factorial_rec)
end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")

###################################################################################################
print("*****************************************************************************")
print("teste de fatoriais usando int:")
start_time = time.time()
functions.now()
params = []
# for a in range(0, 20):
for b in range(1, 11):
    mtl.test_equal(cpus, b, b, functions.factorial_rec)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")

###################################################################################################
print("*****************************************************************************")
print("comparando dois numeros:")
start_time = time.time()
functions.now()
params = []
# for a in range(0, 20):
for b in range(1, 51):
    mtl.test_equal(cpus, b, 12)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")

###################################################################################################
print("*****************************************************************************")
print("comparando dois vetores:")
start_time = time.time()
functions.now()
params = []
paramsx = []
# for a in range(0, 20):
for b in range(1, 51):
    params.append(b)
for x in range(1, 51):
    if x == 42:
        paramsx.append(41)
    else:
        paramsx.append(x)

print(params)

mtl.test_equal(cpus, params, paramsx)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")

###################################################################################################
print("*****************************************************************************")
print("somando dois por vetor:")
start_time = time.time()
functions.now()
input1 = []
input2 = []
expected = []
# for a in range(0, 20):
for a in range(1, 51):
    input1.append(a)
for b in range(1, 51):
    if b == 42:
        input2.append(10)
    else:
        input2.append(b)
for c in range(1, 51):
    expected.append(c + c)
print(input1)
print(input2)
print(expected)

mtl.test_equal(cpus, input1, expected, functions.soma, input2)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")

###################################################################################################
print("*****************************************************************************")



mtl.test_equal(4, 1, 2, functions.soma, 1)
mtl.test_equal(1, 5, 121, functions.factorial_rec)
mtl.test_equal(1, 5, 120, functions.factorial_rec)



