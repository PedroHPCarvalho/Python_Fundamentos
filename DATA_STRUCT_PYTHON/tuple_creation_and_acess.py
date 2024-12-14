# a maior diferença entre tuplas e listas é que tuplas são imutaveis

# declarando tuplas

frutas = ("laranja","pera","uva",)

letras = tuple("Python")

country = ("Brasil",)

print(frutas)
print(letras)
print(country)
print()

#acesso direto
frutas = ("laranja","pera","uva",)
print(frutas[0])
print(frutas[-1])
print()

#Tuplas aninhadas
matriz_tupla = (
  ("Bomdia",1,2,),
  ("HelloWold",2,3,),
  ("Bye",6,5,),
)

print(matriz_tupla[1])
print(matriz_tupla[1][1])
print()

#Fatiamento
tupla_fatiamento = ("p","y","t","h","o","n",)
print(tupla_fatiamento[2:3])
print(tupla_fatiamento[:3])
print(tupla_fatiamento[2:])
print(tupla_fatiamento[0:2:3])
print()

#iterar sobre tuplas com for
tupla_iterar = ["a","b","c","d",]
for letra in tupla_iterar:
  print(letra)

print()
#tupla e enumerate

tupla_enumerate = ["a","b","c","d",]

for indice, letra in enumerate(tupla_enumerate):
  print(f"{indice}: {letra}")