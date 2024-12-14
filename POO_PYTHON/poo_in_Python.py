class bicicleta:
  def __init__(self,cor,modelo,ano,valor):
    self.cor = cor
    self.modelo = modelo
    self.ano = ano
    self.valor = valor
  
  def buzininar(self):
    print("Buzinando")
  
  def parar(self):
    print("Parando...")

  def correr(self):
    print("correndo..")

  def minha_cor(self):
    return self.cor

  def __str__(self):
    return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave,valor in self.__dict__.items()])}"


bicicleta1 = bicicleta("amarelo","caloi",2001,1200)
bicicleta1.buzininar()
bicicleta1.parar()
bicicleta1.correr()
print(bicicleta1.cor,bicicleta1.modelo,bicicleta1.ano,bicicleta1.valor)
print()
print(bicicleta.minha_cor(bicicleta1))
print(bicicleta1)
    
