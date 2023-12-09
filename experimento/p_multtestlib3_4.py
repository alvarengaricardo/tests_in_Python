import time
import multtestlib3 as mtl3
import functions


def main():
    cpus = 4
    values = []
    for i in range(0, 20):
        for x in range(1, 101):
            values.append(x)

    values2 = sorted(values, reverse=True)
    print(values2)
    start_time = time.time()
    mtl3.test_equal(cpus, values2, "", values2, functions.slow_function)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()

