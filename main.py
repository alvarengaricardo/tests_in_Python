import subprocess
import time

import functions

# Defina os parâmetros que você deseja enviar para o programa.py

start_time = time.time()
functions.now()

# Chame o programa.py com os parâmetros usando subprocess

try:
    result = subprocess.run(["python", "p_multtestlib.py"], capture_output=True, text=True, check=True)
    # O resultado estará em result.stdout
    print("Output from program.py:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Error:", e)

end_time = time.time()
functions.now()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")

