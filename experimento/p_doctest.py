import functions
import time

def test_slow_function():
    """
    Testa a função lenta (slow_function) do módulo 'functions'.

    Este teste verifica se a função retorna o mesmo valor de entrada (n)
    para um intervalo de valores de n de 50 a 150.

    >>> for i in range(0, 20):
    ...     for n in range(1, 101):
    ...         result = functions.slow_function(n)
    ...         assert result == n
    """
    pass  # O código de teste está incorporado na docstring acima

if __name__ == '__main__':
    import doctest
    start_time = time.time()
    doctest.testmod()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tempo gasto: {elapsed_time} segundos.")
