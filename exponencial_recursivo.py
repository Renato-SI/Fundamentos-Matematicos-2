# Questão 02
def exponencial(a, n):
    if a == 0 and n == 0:
        return 'impossivel calcular'
    if n < 0:
        return 'O n (expoente) deve ser maior ou igual a 0'
    # Caso Base
    if n == 0:
        return 1
    # Recursiv.
    else:
        return a * exponencial(a, n - 1)