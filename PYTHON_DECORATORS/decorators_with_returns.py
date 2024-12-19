#Neste exemplo o decorador possui argumentos e retorna valores
def decorador_sem_acucar_sintatico(funcao):
  def envelope(*args, **kwargs):
  #Dessa maneira o codigo se torna mais flexivel, podendo ter mais argumentos
    print("Codigo antes da execução da função")
    #Para poder retornar, o valor deve ser armazenado
    resultado = funcao(*args, **kwargs)
    print("Codigo depois da função")
    return resultado

  return envelope

#syntatic sugar
@decorador_sem_acucar_sintatico
def ola_mundo(nome):
  print(f"Ola mundo {nome}!")
  return nome.upper()

resultado = ola_mundo("Joao")
print(resultado)