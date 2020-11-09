import xlrd
from analise_exploratoria import relatorio_analise_exploratoria, distribuicao_de_frequencia
from mmq import mmq

def pegar_valores_da_coluna(planilha, numero_coluna):
    return planilha.col_values(numero_coluna)[1:]


def abrir_planilha():
    book = xlrd.open_workbook("../PD.xlsx")
    return book.sheet_by_index(0)


planilha = abrir_planilha()

# lendo e salvando os valores de cada coluna da planilha
metros_vendidos = pegar_valores_da_coluna(planilha, 0)
gastos_promocao = pegar_valores_da_coluna(planilha, 1)
num_clientes = pegar_valores_da_coluna(planilha, 2)
num_concorrentes = pegar_valores_da_coluna(planilha, 3)
potencial = pegar_valores_da_coluna(planilha, 4)



relatorio_analise_exploratoria(metros_vendidos, "Metros Vendidos")
distribuicao_de_frequencia(metros_vendidos, "Metros Vendidos")
print('------------------------')
relatorio_analise_exploratoria(gastos_promocao, "Gastos Promoção")
distribuicao_de_frequencia(gastos_promocao, "Gastos Promoção")
print('------------------------')
relatorio_analise_exploratoria(num_clientes, "Número de Clientes")
distribuicao_de_frequencia(num_clientes, "Número de Clientes")
print('------------------------')
relatorio_analise_exploratoria(num_concorrentes, "Número de Concorrentes")
distribuicao_de_frequencia(num_concorrentes, "Número de Concorrentes")
print('------------------------')
relatorio_analise_exploratoria(potencial, "Potencial")
distribuicao_de_frequencia(potencial, "Potencial")

#imprimindo arquivo das retas
mmq(gastos_promocao, metros_vendidos, "Gastos_Promocao")
mmq(potencial, metros_vendidos, "Potencial")
mmq(num_clientes, metros_vendidos, "N_Clientes")
mmq(num_concorrentes, metros_vendidos, "N_Concorrentes")
