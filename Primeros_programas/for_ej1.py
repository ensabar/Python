# Cuenta los espacios, comas y puntos de un texto introducido por el usuario

texto_usuario = input("Introduzca un texto: ")
espacios = 0
comas = 0
puntos = 0

for letra in texto_usuario:
    if letra == " ":
        espacios += 1
    elif letra == ".":
        puntos += 1
    elif letra == ",":
        comas += 1

print("Hay {} espacios, {} comas y {} puntos." .format(espacios,comas, puntos))
