def cifrado_cesar(texto, desplazamiento):
    resultado = ""
    
    for i in range(len(texto)):
        caracter = texto[i]
        
        if caracter.isupper():
            resultado += chr((ord(caracter) + desplazamiento - 65) % 26 + 65)
        elif caracter.islower():
            resultado += chr((ord(caracter) + desplazamiento - 97) % 26 + 97)
        else:
            resultado += caracter
    
    return resultado

# Ejemplo de uso
texto = "Hola Mundo"
desplazamiento = 3
texto_cifrado = cifrado_cesar(texto, desplazamiento)
print("Texto Cifrado:", texto_cifrado)

