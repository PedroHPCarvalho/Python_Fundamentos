#conjunto não-ordenado de pares chave:valor
pessoa = {"nome": "Pedro ","idade": 21}
#acesso aos dados e modificações são feitas atraves da chave
print(pessoa["nome"])

#modificacao
pessoa["nome"] = "Ana"
print(pessoa["nome"])
print()

#Dicionario aninhados - podem armazenar qualquer tipo de objeto, desde que a chave para esse valor seja um objeto imutavel como (string e numeros)
dict_aninhado = {"Pedro" : {"idade": 21, "namorada": "Ana"}}

#iterar dicionarios
for dict_ in dict_aninhado:
  print(dict_, dict_aninhado[dict_])

for dict_, valor in dict_aninhado.items():
  print(dict_,valor)