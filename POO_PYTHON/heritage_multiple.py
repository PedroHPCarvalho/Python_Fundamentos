class Veiculo:
  def __init__(self,cor,placa):
    self.cor = cor
    self.placa = placa

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"
  
class Carro_Sedan(Veiculo):
  def __init__(self,tamanho_portamalas,**kw):
    self.tamanho_portamalas = tamanho_portamalas
    super().__init__(**kw)

class Carro_Esportivo(Veiculo):
  def __init__(self, tipo_motor ,**kw):
    self.tipo_motor = tipo_motor
    super().__init__(**kw)

class Sedan_Esportivo(Carro_Sedan,Carro_Esportivo):
  def __init__(self,tamanho_portamalas,tipo_motor,**kw):
    super().__init__(tamanho_portamalas=tamanho_portamalas,tipo_motor=tipo_motor,**kw)
    
    #Outra maneira de fazer
    # def __init__(self,tipo_motor,tamanho_portamalas,cor,placa):
    #super().__init__(tamanho_portamalas,tipo_motor=tipo_motor,cor=cor,placa=placa)

logan = Carro_Sedan(500,cor="cinza",placa="sat-1223")
ferrari = Carro_Esportivo(tipo_motor="V8",cor="Azul",placa="DAS-4567")
bmw = Sedan_Esportivo(550,"v10",cor="Roxo",placa="KSA-9021")

print(logan,"\n")
print(ferrari,"\n")
print(bmw,"\n")
print()
print(Sedan_Esportivo.mro())