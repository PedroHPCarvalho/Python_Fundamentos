#Encapsulamento em python se trata mais de uma convenção doque uma regra
# a IDE não garante o encapsulamento forçadamente
#publicas = não possuem nenhum sinal especifico

#Protedido = se usa o sinal (_) Eles não são acessíveis a partir de
#  fora da classe, mas podem ser utilizados pelas subclasses. 
# O encapsulamento protegido é útil quando você deseja restringir 
# o acesso direto a certos elementos da classe, mas 
# ainda permitir que as subclasses os utilizem.

#Privado = Utiliza o sinal (__) les não são acessíveis a partir de 
# fora da classe e nem pelas subclasses. O encapsulamento privado 
# é o nível mais restritivo e é utilizado quando você deseja 
# ocultar completamente os detalhes de implementação da classe.

class Conta:
  def __init__(self,nro_agencia,saldo=0):
    self.nro_agencia = nro_agencia
    self.__saldo = saldo

  def mostrar_saldo(self):
    return self.__saldo
  
  def add_saldo(self,valor):
    self.__saldo += valor


conta = Conta("NA234")
print(conta.mostrar_saldo())
conta.add_saldo(452)
print(conta.mostrar_saldo())

