import time
import multtestlib3 as mtl3


def slow_function(n):
    time.sleep(n)
    return n


def teste(cpu, vetor):
    start_time = time.time()
    mtl3.test_equal(cpu, vetor, "", vetor, slow_function)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"CPUs: {cpu} - Tempo gasto: {elapsed_time} segundos.")


def main():
    vetor = [1] * 128
    print(len(vetor))
    teste(1, vetor)
    teste(2, vetor)
    teste(4, vetor)
    teste(8, vetor)
    teste(16, vetor)
    teste(32, vetor)
    teste(64, vetor)
    teste(128, vetor)
    teste(256, vetor)

if __name__ == "__main__":
    mtl3.init()
    main()
    mtl3.end()
