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


def line2(ff, a, b, expected, received):
    return ('Function: ' + str(ff.__name__) + ' a: ' + str(a) + ' b: ' + str(b) + ' expected: ' + str(
        expected) + ' received: ' + str(received) + ' Result: ')


def init():
    if os.path.exists('filetot.txt'):
        os.remove('filetot.txt')

    if os.path.exists('filepass.txt'):
        os.remove('filepass.txt')

    if os.path.exists('filefail.txt'):
        os.remove('filefail.txt')


def end():
    if os.path.exists('filetot.txt'):
        with open('filetot.txt') as f:
            tl = len(f.readlines())
            print('Total: ' + str(tl))
            ft = open('filetot.txt', 'a')
            ft.write('\n')
            ft.write('Total: ' + str(tl))
            ft.close()
    if os.path.exists('filepass.txt'):
        with open('filepass.txt') as f:
            tl = len(f.readlines())
            print('Passed: ' + str(tl))
            fp = open('filepass.txt', 'a')
            fp.write('\n')
            fp.write('Passed: ' + str(tl))
            fp.close()
    if os.path.exists('filefail.txt'):
        with open('filefail.txt') as f:
            tl = len(f.readlines())
            print('Failed: ' + str(tl))
            ff = open('filefail.txt', 'a')
            ff.write('\n')
            ff.write('Failed: ' + str(tl))
            ff.close()
    global vector


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


def about():
    print("")
    print("*** multtestLib *** ")
    print("")
    print(" Python package for running unit tests in parallel processing.")
    print(" Author: Ricardo Ribeiro de Alvarenga")
    print("         ITA - Instituto Tecnologico de Aeronáutica")
    print("         Brazil")
    print(" Version: 2023.4")
    print("")


def sos():
    print("")
    print("")
    print("-----------------------------------------------")
    print("Multtestlib Command       Test")
    print("-----------------------------------------------")
    print("test_equal                a == b")
    print("test_not_equal            a != b")
    print("test_func                 function(a, b) == c")
    print("test_not_func             function(a, b) != c")
    print("test_is                   is a b")
    print("test_is_not               is a not b")
    print("test_in                   is a in b")
    print("test_not_in               is a not in b")
    print("test_instance             is instance(a, b)")
    print("test_not_instance         is not instance(a, b)")
    print("test_almost_equal         round(a - b, 7) == 0")
    print("test_not_almost_equal     round(a - b, 7) != 0")
    print("test_greater              a > b")
    print("test_greater_equal        a >= b")
    print("test_less                 a < b")
    print("test_less_equal           a <= b")
    print("-----------------------------------------------")
    print("")
    print("")
