#definindo funções

def exibir_mensagem():
  print("Bom dia")

def exibir_mensagem2(nome):
  print(f"Bom dia {nome}")

def exibir_mensagem3(nome="Anonimo"):
  print(f"Bom dia {nome}")

exibir_mensagem()
exibir_mensagem2("Pedro")
exibir_mensagem3()
exibir_mensagem3("Ana")

#retornando a função, apenas um retorno
def calcular_total(numeros):
  return sum(numeros)
print(calcular_total([10,32,31]))
print()

#dois retorno
def retorna_antecessor_sucessor(numero):
  antecessor = numero -1
  sucessor = numero +1

  return antecessor, sucessor
print(retorna_antecessor_sucessor(12))
print()

#Argumentos nomeados
def salvar_dados_carro(marca,modelo,ano,placa):
  print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_dados_carro("Fiat","Marea",1999,"ESA-1254")
print()