Baseado no Modelo de Markowitz para alocação de investimentos, este modelo considera os retornos de ações no intervalo de tempo 2023 - 2024.


Ele encontra entre as ações escolhidas o a melhor distribuição entre elas, ou seja, 50/50 ou 30/70. Vale ressaltar que podem ser escolhidas quantas ações quiserem, porém não é recomendado mais do que 20 no máximo.

o programa recebe apenas nome de empresas listadas na bolsa, por favor nao coloquem outros(nao tive tempo de arrumar isso)

Algumas ressalvas :

A interação com o gemini gera uma lista das ações escolhidas. mas estou com problema de timeout/localhost que não sei arrumar. Não consigo verificar qual o formato da resposta(response.text)
se ela for uma string tera problema em rodar o arquivo, pois atribuo essa response ao que era para ser um vetor.


caso o código não rode devido aos bugs, deixo algumas sugestôes :
(tickers)

lista1 = ['VALE3.SA', 'PETR4.SA']
lista2 = ['ITUB4.SA', 'BBDC4.SA', 'BBAS3.SA']
lista3 = ['WEGE3.SA', 'HAPV3.SA', 'FLRY3.SA', 'LREN3.SA']
lista4 = ['B3SA3.SA', 'CIEL3.SA', 'GGBR4.SA']
lista5 = ['NTCO3.SA', 'QUAL3.SA', 'RADL3.SA', 'MRVE3.SA', 'PRIO3.SA']
lista6 = ['VIVT3.SA', 'TIMS3.SA', 'TOTS3.SA']
lista7 = ['CSNA3.SA', 'USIM5.SA', 'GOAU4.SA', 'CMIG4.SA']
lista8 = ['SUZB3.SA', 'BEEF3.SA', 'JBSS3.SA']
lista9 = ['BRFS3.SA', 'MGLU3.SA']
lista10 = ['EQTL3.SA', 'EGIE3.SA', 'ENBR3.SA', 'ELET3.SA', 'TRPL4.SA']

Pode misturar as listas, mas não repita ações. (sem tempo kkkkkkkk)








