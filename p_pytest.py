import functions
import pytest

def test_slow_function():
    for i in range(0, 20):
        for n in range(1, 101):
            result = functions.slow_function(n)
            assert result == n

if __name__ == '__main__':
    pytest.main([__file__])
