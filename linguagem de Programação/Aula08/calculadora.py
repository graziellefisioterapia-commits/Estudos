import operacoes

print("==Calculadora==")
print("1 - somar")
print("1 - subtrair")
print("1 - multiplicar")
print("1 - dividir")

opcao= int (input ("Escolha a operação:"))
a=float(input("digite o primeiro número:"))
b=float(input("digite o segundo numero:"))


if opcao == 1 :
    print("resultado:",operacoes.soma(a,b))

elif opcao == 2 :
    print("resultado:",operacoes.sub(a,b))

elif opcao == 3 :
    print("resultado:",operacoes.mult(a,b))

elif opcao == 4 :
    print("resultado:",operacoes.div(a,b))    
