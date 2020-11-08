import math
import numpy
import statistics
from scipy import stats
from collections import Counter # conta a ocorrência de valores em uma lista


def media(lista):
    return statistics.mean(lista)

def mediana(lista):
    return statistics.median(lista)

def moda(lista):
    # essa função não leva em consideração casos onde a moda é bimodal etc
    return statistics.mode(lista)

def variancia(lista):
    return statistics.variance(lista)

def desvio_padrao(lista):
    return statistics.stdev(lista)

def coeficiente_variacao(lista):
    return desvio_padrao(lista)/media(lista)

def relatorio_analise_exploratoria(lista, titulo):
    print(titulo.upper())
    print("Valor mínimo: ", min(lista))
    print("Valor máximo: ", max(lista))
    print("Média aritmética: ", media(lista))
    # print("Moda: ", moda(lista))
    print("Mediana: ", mediana(lista))
    print("Variância: ", variancia(lista))
    print("Desvio padrão: ", desvio_padrao(lista))
    print("Coeficiente de variação: ", coeficiente_variacao(lista))

def gerar_tabela(n, titulo, matriz_linhas, intervalos):
    print(f"{titulo}\t\tFreq. Absoluta\t\tFreq. relativa")
    print("-----------------------------------------------------------------")
    for (linha, intervalo) in zip(matriz_linhas, intervalos):
        freq_absoluta = len(linha)
        freq_relativa = freq_absoluta/n
        # texto do intervalo formatado
        str_intervalo = f"{intervalo[0]} -> {intervalo[1]}"

        print(f"{str_intervalo}\t\t{freq_absoluta}\t\t{freq_relativa}")

def distribuicao_de_frequencia(lista, titulo):
    n = len(lista)
    # achar o K pela regra de Sturges
    k = math.floor(1 + 3.3 * math.log(n))
    # achar a amplitude
    h = math.ceil((max(lista) - min(lista))/k)

    print("k = ", k)
    print("h = ", h)

    matriz_linhas = []
    intervalos = []
    for i in range(k):
        matriz_linhas.append([])
        # populando as tuplas de intervalos
        intervalos.append(())
        if i == 0:
            intervalos[i] = (min(lista), min(lista)+h)
        else:
            teto_ultimo_intervalo = intervalos[i-1][1]
            intervalos[i] = (teto_ultimo_intervalo, teto_ultimo_intervalo+h)

    # separando os valores em seus intervalos
    for valor in lista:
        indice = 0
        for intervalo in intervalos:
            if valor >= intervalo[0] and valor <= intervalo[1]:
                matriz_linhas[indice].append(valor)
            indice+=1

    gerar_tabela(n, titulo, matriz_linhas, intervalos)
