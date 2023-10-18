import multtestlib3 as mtl3
import functions

def main():
    cpus = 2
# Criar a lista "values" usando um loop "for"
    values = []
    for i in range(0, 20):
        for x in range(1, 101):
            values.append(x)

    mtl3.test_equal(functions.slow_function, values, values, cpus)


if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()


