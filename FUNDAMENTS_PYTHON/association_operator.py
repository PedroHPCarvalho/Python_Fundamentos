# Operador in
curso = "curso de python"
frutas = ["abacaxi","pera","uva"]
nome_curso = curso
saldo, limite = 100, 200

print("------ Operador in -------")
print ("python" in nome_curso) # É CASE_SENSITIVE
print ("Python" in nome_curso) 
print (nome_curso)

print()

print("uva" in frutas)
print (frutas)

print()
#----------------------------------------
# Operador not in
print("------ Operador is not -------")

print ("python" not in nome_curso)
print (curso)

print()

print("carro" not in frutas)
print (frutas)