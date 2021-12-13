import random
titulo = "Bienvenido al juego de la mazmorra"
print("\n" + titulo + "\n" + "-" * len(titulo) + "\n"
      "Tu y tu compañero de celda os acabáis de escapar de la prisión espacial,. habéis burlado a los guardias y os \n"
      "dirigís hacia el exterior. Entrais en una mazmorra controlada por mounstros alienígenas, uno de los guardias \n"
      "ataca a tu compañero, se lo lleva pero tu pasas desapercibido escondido en las sombras. El guardia se retira \n"
      "es tuy posibilidad de escapar. Hacia donde te diriges \n"
      "A la izquierda tienes una puerta semiabierta, a la derecha una escotilla en el suelo.")

opcion = input("A - Puerta semiabierta / B - Escotilla en el suelo: \n")
palo_en_inventario = False
if opcion == "A":
    print("Entras en la puerta y otro guardia te descubre, ¿que haces?:")
    opcion = input("A - Te haces el dormido / B - Sales corriendo hacia la siguiente puerta: \n")
    if opcion == "A":
        print("El guardia te atrapa, te encierran en una celda de máxima seguridad \n FIN")
    if opcion == "B":
        print("Despues de esa puerta encuentras una rana mutante que te regaña un puñal casero hehcho con la pata de una mesa,\n" 
        "lo aceptas?")
        opcion = input("A - Si / B - No:")
        if opcion == "A":
            print("Coges el pincho y avanzas, hay dos pasillos circulares, no ves el final de ninguno de los dos, uno está a \n"
            "la derecha y el otro a la izquierda, cual tomas?: ")
            opcion = input("A - Izquierda / B - Derecha: \n")
            if opcion == "A":
                print("La habitación se hace cada vez más oscura, ves tan poco que caes en un agujero en el suelo con\n"
                "mueres a las dos horas de forma lenta y dolorosa. \n FIN")
            if opcion == "B":
                print("Encuentras la salida, en la puerta hay aparcado un Ferrari espacial, te montas es tu dia de suerte, escapas.")
        if opcion == "B":
            print("La rana te devora, mueres de forma rápida, el veneno hace efecto casi\
            de manera instantánea. \n FIN")
if opcion == "B":
    print("Caes en una zona inundada, el agua te llega hasta las rodillas, avanzas durante meda hora y finalmente llegas a una zona \n"
    "abierta, seca y con luz, parecen unas alcantarillas.\n "
    "Encuentras un palo largo, parece algo pesado pero podría servir, lo coges?")
    opcion = input("A - Sí / B - No: \n")
    if opcion == "A":
        print("Coges el palo")
        palo_en_inventario = True
    if opcion == "B":
        print("No coges el palo")
    num_rand=random.randint(1,50)
    opcion = int(input("Sigues adelante, encuentras una rata de 2 metros, la rata te pregunta cuanto es 13*{} \n".format(num_rand)))
    if opcion == 13*num_rand:
        print("La rata te asesina en el acto, resulta que no tolera a los cerebritos. \n FIN")
    if opcion != 13*num_rand:
        print("La rata abre una puerta delante de ti, parece un pasillo que lleva hasta la salida. Lo recorres, llegas al final, el tunel \n"
        "se derrumba detras de ti, no hay salida más que una especie de boca de alcantarilla pero esta lejos de tu alcance, que haces?\n")
    opcion = input("A - Esperas a que alquien te rescate / B - Si tienes el palo")
    if opcion == "A":
        print("Un monton de ratas aparecen y te devoran vivo, es tu fin. \n FIN")
    if opcion == "B" and palo_en_inventario == True:
        print("Usas el palo para impulsate, es tu dia de suerte y consigues escapar. \n FIN")
    elif opcion == "B" and palo_en_inventario == False:
        print("No tienes como escapar y mueres. \n FIN")


