import pandas as pd

df = pd.read_csv('jogos.csv')
# Exercício 1 – Primeiro contato
'''
linhas, colunas = df.shape
print("Existem", linhas, "jogos no dataset")
'''
'''
print(df.info())
'''
'''
print(df[['preco', 'nota']].mean())
'''
'''
print(df[['jogo', 'preco']].head(3))
'''
# Exercício 2 – Exploração guiada

df['genero'].value_counts()           # Minha previsão: Mostra todos gêneros existentes
df['nota'].max()                       # Minha previsão: A maior nota dentre todas
df['preco'].min()                      # Minha previsão: A menor nota dentre todas
df.loc[5, 'jogo']                      # Minha previsão: Mostra a quinta linha da coluna jogo 
df.iloc[0:3, 1:3]                      # Minha previsão: Mostra da linha 0 a 3 e a coluna 1 a 3
df[['jogo', 'ano']].tail(3)            # Minha previsão: Mostra as 3 últimas linhas da coluna jogo e ano
df.describe().loc['mean']              # Minha previsão: Mostra um resumo estatístico do dataframe e apenas a linha da media desse resumo



