import operacoes


print("Qual será a conversão?")
print("1 - metros para centímetros")
print("2 - centímetros para metros")
print("3 - kilometros para metros")



opcao= int (input ("Escolha a operação:"))
a=float(input("digite um número:"))



if opcao == 1 :
    
    print("resultado:",operacoes.m_para_cm(a))

elif opcao == 2 :
    print("resultado:",operacoes.cm_para_m(a))

elif opcao == 3 :
    print("resultado:",operacoes.km_para_m(a))

else:
    print("opção inválida")




  