# Questão 04
def mdc(a, b):
    if a < b:
        return mdc(b, a)
    # Caso Base
    if b == 0:
        return a
    # Recursiv.
    else:
        return mdc(a, a % b)
    