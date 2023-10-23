import functions
import pytest

def test_slow_function():
    for n in range(1, 10001):
        result = functions.slow_function(1000)
        assert result == 1000

if __name__ == '__main__':
    pytest.main(["-n", "4", __file__])
