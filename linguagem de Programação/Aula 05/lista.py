numero = [2,5,10,1,4,9,22,100,3]
print (len(numero)) #"len" descreve o tamanho da lista
print (min(numero)) #"min" menor valor da lista
print (max(numero)) #"max" maior valor da lista
print (sum(numero)) #"sun" soma de todos os elementos da lista
print (sorted(numero)) #"sorted" organiza do menor para o maior (crescente)
print (sorted(numero,reverse = True)) # "sorted(numero,reverse = True" forma de organizar em ordem decrescente
print (numero[1]) #"para mostrar o numero que está nesta posição" 
print (100 in numero) #testa se esse numero esta na lista , como verdadeiro ou falso 
print (30 in numero)
print (numero)
print (numero[2:8]) #serve para fazer um fatiamento da lista, inicio e fim. (começa no segundo da lista e termina no 7°)
print (numero[:2]) #nesse caso o fatiamento começa na posição 0 e vai até a segunda
print (numero[2:]) # nesse caso o fatiamento começa na segunda posição e vai até onde termina a lista
del numero [1] # deleta o indice (numero) da posição que vc quer deletar
print (numero)
numero.append (101)
print(numero) #adiciona elemento no final da lista

