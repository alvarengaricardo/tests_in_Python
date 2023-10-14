import functions
import pytest

# Use o decorador `@pytest.mark.parametrize` para parametrizar os testes
@pytest.mark.parametrize("n", range(1, 101))
def test_slow_function(n):
    for i in range(0, 20):
        result = functions.slow_function(n)
        assert result == n

if __name__ == '__main__':
    pytest.main(["-n", "1"])  # "-n 1" permite que o pytest use 1 núcleo de CPU
