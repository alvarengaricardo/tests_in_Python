import subprocess
import time
import functions

# arquivo de log
arquivo = open("log_test_t2.txt", "w")
arquivo.write("Inicio do processamento de testes.\n\n")
arquivo.write("------------------------------------------\n")
print("Inicio do processamento de testes.")
functions.now()

#----------------------------------------------------------------------------

nome = "p_pytest.py"
try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome} com 128 cores\n")
    start_time = time.time()
    command = ["pytest", "-n", "8", "p_pytest.py"]
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

nome = "p_multtestlib3_8.py"
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
arquivo.close()
print("Fim de processamento.")
functions.now()
