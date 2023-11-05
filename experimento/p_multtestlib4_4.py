import multtestlib4 as mtl4
import functions


def main():
    cpus = 4
# Criar a lista "values" usando um loop "for"
    values = []
    print("antes do for")
    for i in range(0, 5):
        for x in range(1, 5):
            values.append(x)

    print("depois do for")
    print(len(values))
    mtl4.test_equal(cpus, values, values, functions.slow_function)
    print("depois do teste")


if __name__ == "__main__":
    print(1)
    mtl4.init()
    print(2)
    mtl4.freeze_support()
    print(3)
    functions.now()
    main()
    functions.now()
    print(4)
    mtl4.end()
    print(5)

