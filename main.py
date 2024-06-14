import numpy as np # Manipular os Arrays
import matplotlib.pyplot as plt # Visualizar os dados
import pandas as pd
from sklearn.linear_model import LinearRegression # Para criar modelo de Regressão Linear
from sklearn.metrics import mean_squared_error, r2_score # Avaliar o modelo

# Carregar os dados do arquivo Excel
tabela = pd.read_excel('C:/Users/vinic/OneDrive/Área de Trabalho/Python/Loto_v8.xlsx', engine='openpyxl')

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
    'Data Sorteio'
]

# Excluir as colunas da lista
tabela = tabela.drop(columns=colunas_para_excluir)

# Considerar apenas os 100 últimos dados
tabela = tabela.tail(5)

# Preparar os dados
x = tabela.drop(columns=['Concurso'])  # Remover a coluna 'Concurso'
y = tabela[['Bola1', 'Bola2', 'Bola3', 'Bola4', 'Bola5', 'Bola6', 'Bola7', 'Bola8', 'Bola9', 'Bola10', 'Bola11', 'Bola12', 'Bola13', 'Bola14', 'Bola15']]

# Visualizar os dados em um gráfico de dispersão
plt.figure(figsize=(10, 6))
for i in range(1, 16):
    plt.scatter(x.index, y[f'Bola{i}'], label=f'Bola{i}', alpha=0.5)
plt.xlabel('Concurso')
plt.ylabel('Bolas')
plt.title('Lotofacil')
plt.legend()
# plt.show()

# Criar e treinar um modelo de regressão linear para cada bola
models = []
predictions = []

for i in range(15):
    model_linear = LinearRegression()
    model_linear.fit(np.arange(len(x)).reshape(-1, 1), y[f'Bola{i + 1}'])
    models.append(model_linear)

    # Fazer previsão para o próximo número
    x_new = np.array([len(x) + 1])
    y_new = model_linear.predict(x_new.reshape(-1, 1))
    predictions.append(y_new[0])

# Mostrar as previsões para cada bola
for i in range(15):
    print(f'A bola {i+1} = {int(round(predictions[i]))}')

# Avaliar o desempenho dos modelos com algumas métricas (opcional)
y_pred_linear = np.zeros_like(y.values)
for i in range(15):
    y_pred_linear[:, i] = models[i].predict(np.arange(len(x)).reshape(-1, 1))

mse = mean_squared_error(y, y_pred_linear)
r2 = r2_score(y, y_pred_linear, multioutput='variance_weighted')

print(f'MSE: {mse}')
print(f'R2: {r2}')
