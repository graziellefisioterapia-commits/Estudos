import pandas as pd

dados_df = pd.read_excel("produtos_ficticios.xlsx")
#print(dados_df.to_string()) mostra a tabela
#print(dados_df.columns) mostra as colunas
#print(dados_df.shape) quantidade de colunas e linhas
#produto = dados_df[['Categoria','Preço']] mostra cada coluna individualmente
#print(produto)

#roupas = dados_df.loc[dados_df['Categoria'] == "Roupas", ['Categoria','Código do produto', 'Preço']]
#print(roupas)

#roupas = dados_df.loc[dados_df['Cor'] == "Preto",['Cor','Nome do produto','Preço']]
#print(roupas)

#produto_cor_df = dados_df.loc[(dados_df['Categoria'] == "Roupas") & (dados_df['Cor'] == "Preto"),
                             # ['Categoria','Código do produto','Preço','Cor']]
#print(produto_cor_df)
            
print(dados_df.loc[5, 'Código do produto'])