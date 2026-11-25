import random
# Atividade de Renato Rodrigues Barbosa Filho
# Resolução do Problema 02 da Ficha de Exercícios de Monte Carlo
def gerar_cordenada():
    """
    Função responsável pela geração das cordenadas do problema (Dados da simulação)!
    No peroblema 2 o lado do quadrado é 2, então as cordenadas possíveis giram em torno do range (-1 -> 1)
    isso considerando o centro no plano (0,0)
    """
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    return (x, y)

def testar_cordenada(cordenada):
    """
    Para determinar se a cordenada está contida dentro da Área do Circulo,
    usei a Equação da circuferencia: x² +  y² = r²
    se a igualdade for maior que r então o ponto está fora da circ.
    se for igual está na borda da circ.
    se for menor está dentro, para isso usei os 02 casos que favorecem (<=);
    """
    return (cordenada[0] ** 2) + (cordenada[1] ** 2) <= 1

def executar_experimentos(qtd_experimentos):
    """
    Ao aproximar a proporção de pontos contidos no circulo com a proporção das áreas
    isolando o pi, vai ficar +- assim: cordCirculo / cordQuadrado = pi / 4
    resultando em 4 * proporcao_circulo.
    Aqui eu executo n experimentos 
    """
    coord_contidas = 0
    for _ in range(qtd_experimentos):
        cordenada = gerar_cordenada()
        if testar_cordenada(cordenada):
            coord_contidas += 1
            
    proporcao_circulo = coord_contidas / qtd_experimentos
    return 4 * proporcao_circulo

def executar_simulacoes(qtd_sim, qtd_exp):
    """
    Aqui é a parte na qual realizo k simulacoes de n experimentos
    """
    soma = 0
    for _ in range(qtd_sim):
        soma += executar_experimentos(qtd_exp)

    return soma / qtd_sim

quantidade_simulacoes = 250
quantidade_experimentos = 6000
print(executar_simulacoes(quantidade_simulacoes, quantidade_experimentos))
