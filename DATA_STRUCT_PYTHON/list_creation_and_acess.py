# Trabalhando com listas
frutas = ["Laranja","Groselha","Uva"] # Declarando a lista

print(frutas[0]) # Acessando os dados da lista

print(frutas[-1]) # Em Python existe o conceito de indice negativo, onde o cursor percorre a lista de maneira inversa, nesse caso o -1 para no ultimo item da lista (Uva)



#Listas podem conter todo tipo de objeto em python, sendo assim podem conter listas formando estruturas bidimensionais (tabelas)

matriz = [
  ["Pedro",21,1600],
  ["Luizz",41,15760],
  ["Maria",26,6800]
]

#sua forma de acesso pode se diferenciar dependendo da informação que se quer obert
print(matriz[0]) #Puxar toda a primeira lista
print(matriz[0][0]) #Puxar o primeiro elemento da lista


#fatiamento em listas
lista = ["p","y","t","h","o","n"]
print(lista[2:4])
print(lista[:4])
print(lista[1:])


#iterar Listas
#forma mais utilizada de percorrer dados de uma lista, utilizando for

frutas = ["Laranja","Groselha","Uva"] # Declarando a lista

for fruta in frutas:
  print(fruta)

#para saber o indice de um objeto dentro do for, usamos a funcao enumerate

for indice,fruta in enumerate(frutas):
  print(f"{indice}: {fruta}")


# Compreensão de listas
#sintaxe mais curta de listas quando se deseja criar uma lista com base nos valores de uma lista existente(Filtro) ou gerar uma lista aplicando modificacoes numa existente

numeros = [1,12,31,33,45,67,95,80]
pares =[]

for numero in numeros:
  if numero % 2 == 0:
    pares.append(numero)

print(pares)

#Outra forma de ser feito

numeros = [1,12,31,33,45,67,95,80]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

#Modificando e criando nova lista
# vamos pegar a lista de numeros e usa-la para compor uma nova lista

quadrado = []
for numero in numeros:
  quadrado.append(numero ** 2)

print(quadrado)