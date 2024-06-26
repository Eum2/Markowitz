Original file is located at
    https://colab.research.google.com/drive/1QecjCNNvjnuCW3fUlv_Dqqeq4ruprqx3
"""

!pip install -q -U google-generativeai

import google.generativeai as genai
from google.colab import userdata

GOOGLE_API_KEY="AIzaSyCyEDxQ_ExRw_-Hsra5bWvHcdoss4QHy28"
genai.configure(api_key=GOOGLE_API_KEY)

generation_config = {
    "candidate_count" : 1,
    "temperature" : 1,
    #"top_p" :1,
    #"top_k": 1,

}

#safety_settings = {
    #'harassment' : 'WARN',
   # 'hate' : 'WARN',
    #'sexual': 'WARN',
    #'dangerous' : 'WARN',

#}

model = genai.GenerativeModel(model_name ='gemini-1.0-pro',
                              generation_config = generation_config,
                              )

chat = model.start_chat()
print("Diga quais ações voce gostria de ter na sua carteira de investimento")
ações  = input("")

response = chat.send_message("retorne apenas uma lista no formato do python com yfinance que contenha as ações. Não retorno nada alem do pedido : "+ações)
print(response.text, "\n")

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definindo os tickers dos ativos
tickers = response.text

# Definindo o período de análise
inicio = "2022-12-12"
fim = "2024-01-01"

# Baixando os dados históricos dos ativos
dados = yf.download(tickers, start=inicio, end=fim)["Adj Close"]

# Visualizando os dados (opcional)
print(dados.head())

# Calculando os retornos diários logarítmicos
retornos = np.log(dados / dados.shift(1))

# Visualizando os retornos (opcional)
print(retornos.head())

# Calculando a matriz de covariância dos retornos
cov_matrix = retornos.cov()

# Visualizando a matriz de covariância (opcional)
print(cov_matrix)

# Número de carteiras a serem simuladas
num_portfolios = 10000

# Arrays para armazenar os resultados
resultados = np.zeros((4+len(tickers), num_portfolios))
# Retorno livre de risco
risk_free_rate = 0.09

for i in range(num_portfolios):
    # Gerando pesos aleatórios para os ativos, garantindo que somem 1
    pesos = np.random.random(len(tickers))
    pesos /= np.sum(pesos)

    # Calculando o retorno da carteira
    retorno_carteira = np.sum(retornos.mean() * pesos) * 252
    # 252 = número aproximado de dias de negociação em um ano



    # Calculando o risco (desvio padrão) da carteira
    risco_carteira = np.sqrt(np.dot(pesos.T, np.dot(cov_matrix, pesos))) * np.sqrt(252)

    # Calculando o Sharpe Ratio
    sharpe_ratio = (retorno_carteira - risk_free_rate) / risco_carteira

    # Armazenando os resultados
    resultados[0,i] = risco_carteira
    resultados[1,i] = retorno_carteira
    resultados[2:2+len(tickers),i] = pesos
    resultados[3 + len(tickers), i] = sharpe_ratio # Armazenando o sharpe ratio


# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.scatter(resultados[0,:],resultados[1,:],c=resultados[3 + len(tickers),:], cmap='viridis')
plt.colorbar(label="Sharpe Ratio")
plt.xlabel('Risco (Desvio Padrão)')
plt.ylabel('Retorno Esperado')
plt.title('Simulação de Carteiras e Fronteira Eficiente')

# Destacando as carteiras otimizadas
sharpe_optimal_index = np.argmax(resultados[3 + len(tickers),:])
plt.scatter(resultados[0,sharpe_optimal_index], resultados[1,sharpe_optimal_index], c='red', marker='*', s=200, label='Carteira com Maior Sharpe Ratio')

min_vol_index = np.argmin(resultados[0,:])
plt.scatter(resultados[0,min_vol_index], resultados[1,min_vol_index], c='blue', marker='o', s=100, label='Carteira de Menor Volatilidade')

plt.legend()
plt.show()

# Exibindo os resultados das carteiras otimizadas
print("\n----- Carteira com Maior Sharpe Ratio -----")
print("Retorno:", resultados[1,sharpe_optimal_index])
print("Risco:", resultados[0,sharpe_optimal_index])
print("Sharpe Ratio:", resultados[3 + len(tickers),sharpe_optimal_index])
print("Pesos:", response.text, resultados[2:2+len(tickers),sharpe_optimal_index])

print("\n----- Carteira de Menor Volatilidade -----")
print("Retorno:", resultados[1,min_vol_index])
print("Risco:", resultados[0,min_vol_index])
print("Sharpe Ratio:", resultados[3 + len(tickers),min_vol_index])
print("Pesos:", response.text ,resultados[2:2+len(tickers),min_vol_index])

response1 = chat.send_message("explique oque é : indice sharpe,risco e retorno.")
print(response.text, "\n")
