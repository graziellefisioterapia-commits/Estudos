import pandas as pd

#Mostre o nome e preços dos produtos com valor acima de R$300,00

dados_df = pd.read_excel("produtos_ficticios.xlsx")
print(dados_df.to_string())

caros = dados_df[dados_df['Preço'] > 300][['Nome do produto','Preço']]
print (caros)

                      

