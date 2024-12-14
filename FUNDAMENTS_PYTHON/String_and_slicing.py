#Metodos para manipulação de String
String = "Palavras"

print(String.upper()) # Todas Maiusculas

print(String.lower()) # Todas Minusculas

print(String.title()) # Transforma em formato de titulo

String2 =  "       Palavras   "

print(String2.strip()) # Elimina os espaços

print(String2.lstrip()) # adiciona espaço a esquerda

print(String.rstrip()) # adiciona espaço a esquerda

print(String.center(10,"#")) # Centraliza o texto, preeenchendo com caracteres o resto

print(".".join(String2)) #inclui um caractere entre a string

#----------------------------------------------

#OLD Style %
nome = "Pedro"
idade = 21

print("Bom dia, meu nome é %s e tenho %d anos de idade" % (nome,idade))

#------------------------------------------
#format

print("Eu sou {} e tenho {} de idade" .format(nome,idade))

#--------------------------------------------
#f-string
print(f"Eu sou {nome} e tenho {idade} anos de idade")

#------------------------------------------------
#fatiamento
frase = "Fui comprar arroz hoje pela tarde"

print(frase[0:10])

#_____________________________________________
frase2 = """" Bom dia, sou {nome} e {frase}, 
dia 21 irei completar {idade} de idade
"""
print("""" Bom dia, sou {nome} e {frase}, 
dia 21 irei completar {idade} de idade
""")