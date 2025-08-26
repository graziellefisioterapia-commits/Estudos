pessoa = {
    "nome" : "Grazielle",
    "idade": "35",
    "peso": "71 kg"
} # para criar um dicionário

print (pessoa)
print(pessoa ["peso"]) #mostra apenas o atributo desejado
print(pessoa.keys()) # mostra apenas as chaves
print(pessoa.values()) # mostra os valores

pessoa ["altura"] = 1.62 #acrescenta altura (mas é utilizada tanto para acrescentar quanto para alterar)

print(pessoa)

pessoa ["peso"] = 71
print (pessoa)

del pessoa ["idade"] #del (usado para delletar um dado)
print (pessoa)
print ("idade" in pessoa)
print ("nome" in pessoa)