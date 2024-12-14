#------------------------------------------------------------------

# Laço For/Else
text = input("Informe um Texto: ")
VOGAIS = "AEIOU"

for letra in text: # Este é um laço for que percorre cada caractere da string armazenada na variável text.
  if letra.upper() in VOGAIS: # converte a letra lida pelo for em maiuscula e verifica se esta entre as vogais
    print(letra, end="") # imprime a letra que passou pelo if, end="" faz com que a saida da impressao seja na mesma linha
else: 
  print("NÃO TEM VOGAIS")


#------------------------------------------------------------------

# Função Range
# função built-in do python, usada para produzir uma sequencia de numeros inteiros a partir de um inicio para um final

# for numero in range(0,11):
#   print(numero, end=" ")

# print()

# for numero in range(0,51,5):
#   print(numero, end=" ")

#--------------------------------------------------------------------

# While/else
# usado para repetir um bloco de código muitas vezes
# usamos quando nao sabemos a quantidade exata de vezes que o codigo sera executado

init = 1

while init < 10:
  print (init)
  init += 1  