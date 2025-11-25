"""
Vamos praticar Pandas usando o dataset Titanic.csv.
Este trabalho vale 15 pontos.

Lembre-se: o semestre está acabando e a prova está chegando.
Aprenda!!
"""

#--------------------------------------------------
# 1. Importação da biblioteca e carregamento
#--------------------------------------------------
import pandas as pd

titanic_df = pd.read_csv("Titanic.csv")

#importe aqui a planilha

#print(titanic_df.head())

#--------------------------------------------------
# 2. Explorando o dataset
#--------------------------------------------------
#print(titanic_df.info())
#print(titanic_df.describe())

#--------------------------------------------------
# 3. Exercícios (RESPONDA USANDO CÓDIGO EM PYTHON)
#------------------------------------------------


# 1) Quantas linhas e colunas o dataset possui?
#    Dica: use df.shape

#print(titanic_df.shape)

# 2) Qual é a idade média dos passageiros?
#    Dica: mean()

#idade_media = titanic_df["Age"].mean()
#print("Idade média dos passageiros:", idade_media)

# 3) Trazer apenas as colunas 'Name' e 'Age'

#print(titanic_df[['Name', 'Age']])


# 4) Trazer apenas os passageiros do sexo feminino

#mulheres = titanic_df[titanic_df["Sex"] == "female"]
#print(mulheres)


# 5) Trazer apenas passageiros do sexo masculino com idade > 30

#homens_m30 = titanic_df[(titanic_df["Sex"] == "male") & (titanic_df["Age"] > 30)]
#print(homens_m30)


# 6) Mostrar apenas mulheres sobreviventes

#mulheres_s = titanic_df[(titanic_df["Sex"] == "female") & (titanic_df["Survived"] == 1)]
#print(mulheres_s)

# 7) Mostrar passageiros da 1ª classe com menos de 18 anos

#primeira_c_m = titanic_df[(titanic_df["Pclass"] == 1) & (titanic_df["Age"] < 18)]
#print(primeira_c_m)


# 8) Criar uma coluna chamada 'Faixa' com:
#       - CRIANCA para idade < 18
#       - ADULTO para idade >= 18

#titanic_df['Faixa'] = 'N/A'
#titanic_df.loc[titanic_df['Age'] < 18, 'Faixa'] = 'Criança'
#titanic_df.loc[titanic_df['Age'] >= 18, 'Faixa'] = 'Adulto'


# 9) Agrupar e mostrar taxa de sobrevivência por sexo



#taxa_por_sexo = df.groupby("Sex")["Survived"].mean()

#print(taxa_por_sexo)

#taxa_sobrevivencia_sexo = titanic_df.groupby("Sex")["Survived"].mean()

#print(taxa_sobrevivencia_sexo)


# 10) Mostrar a tarifa média por classe

#tarifa_media_por_classe = titanic_df.groupby("Pclass")["Fare"].mean()

#print(tarifa_media_por_classe)

# 11) Qual é a idade da pessoa mais velha do Titanic?
#     Dica: df['Age'].max()

#idade_maxima = titanic_df["Age"].max()
#print("Idade máxima:", idade_maxima)

# 12) Qual foi a tarifa mais alta paga no Titanic?
#     Dica: df['Fare'].max()

#tarifa_maxima = titanic_df["Fare"].max()
#print("Tarifa mais alta paga:", tarifa_maxima)

# 13) Qual classe tinha mais passageiros?
#     Dica: use value_counts()

#mais_passageiros = titanic_df["Pclass"].value_counts().idxmax()
#print("A classe com mais passageiros é:", mais_passageiros)
#--------------------------------------------------
# 5. Exportação
#--------------------------------------------------
#titanic_df.to_csv("titanic_exportado.csv", index=False)

# 14) Exportar apenas os sobreviventes para um arquivo CSV
#     Nome sugerido: sobreviventes.csv

#titanic_df.to_csv("sobreviventes.csv", index=False)