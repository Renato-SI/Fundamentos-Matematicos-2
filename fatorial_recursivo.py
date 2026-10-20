# Questão 01
def fatorial(n):
    # Caso Base
    if n == 0:
        return 1
    elif n < 0:
        return 0
    # Recursiv.
    else:
        return n * fatorial(n - 1)