import time
from recursos.testes_pacotes import multtestlib3 as mtl3
import functions


def main():
    cpus = 4
# Criar a lista "values" usando um loop "for"
    values = []
    values2 = []
    for i in range(0, 20):
        for x in range(1, 101):
            values.append(x)

    functions.now()
    start_time = time.time()
    mtl3.test_equal(cpus, values, "", values, functions.slow_function)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()

