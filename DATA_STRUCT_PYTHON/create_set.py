#criando um conjunto (set)
#set é uma coleção de onjetos que não possui objetos repetidos, ele elimina itens duplicados de um iteralvel

set([1,2,3,4,5,6,7])
set("abacaxi")

#Acessando dados
#conjuntos em python não suportam indexação e nem fatiamento, para isso é necessario transformar o conjunto em lista
numeros = {1,2,3,4,4,2}
numeros = list(numeros)
print(numeros[0])

#Iterar conjuntos utilizando for
set_iterar = {1,2,3,4,5,6,7,5}

for numero in set_iterar:
  print(numero)
print()
#Enumerate em conjuntos(set)
set_iterar = {1,2,3,4,5,6,7,5}

for indice, numero in enumerate(set_iterar):
  print(f"{indice}: {numero}")