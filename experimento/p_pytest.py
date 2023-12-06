import time
import functions
import pytest

start_time = time.time()


# Use o decorador `@pytest.mark.parametrize` para parametrizar os testes
@pytest.mark.parametrize("n", range(1, 101))
def test_slow_function(n):
    for i in range(0, 20):
        result = functions.slow_function(n)
        assert result == n


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo gasto: {elapsed_time} segundos.")
