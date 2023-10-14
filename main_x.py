import subprocess
import time
import functions

# arquivo de log
arquivo = open("log_test_x.txt", "w")
arquivo.write("Inicio do processamento de testes.\n\n")
arquivo.write("------------------------------------------\n")
print("Inicio do processamento de testes.")
functions.now()

nome = "p_multtestlib2_4.py"
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


# ****************************************************************
arquivo.close()
print("Fim de processamento.")
functions.now()

