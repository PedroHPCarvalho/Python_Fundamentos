def contar_caracteres(string):
    # Inicialize um dicionário vazio 'contador' para armazenar as contagens de caracteres.
    contador = {}
    
    # Itere através de cada caractere na string.
    for caractere in string:
        # Verifique se o caractere já está presente no dicionário contador.
        if caractere in contador:
            # Se estiver, incremente a contagem.
            contador[caractere] += 1
        else:
            # Caso contrário, inicialize a contagem como 1.
            contador[caractere] = 1
    
    return contador

# Solicita entrada do usuário
entrada = input()
resultado = contar_caracteres(entrada)
print(resultado)
