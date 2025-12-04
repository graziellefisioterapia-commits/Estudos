#Funções servem para organizar o código, reutilizar e facilitar manutenção.

#Função simples

def saudacao():
    print("Bem Vindo!")

saudacao()
    
#função com parâmetros

def soma(a,b):
    return a + b

resultado = soma(5, 3)
print(resultado)