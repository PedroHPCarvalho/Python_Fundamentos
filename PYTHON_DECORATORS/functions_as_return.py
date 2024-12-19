#Neste exemplo é retornada uma função de outra função

def calculadora(operacao):

  def soma(a,b):
    return a + b
  
  def sub(a,b):
    return a - b
  
  def mul(a,b):
    return a * b

  def div(a,b):
    return a / b
  
# Match é o Switch case em python
  match operacao:
    case "+":
      return soma
    case "-":
      return sub
    case "*":
      return mul
    case "/":
      return div
        
print(calculadora("+")(2,4))
print()
print(calculadora("-")(2,4))
print()
op = calculadora("*")
print(op(2,64))
print()
op = calculadora("/")
print(op(64,2))
print()