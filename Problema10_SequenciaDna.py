import random
# Resolução do Problema 10 da Ficha de Exercícios de Monte Carlo
def gerar_dna(qdt_pares):
    """
    Responsável por gerar a sequencia de pares do DNA.
    """
    pares = ([('A', 'T')] * qdt_pares) + ([('C', 'G')] * qdt_pares)
    random.shuffle(pares)

    pares_sorteados = []
    for p in pares:
        if random.random() < 0.5:
            pares_sorteados.append(p)
        else:
            pares_sorteados.append(p[::-1])

    return pares_sorteados

def testar_sequencia_dna(pares):
    """
    Responsavel por verificar se a Sequencia alvo está em alguma das Fitas
    A fita02 ta invertida devido ao sentido 5'3' do Dna
    a fita01 n precisa disso pq ela ja vem no sentido 5'3'
    """
    fita01 = ''.join(par[0] for par in pares)
    fita02 = ''.join(par[1] for par in pares)[::-1]
    sequencia = "GATTACA"

    return sequencia in fita01 or sequencia in fita02

def executar_experimento(qtd_exp, qtd_pares):
    """
    Responsavel por fazer n experimentos e tirar a media de encontros
    """
    encontros = 0
    for _ in range(qtd_exp):
        pares_dna = gerar_dna(qtd_pares)
        if testar_sequencia_dna(pares_dna):
            encontros += 1

    return encontros / qtd_exp

def executar_simulacao(qtd_simu, qtd_exp, qtd_pares):
    soma = 0
    for _ in range(qtd_simu):
        soma += executar_experimento(qtd_exp, qtd_pares)
    return (soma / qtd_simu) * 100

QTD_PARES_DNA = 10
qtd_simulacoes = 200
qtd_experimentos = 1000

resultado = executar_simulacao(qtd_simulacoes, qtd_experimentos, QTD_PARES_DNA)
print(f'A Probabilidade de Achar a Sequência "GATTACA" em uma sequencia de Dna é de {resultado:.4f} %')