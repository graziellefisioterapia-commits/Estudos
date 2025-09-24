#read (r) - leitura
#write (W)- subscreve
#append


with open("dados.txt","w")as arquivo:
    arquivo.write("Grazielle")

with open("dados.txt","r")as arquivo:
    conteudo=arquivo.read()
    print(conteudo)

with open("dados.txt","a")as arquivo:
    arquivo.write(" Moreira")

