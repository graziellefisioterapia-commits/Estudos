import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx")
print(dados_df.to_string())

#Liste os produtos fabricados na china acima de 50 unidades


china = dados_df.loc[(dados_df['País de origem'] == 'China') & (dados_df['Quantidade em estoque'] > 50), ['Nome do produto', 'País de origem', 'Quantidade em estoque']]
print(china)
