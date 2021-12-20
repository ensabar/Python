# Mapa bidimensional por el que nos vamos desplazando y en las esquinas aparecemos en el otro lado
import readchar
import os
import random

POS_X = 0
POS_Y = 1

NUM_OF_MAP_OBJECTS = 11

obstacle_definition ="""\
############################
                      ######
##################    ######
##################    ######
##################    ######
################    ########
#############         ######
###############   ######### 
##############    ####      
###############             
##################    ####  
########     #####    ####  
#####       ####            
##########  ######    ####  
#########   ######    ####  
#########  ###############  \
"""


my_position = [15, 8]
map_objects = []
tail_length = 0
tail = []

end_game = False
died = False
# Create obstacle map
obstacle_definition = [list(row) for row in obstacle_definition.split("\n")]

MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)

# Main Loop
while not end_game:
    os.system("cls")
    # Generate random objects
    while len(map_objects) < NUM_OF_MAP_OBJECTS:
        new_position = [random.randint(0,MAP_WIDTH - 1),random.randint(0,MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and \
        obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#": # Comprobamos que no se repita ninguna posicion y no este en la misma posicion que el usuario
            map_objects.append(new_position)
      
    # Draw map
    print("+" + "-" * (MAP_WIDTH * 2) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDTH):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_object in map_objects:

                if map_object[POS_X] == coordinate_x and map_object[POS_Y] == coordinate_y:
                    char_to_draw = " *"
                    object_in_cell = map_object # Cuando detectamos un objeto, marcamos su posicion

            for tail_element in tail: 
                if tail_element[POS_X] == coordinate_x and tail_element[POS_Y] == coordinate_y:
                    char_to_draw = " @"
                    tail_in_cell = tail_element

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " @"

                if object_in_cell: # Si el objeto se encuenta en la misma posicion que el usuario, lo eliminamos
                    map_objects.remove(object_in_cell)
                    tail_length += 1 # Incrementamos el tamanio de la cola

                if tail_in_cell:
                    died = True
                    end_game = True



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

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]
        
    elif direction == "q": # con la q cerramos el programa
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]]!= "#": # Dectamos si hay algun corchete y si podemos desplazarnos
            tail.insert(0, my_position.copy()) # Insertamos una copia para que no se actualize en cada momento
            tail = tail[:tail_length]
            my_position = new_position
    

if died:
    print("Has muerto!!")


