# Questão 04
def mdc(a, b):
    if a == 0 and b == 0:
        return 'indeterminado'
    if a < b:
        return mdc(b, a)
    # Caso Base
    if b == 0:
        return a
    # Recursiv.
    else:
        return mdc(b, a % b)