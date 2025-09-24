try:
    a= int(input("digite um número inteiro:"))

except ValueError:

    print("você digitou um valor inválido")

else:

    print("número válido")

finally:

    print("seu programa foi executado")