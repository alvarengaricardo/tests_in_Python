import subprocess
import time
from datetime import datetime

nome = "p_pytest.py"
arquivo = open("output.txt", "a")

try:
    print(f"Arquivo: {nome}")
    arquivo.write(f"Arquivo: {nome} com 4 cores\n")

    start_time = time.time()

    command = ["pytest", "-n", "4", "--dist=loadscope", "p_pytest.py"]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    end_time = time.time()

    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    elapsed_time = end_time - start_time

    print(f"Tempo gasto: {elapsed_time} segundos.")
    arquivo.write(f"Tempo gasto: {elapsed_time} segundos.\n")
    arquivo.write("------------------------------------------\n")

except subprocess.CalledProcessError as e:
    print("Error:", e)
finally:
    arquivo.close()
