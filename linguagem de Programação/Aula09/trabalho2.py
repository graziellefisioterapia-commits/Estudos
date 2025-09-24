n=input("Digite seu nome: ")
i=input("Digite sua idade: ")


with open("aula9.txt","w")as arquivo:
    arquivo.write("n")

with open("aula9.txt","r")as arquivo:
    conteudo=arquivo.read()
    print(conteudo)

with open("aula9.txt","a")as arquivo:
    arquivo.write("")
