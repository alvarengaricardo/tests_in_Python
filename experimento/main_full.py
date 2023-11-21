import subprocess
import time
import functions

# arquivo de log
arquivo = open("log_test_full_cenario_2_aprimorado.txt", "w")
arquivo.write("Inicio do processamento de testes.\n\n")
arquivo.write("------------------------------------------\n")
print("Inicio do processamento de testes.")
functions.now()
start_time_global = time.time()
nome = "reference.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_unittest.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_doctest.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_multtestlib_1.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_multtestlib_2.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_multtestlib_4.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------
nome = "p_pytest.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome} com 1 core.\n")
    start_time = time.time()
    command = ["pytest", "-n", "1", "p_pytest.py"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_pytest.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome} com 2 cores\n")
    start_time = time.time()
    command = ["pytest", "-n", "2", "p_pytest.py"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_pytest.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome} com 4 cores\n")
    start_time = time.time()
    command = ["pytest", "-n", "4", "p_pytest.py"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------


nome = "p_multtestlib3_1.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_multtestlib3_2.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ----------------------------------------------------------------------------

nome = "p_multtestlib3_4.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome}.\n")
    start_time = time.time()
    result = subprocess.run(["python", nome], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    # print("Output from program.py:", result.stdout)
    end_time = time.time()
    functions.now()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")
except subprocess.CalledProcessError as e:
    print("Error:", e)

# ****************************************************************
end_time_global = time.time()
elapsed_time_global = end_time_global - start_time_global
print(f"Tempo global: {elapsed_time_global} segundos.")
arquivo.write("------------------------------------------\n")
arquivo.write(f"Tempo global: {elapsed_time_global} segundos.\n")
arquivo.write("------------------------------------------\n")
arquivo.close()
print("Fim de processamento.")
functions.now()
