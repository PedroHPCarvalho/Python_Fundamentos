#Neste exemplo o decorador nao possui syntatic sugar
def decorador_sem_acucar_sintatico(funcao):
  def envelope():
    print("Codigo antes da execução da função")
    funcao()
    print("Codigo depois da função")

  return envelope

def ola_mundo():
  print("Ola mundo")

ola_mundo = decorador_sem_acucar_sintatico(ola_mundo)
ola_mundo()