import multtestlib3 as mtl3
import functions


def main():
    cpus = 4
    # Criar a lista "values" usando um loop "for"
    values = []
    for x in range(1, 10001):
        values.append(1000)


    mtl3.test_equal(cpus, values, values, functions.slow_function)

if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()
