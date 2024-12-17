class Estudante:
  #Atributo de classe
  escola = "Unip"
  def __init__(self, nome_aluno, media_nota):
    self.nome_aluno = nome_aluno
    self.media_nota = media_nota

  def __str__(self):
    return f"{self.nome_aluno} : {self.media_nota} : {self.escola}"
  
def mostra_valores(*objs):
  for obj in objs:
    print(obj)

aluno_1 = Estudante("Pedro",8)
aluno_2 = Estudante("Ana",9)

mostra_valores(aluno_1,aluno_2)
print()
# ATRIBUTO DE INSTANCIA, DADOS FERENTES A UMA INSTANCIA
aluno_1.nome_aluno = "Pedro Carvalho"
mostra_valores(aluno_1,aluno_2)
# ATRIBUTO DE CLASSE É AQUELE Q AFETA TODAS AS INSTANCIAS
print()
Estudante.escola = "Universidade Paulista"
mostra_valores(aluno_1,aluno_2)