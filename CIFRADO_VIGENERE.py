def cifrado_vigenere(texto, clave):
    resultado = []
    clave = clave.upper()
    indice_clave = 0
    
    for i in range(len(texto)):
        caracter = texto[i]
        
        if caracter.isupper():
            desplazamiento = ord(clave[indice_clave % len(clave)]) - 65
            resultado.append(chr((ord(caracter) + desplazamiento - 65) % 26 + 65))
            indice_clave += 1
        elif caracter.islower():
            desplazamiento = ord(clave[indice_clave % len(clave)]) - 65
            resultado.append(chr((ord(caracter) + desplazamiento - 97) % 26 + 97))
            indice_clave += 1
        else:
            resultado.append(caracter)
    
    return ''.join(resultado)

# Ejemplo de uso
texto = "Hola Mundo"
clave = "Clave"
texto_cifrado = cifrado_vigenere(texto, clave)
print("Texto Cifrado:", texto_cifrado)