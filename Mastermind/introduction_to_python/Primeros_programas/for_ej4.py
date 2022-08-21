# Obtiene el mayor y menor de los numeros introducidos por el usuario

numero_introducido = input("Introduzca los numeros separados por coma: ") #1,2,3,4,5,6,7,8,9
numero_usuario = numero_introducido.split(",") # Pero la lista es de tipo string no de int
# List comprehesion 
# es un for rapido 
# Recorre todos los items de numero_usuario y lo pasa por el filtro (int(numero))
numero_usuario = [int(numero) for numero in numero_usuario]

"""
numero_introducido = int(input(("Introduzca un numero en la lista: "))
num_usuario.append(numero_introducido)
while input("Desea introducir mas numeros?") == "S":
    numero_introducido = int(input(("Introduzca un numero en la lista: "))
    numeros.append(num_usuario)
"""

numero_pequenio = numero_usuario[0]
numero_grande = numero_usuario[0]

for numero in numero_usuario[1:]: # indicamos que queremos empezar por el elemento 1, no el 0 
    if numero_pequenio > numero:
        numero_pequenio = numero

    if numero_grande < numero:
        numero_grande = numero

print("Numero grande: {} y numero pequeño: {}" .format(numero_grande,numero_pequenio))