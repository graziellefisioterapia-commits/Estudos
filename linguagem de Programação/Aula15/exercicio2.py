import pandas as pd

#Qual o produto mais caro e o mais barato?

dados_df = pd.read_excel("produtos_ficticios.xlsx")
print(dados_df.to_string())

maisbarato = dados_df.loc[dados_df['Preço'].idxmin()]
print(maisbarato)
