#Neste exemplo o decorador possui argumentos
def decorador_sem_acucar_sintatico(funcao):
  def envelope(*args, **kwargs):
  #Dessa maneira o codigo se torna mais flexivel, podendo ter mais argumentos
    print("Codigo antes da execução da função")
    funcao(*args, **kwargs)
    print("Codigo depois da função")

  return envelope

#syntatic sugar
@decorador_sem_acucar_sintatico
def ola_mundo(nome):
  print(f"Ola mundo {nome}!")

ola_mundo("PEDRO")