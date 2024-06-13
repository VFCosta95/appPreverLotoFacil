import pandas as pd
import matplotlib.pyplot as plt
import sklearn as skl
import numpy as np

# Projeto Machine Learning - Aprendizado de Máquina
"""
# Carregar todas as abas do arquivo Excel
tabela = pd.ExcelFile('C:/Users/vinic/OneDrive/Área de Trabalho/Python/Lotofacil.xlsx')
sheets = tabela.sheet_names


# Criar uma lista vazia para armazenar os DataFrames
dfs = []

# Loop através de cada aba e carregar em um DataFrame
for sheet in sheets:
    df = pd.read_excel(tabela, sheet_name=sheet)
    dfs.append(df)

# Concatenar todos os DataFrames
result = pd.concat(dfs, ignore_index=True)

# Excluir colunas específicas
colunas_para_excluir = [
    'Acumulado sorteio especial Lotofácil da Independência',
    'Estimativa Prêmio',
    'Arrecadacao Total',
    'Acumulado 15 acertos',
    'Rateio 11 acertos',
    'Ganhadores 11 acertos',
    'Rateio 12 acertos',
    'Ganhadores 12 acertos',
    'Rateio 13 acertos',
    'Ganhadores 13 acertos',
    'Rateio 14 acertos',
    'Ganhadores 14 acertos',
    'Rateio 15 acertos',
    'Cidade / UF',
    'Ganhadores 15 acertos',
    'Observação',
    'Data Sorteio']  # Substitua pelos nomes das colunas que você deseja excluir

result = result.drop(columns=colunas_para_excluir)

# Criar uma lista de resultados
resultados = []

# Iterar sobre cada linha do DataFrame
for index, row in result.iterrows():
    # Converter a linha em uma lista e adicionar à lista de resultados
    resultado = list(row)
    resultados.append(resultado)

# Exibir o exemplo do resultado 1
print("Resultado", resultados[1])

# Especificar o nome do arquivo de saída com as modificações
nome_arquivo_saida = 'C:/Users/vinic/OneDrive/Área de Trabalho/Python/Lotofacil_modificado.xlsx'

# Salvar o DataFrame modificado em um novo arquivo Excel
result.to_excel(nome_arquivo_saida, index=False)

print("Arquivo salvo com sucesso!")"""

# Carregando os dados da tabela
tabela = pd.read_excel('C:/Users/vinic/OneDrive/Área de Trabalho/Python/Lotofacil_modificado.xlsx')
# print(tabela.head(10)) # Mostrar as 10 primeiras

resultados = []

# Iterar sobre cada linha do DataFrame
for index, row in tabela.iterrows():
    # Converter a linha em uma lista e adicionar à lista de resultados
    resultado = list(row)
    resultados.append(resultado)

# Exibir o exemplo do resultado 1
print("Resultado:", resultados[1])


# Tranformar o nome e o valor da coluna style de red para o n° 0
tabela['Concurso'] = tabela['Concurso'].replace('red', 0)

# Tranformar o nome e o valor da coluna Bola de b para o n° 1
tabela['Bola1'] = tabela['Bola1'].replace('b1', 1)
tabela['Bola2'] = tabela['Bola2'].replace('b2', 1)
tabela['Bola3'] = tabela['Bola3'].replace('b3', 1)
tabela['Bola4'] = tabela['Bola4'].replace('b4', 1)
tabela['Bola5'] = tabela['Bola5'].replace('b5', 1)
tabela['Bola6'] = tabela['Bola6'].replace('b6', 1)
tabela['Bola7'] = tabela['Bola7'].replace('b7', 1)
tabela['Bola8'] = tabela['Bola8'].replace('b8', 1)
tabela['Bola9'] = tabela['Bola9'].replace('b9', 1)
tabela['Bola10'] = tabela['Bola10'].replace('b10', 1)
tabela['Bola11'] = tabela['Bola11'].replace('b11', 1)
tabela['Bola12'] = tabela['Bola12'].replace('b12', 1)
tabela['Bola13'] = tabela['Bola13'].replace('b13', 1)
tabela['Bola14'] = tabela['Bola14'].replace('b14', 1)
tabela['Bola15'] = tabela['Bola15'].replace('b15', 1)

"""
# Separar as Variaveis
y = tabela['Bola1'] # Vai receber o valor da coluna style
x = tabela.drop('Bola1', axis = 1) # Será todas as outras colunas menos a coluna style

# Treinar e testar a maquina para saber o que é vinho red ou white

from sklearn.model_selection import train_test_split
# Exportando função da biblioteca sklearn

# Treinar e testar as variaveis x e y. E testar 30% = test_size=0.3
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3)
#___________________________________________________________________________
x_teste.shape # Testou 1950 Linhas e 12 Colunas
y_teste.shape # Testou 1950 Linhas e 1 Colunas
#___________________________________________________________________________

# Árvore de Classificação
from sklearn.ensemble import ExtraTreesClassifier
# Criando modelo
modelo = ExtraTreesClassifier()
# Treinar o x, y
modelo.fit(x_treino, y_treino)
# Imprimindo o Resultado do Teste
resultado = modelo.score(x_teste, y_teste)
print("Probabilidade: ", resultado) # Probabilidade:  0.9948717948717949
# A probabilidade da correção foi 99.48%
print("__________________________________")
#___________________________________________________________________________

# Fazer a previsão do teste
previsao = modelo.predict(x_teste[500:505])
print(previsao)
"""