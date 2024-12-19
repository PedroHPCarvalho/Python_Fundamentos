import functools

def decorador_sem_acucar_sintatico(funcao):
  @functools.wraps(funcao)  
  def envelope(*args, **kwargs):
    funcao(*args, **kwargs)

  return envelope


@decorador_sem_acucar_sintatico
def ola_mundo(nome):
  print(f"Ola mundo {nome}!")


print(ola_mundo.__name__)