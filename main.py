# Importando bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Gerando dados de exemplo
np.random.seed(0)
area = 2.5 * np.random.randn(100) + 25
preco = 100 + 10 * area + np.random.randn(100) * 10

# Dividindo os dados em conjuntos de treinamento e teste
area_treino, area_teste, preco_treino, preco_teste = train_test_split(area, preco, test_size=0.2, random_state=0)

# Criando e treinando o modelo de regressão linear
modelo = LinearRegression()
modelo.fit(area_treino.reshape(-1, 1), preco_treino)

# Fazendo previsões
previsoes = modelo.predict(area_teste.reshape(-1, 1))

# Avaliando o modelo
mse = mean_squared_error(preco_teste, previsoes)
print(f'Erro quadrático médio: {mse:.2f}')

# Visualizando os resultados
plt.scatter(area_teste, preco_teste, color='blue', label='Dados reais')
plt.plot(area_teste, previsoes, color='red', linewidth=2, label='Previsões')
plt.xlabel('Área (m²)')
plt.ylabel('Preço (milhares de dólares)')
plt.legend()
plt.show()
