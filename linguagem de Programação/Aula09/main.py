try:
    a= int(input("numerador:"))
    b= int(input("denominador:"))

    d= a/b

except ZeroDivisionError:

    print("Não é possível dividir por zero")

except ValueError:

    print("você digitou um valor inválido")

else:

    print(f"o resultado é:{d}")

finally:

    print("seu programafoi executado")