# Cuenta el numero de mayusculas que hay en un texto introducido por el usuario

import string
texto_usuario = input("Introduzca un texto: ")

letras_mayusculas = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1 

print("Hay {} mayusculas" .format(letras_mayusculas))