
titulo = "Bienvenido al juego de la mazmorra"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n"
      "Tu y tu compañero de celda os acabáis de escapar de la prisión espacial,. habéis burlado a los guardias y os \n"
      "dirigís hacia el exterior. Entrais en una mazmorra controlada por mounstros alienígenas, uno de los guardias \n"
      "ataca a tu compañero, se lo lleva pero tu pasas desapercibido escondido en las sombras. El guardia se retira \n"
      "es tuy posibilidad de escapar. Hacia donde te diriges \n"
      "A la izquierda tienes una puerta semiabierta, a la derecha una escotilla en el suelo.")

opcion = input("A - Puerta semiabierta / B- Escotilla en el suelo\n")

if opcion == "A":
    print("Entras en la puerta y otro guardia te descubre, ¿que haces?:")
    opcion = input("A - Te haces el dormido / B - Sales corriendo hacia la siguiente puerta: ")
    if opcion == "A":
        print("El guardia te atrapa, te encierran en una celda de máxima seguridad \n FIN")

