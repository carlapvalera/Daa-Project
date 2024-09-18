def conjunto_potencia(n):
    if n == 0:
        yield []
    else:
        for i in conjunto_potencia(n - 1):
            yield [1] + i
            yield [0] + i