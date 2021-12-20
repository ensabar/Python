# Mapa con entrenadores pokemon
import os
import random

import readchar

POS_X = 0
POS_Y = 1

NUM_OF_MAP_TRAINERS = 3

obstacle_definition ="""\
############################
                      ######
###        #######    ######
###        #######    ######
##################    ######
########   #####    ########
########              ######\
"""


my_position = [0, 1]
map_objects = []


end_game = False
died = False
# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)
# Generate random objects
while len(map_objects) < NUM_OF_MAP_TRAINERS:
    new_position = [random.randint(0,MAP_WIDTH - 1),random.randint(0,MAP_HEIGHT - 1)]

    if new_position not in map_objects and new_position != my_position and \
    obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#": # Comprobamos que no se repita ninguna posicion y no este en la misma posicion que el usuario
        map_objects.append(new_position)
      
# Main Loop
while not end_game:
    os.system("cls")

    # Draw map
    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            trainer_in_cell = None

            for map_object in map_objects:

                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    trainer_in_cell = map_object # Cuando detectamos un objeto, marcamos su posicion
                    
            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                if trainer_in_cell: # Si el objeto se encuenta en la misma posicion que el usuario, lo eliminamos
                    map_objects.remove(trainer_in_cell)
                    # Se ejectuta el combate pokemon
                    my_position[POS_X] == coordinate_x
                    my_position[POS_Y] == coordinate_y
                    char_to_draw = " @"
                    ########################################################################
                    # Declaracion de constantes
                    VIDA_INICIAL_PIKACHU = 10
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
                        while ataque_squirtle not in ["P", "A", "B", "N"]:
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
                    ########################################################################
                    NUM_OF_MAP_TRAINERS -=1
                    break


            if obstacle_definition[coordinate_y][coordinate_x] == "#":
                char_to_draw = "##"
            
            print("{}".format(char_to_draw), end="") # con el parametro end consigues que no introduzca un intro al final del print
        print("|")
    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    # Where to move
    direction = readchar.readchar().decode() 
    # Devuelve el caracter introducido por teclado
    # Devuelve un tipo byte, con decode se lo quita y se queda tipo string
    # Utilizando la operacion modulo te devuelve las casillas de desplazamiento extra y te reconduce a la primera.
    new_position = None
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_HEIGHT]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_HEIGHT]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
        
    elif direction == "q": # con la q cerramos el programa
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]]!= "#": # Dectamos si hay algun corchete y si podemos desplazarnos
            my_position = new_position
    

if died:
    print("Has muerto!!")


