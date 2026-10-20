# Questão 03
def exponencial_modualr(a, n, m):
    if m <= 1 or (a == 0  and n == 0):
        return 'impossível calcular'
    # Cso Base
    if n == 0:
        return 1
    # Recursividades.
    if n % 2 == 0:
        metade = exponencial_modualr(a, n // 2, m)
        return (metade * metade) % m
    else:
        return (a * exponencial_modualr(a, n - 1, m)) % m 