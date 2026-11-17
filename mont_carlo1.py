"""
Dois amigos combinam de se encontrar em determinado local, mas cada um
chegará em um horário aleatório dentro de um intervalo de 60 minutos.
Ambos podem esperar até 15 minutos pelo outro.

Utilize uma simulação de Monte Carlo para estimar a probabilidade de
que os dois amigos consigam se encontrar.
"""

import random
def gerar_dados(tempo):
    """
    Função que gera os dados do Problema.
    """
    return [random.uniform(0, tempo) for k in range(2)]

def testar_dados(dados:list, valor):
    """
    Função que testa os dados de acordo com as restrições do problema.
    """
    if abs(dados[0] - dados[1]) <= valor:
        return True
    else:
        return False
    
def simular(tempo, qtd, valor):
    """
    Tempo: Intervalo total de tempo (60Min)
    Valor: Valor da diferença dos tempos.
    Qtd: quantidade de experimentos

    retorna a % de vezes que o evento ocorreu na simulação.
    """
    encontros = 0
    for i in range(qtd):
        dados = gerar_dados(tempo)
        if testar_dados(dados, valor):
            encontros += 1

    return (encontros / qtd) * 100

def simular_completa(tempo, valor, qtd_experim, qtd_simula):
    """
    Vai tirar a Média de n simulações simples
    assim simulando o resultado real.
    """
    soma = 0
    for k in range(qtd_simula):
        soma += simular(tempo, qtd_experim, valor)
    return (soma / qtd_simula)

print(simular_completa(60, 15, 150, 4000))
# Resultado final: A chance de se encontrarem é de aproximadamente 43,7%.