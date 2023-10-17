from concurrent.futures import ThreadPoolExecutor
import os


def test_equal(process_function, a, b, cpus):
    def run_test(a_item, b_item):
        result = process_function(a_item)
        line = line1('test_equal', result, b_item)
        filepass(line) if result == b_item else filefail(line)

    with ThreadPoolExecutor(max_workers=cpus) as executor:
        for a_item, b_item in zip(a, b):
            executor.submit(run_test, a_item, b_item)



def test_not_equal(a, b):
    line = line1('test_not_equal', a, b)

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        future = executor.submit(filepass, line) if a != b else executor.submit(filefail, line)
        future.result()


def line1(t, a, b=""):
    return str(t) + ' - ' + 'a: ' + str(a) + ' b: ' + str(b) + ' Result: '


def filepass(line):
    line = line + 'Pass'
    ft = open('filetot.txt', 'a')
    ft.write(line + '\n')
    fp = open('filepass.txt', 'a')
    fp.write(line + '\n')
    print(line)


def filefail(line):
    line = line + 'Fail'
    ft = open('filetot.txt', 'a')
    ft.write(line + '\n')
    ff = open('filefail.txt', 'a')
    ff.write(line + '\n')
    print(line)


# Resto do seu código...


def line2(ff, a, b, expected, received):
    return ('Function: ' + str(ff.__name__) + ' a: ' + str(a) + ' b: ' + str(b) + ' expected: ' + str(
        expected) + ' received: ' + str(received) + ' Result: ')

# Resto do seu código...
