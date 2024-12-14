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



