import random
# Resolução do Problema 06 da Ficha de Exercícios de Monte Carlo
def pacote_figurinhas(qtd_por_pacote, tam_album):
    """
    Função que gera as Figurinhas de um pacotinho de acordo com a qtd no pacote
    & no tam do album.
    """
    return [random.randint(1, tam_album) for _ in range(qtd_por_pacote)]

def colar_fugurinhas(pacote, album:list):
    """
    Responsável pela colagem das fig, se a fig for repetida ele simplismente ignora.
    o uso do set acabou sendo conveniente pela sua complexidade de remoção.
    """
    for figurinha in pacote:
        album.discard(figurinha)

def executar_experimento(qtd_exp, tam_album, fig_por_pacote):
    """
    Aqui ele vai preencher "N" (albums) completos de acordo com a qtd de experimentos
    e tirar uma media de todos os pacotes que foram abertos para preencher "N".
    """
    total_pacotes_abertos = 0
    for _ in range(qtd_exp):
        album = set(range(1, tam_album + 1))
        pacotes_abertos = 0

        while len(album) > 0:
            pacote = pacote_figurinhas(fig_por_pacote, tam_album)
            pacotes_abertos += 1
            colar_fugurinhas(pacote, album)

        total_pacotes_abertos += pacotes_abertos

    return total_pacotes_abertos / qtd_exp

def executar_simulacao(qtd_simu, qtd_exp, fig_por_pacote, tam_alum):
    """
    Para Obter uma Média mais proxima da realidade, executa-se X (qtd_simulações) com Y 
    experimentos em cada.
    """
    medias = 0
    for _ in range(qtd_simu):
        medias += executar_experimento(qtd_exp, tam_alum, fig_por_pacote)
    return (medias // qtd_simu) + 1


QTD_EXP = 150
QTD_SIMU = 20

# Simulando o Album da Ficha de Gama
TAM_ALBUM_QUESTAO = 500
FIGU_POR_PACOTE_QUESTAO = 5

media_pacotes_questao = executar_simulacao(QTD_SIMU, QTD_EXP, FIGU_POR_PACOTE_QUESTAO, TAM_ALBUM_QUESTAO)
custo_real = media_pacotes_questao * 7
print(f"==========COPA GAMA==========")
print(f"Para Concluir o Albúm de {TAM_ALBUM_QUESTAO} figurinhas (FICHA)\nÉ necessário aproximadamente {media_pacotes_questao} pacotes de figurinha\nCustando {custo_real} R$.\n")

# Simulando o Album de 2026 
TAM_ALBUM_2026 = 980
FIGU_POR_PACOTE_2026 = 7

media_pacotes_2026 = executar_simulacao(QTD_SIMU, QTD_EXP, FIGU_POR_PACOTE_2026, TAM_ALBUM_2026)
custo_real = media_pacotes_2026 * 7
print(f"==========COPA 2026==========")
print(f"Para Concluir o Albúm de {TAM_ALBUM_2026} figurinhas (2026)\nÉ necessário aproximadamente {media_pacotes_2026} pacotes de figurinha\nCustando {custo_real} R$.")
