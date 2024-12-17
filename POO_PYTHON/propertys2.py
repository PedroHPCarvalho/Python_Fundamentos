class Pessoa:
  def __init__(self,nome,ano_nascimento,documento):
    self.nome = nome
    self._ano_nascimento = ano_nascimento
    self.__documento = documento

  @property
  def documento(self):
    return  self.__documento or None
    
    @documento.setter()
  