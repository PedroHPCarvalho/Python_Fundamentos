#TODO: Crie uma classe para converter temperaturas de Celsius para Fahrenheit e um método que realiza o cálculo de conversão:
class ConversorTemperatura:
  def __init__(self):
    pass

  def celsius_para_fahrenheit(self,celsius):
    fahrenheit = (celsius* 9 / 5)+32
    return fahrenheit
    
  
# Entrada do usuário
celsius = float(input())

# TODO: Crie uma instância do conversor:
conversor = ConversorTemperatura()

fahrenheit = conversor.celsius_para_fahrenheit(celsius)
print(fahrenheit)