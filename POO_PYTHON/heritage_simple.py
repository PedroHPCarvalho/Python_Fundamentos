class Veiculo:
  def __init__(self,*,potencia,valor,cor):
    self.potencia = potencia
    self.valor = valor
    self.cor = cor
  
class Carro(Veiculo):
  def __init__(self, *, potencia, valor, cor, is_drift=False):
    super().__init__(potencia=potencia, valor=valor, cor=cor)
    self.is_dift = is_drift

  def verifica_drift(self,):
    if self.is_dift:
      return print("Fazendo Drift")
    if not self.is_dift:
      return print("Andando normal")
    
class Moto(Veiculo):
  def __init__(self, *, potencia, valor, cor, is_grau=False):
    super().__init__(potencia=potencia, valor=valor, cor=cor)
    self.is_grau = is_grau
  
  def verifica_grau(self):
    if self.is_grau:
      print("Dando Grau")
    if not self.is_grau:
      print("Andando normal")


carro = Carro(potencia=250,valor=30000,cor="Azul",is_drift=True)
carro.verifica_drift()

moto = Moto(potencia=120,valor=13445,cor="verde",is_grau=True)
moto.verifica_grau()