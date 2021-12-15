import random
import os
# Declaracion de constantes
VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90
TAMANIO_BARRA_VIDA = 20

vida_actual_pikachu = VIDA_INICIAL_PIKACHU
vida_actual_squirtle = VIDA_INICIAL_SQUIRTLE

while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:
    os.system("cls") # Limpia el terminal 

    #Turno pikachu
    print("Turno de Pikachu")
    ataque_pikachu = random.randint(1,3)
    if ataque_pikachu == 1:
        # Bola voltio
        print("Pikachu ataca con Bola Voltio")
        vida_actual_squirtle -=10
    elif ataque_pikachu == 2:
        # Onda Trueno
        print("Pikachu ataca con Onda Trueno")
        vida_actual_squirtle -=11 
    elif ataque_pikachu == 3:
        print("Pikachu no hace nada")

    if vida_actual_squirtle < 0:
        vida_actual_squirtle = 0   
    factor_pikachu = round(vida_actual_pikachu/VIDA_INICIAL_PIKACHU*TAMANIO_BARRA_VIDA)
    factor_squirtle = round(vida_actual_squirtle/VIDA_INICIAL_SQUIRTLE*TAMANIO_BARRA_VIDA)
   
    print("La vida de Pikachu es  [{}{}] ({}/{})" .format("#" * factor_pikachu," " * (TAMANIO_BARRA_VIDA - factor_pikachu), vida_actual_pikachu,VIDA_INICIAL_PIKACHU))
    print("La vida de Squirtle es [{}{}] ({}/{})" .format("#" * factor_squirtle," " * (TAMANIO_BARRA_VIDA - factor_squirtle), vida_actual_squirtle,VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n\n")
    os.system("cls") # Limpia el terminal 

    # Turno Squirtle
    print("Turno Squirtle")
    ataque_squirtle = None
    while ataque_squirtle != "P" and ataque_squirtle != "A" and ataque_squirtle != "B":
        ataque_squirtle = input("Que ataque deseas realizar P - placaje, A - Pistola Agua, B - Burbuja, N - No hacer nada: ")

    if ataque_squirtle == "P":
        print("Squirtel ataca con Placaje")
        vida_actual_pikachu -=10
    
    elif ataque_squirtle == "A":
        print("Squirtel ataca con Pistola Agua")
        vida_actual_pikachu -=12
    elif ataque_squirtle == "B":
        print("Squirtel ataca con Burbuja")
        vida_actual_pikachu -=9
    elif ataque_squirtle == "N":
        print("Squirtle no hace nada.")
    
    if vida_actual_pikachu < 0:
            vida_actual_pikachu = 0
    factor_pikachu = round(vida_actual_pikachu/VIDA_INICIAL_PIKACHU*TAMANIO_BARRA_VIDA)
    factor_squirtle = round(vida_actual_squirtle/VIDA_INICIAL_SQUIRTLE*TAMANIO_BARRA_VIDA)
    print("La vida de Pikachu es  [{}{}] ({}/{})" .format("#" * factor_pikachu," " * (TAMANIO_BARRA_VIDA - factor_pikachu), vida_actual_pikachu,VIDA_INICIAL_PIKACHU))
    print("La vida de Squirtle es [{}{}] ({}/{})" .format("#" * factor_squirtle," " * (TAMANIO_BARRA_VIDA - factor_squirtle), vida_actual_squirtle,VIDA_INICIAL_SQUIRTLE))
    input("Enter para continuar...\n\n")

if vida_actual_pikachu > vida_actual_squirtle:
    print("Gana Pikachu")
else:
    print("Gana Squirtle")
