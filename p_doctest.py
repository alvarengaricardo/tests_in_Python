import functions

def test_slow_function():
    """
    Testa a função lenta (slow_function) do módulo 'functions'.

    Este teste verifica se a função retorna o mesmo valor de entrada (n)
    para um intervalo de valores de n de 50 a 150.

    >>> for i in range(0, 20):
    ...     for n in range(50, 151):
    ...         result = functions.slow_function(n)
    ...         assert result == n
    """
    pass  # O código de teste está incorporado na docstring acima

if __name__ == '__main__':
    import doctest
    doctest.testmod()
