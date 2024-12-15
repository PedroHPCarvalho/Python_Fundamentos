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
salvar_dados_carro(marca="Ford",modelo="Focus",ano=2000,placa="SDF-4234")
salvar_dados_carro(**{"marca": "honda","modelo" : "civic","ano": 2004,"placa" : "FGE-2342"})
print()

#Args e Kwargs, combinar parametros obrigatorios com args e kwargs, *agrs recebe tuplas e **kwargs recebe dicionarios

#*args: Representa uma lista de argumentos posicionais adicionais, que são recebidos como uma tupla. Aqui, é usado para os versos do poema ou linhas de texto.

#**kwargs: Representa argumentos nomeados adicionais, recebidos como um dicionário. Esses argumentos podem ser usados para armazenar informações adicionais, 
#como o autor, o título, ou outras características do poema.
def exibir_poema(data_extenso,*args,**kwargs):

#Os elementos em args (linhas do poema) são unidos em uma única string, separados por quebras de linha (\n).
#join no Python é usado para combinar os elementos de uma sequência (como uma lista, tupla ou conjunto) em uma única string, utilizando um delimitador especificado.
  texto = "\n".join(args)

#ara cada par chave-valor em kwargs (os metadados), cria-se uma string no formato "Chave: Valor".
#.title capitaliza a chave (ex.: "autor" vira "Autor").
#Essas strings são então unidas com quebras de linha (\n) para formatação.
  meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
  mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
  print(mensagem)  

exibir_poema("Zen of Python","Beautiful is better than ugly", autor="Tim Peters", ano=1999)
print()

#parametros Especiais - podem ser por posisão, por nome, ou por posição e nome
#somente por posisição
def criar_pedido(N_pedido,valor,/,endereco,comprador):
  print(N_pedido,valor,endereco,comprador)

print("Valido")
criar_pedido(545534,1444.25,"Avenida dos tomates","Seu João") 
print("Invalido")
criar_pedido(1444.25,545534,"Seu João","Avenida dos tomates")
print()

#apenas por nome ou chave
def criar_pedido2(*,N_pedido,valor,endereco,comprador):
  print(N_pedido,valor,endereco,comprador)

print("válido")
criar_pedido2(N_pedido=324132,valor=2345.21,endereco="AVENIDA DO ARROZ",comprador="SEU OMAR")
# print("inválido")
# criar_pedido2(324132,2345.21,"AVENIDA DO ARROZ","SEU OMAR")
print()


#é possivel passaar uma função como parametro
def criar_pedido3(pedido,valor,/,*,endereco,comprador):
  print(pedido,valor,endereco,comprador)

criar_pedido3(7445862,524.45,endereco="Avenida 2",comprador="Dona nona")

def somar (a,b):
  return a+b

def exibir_resultado(a,b,funcao):
  resultado = funcao(a,b)
  print(f"a função deu o resultado de {resultado}")


exibir_resultado(8,5,somar)