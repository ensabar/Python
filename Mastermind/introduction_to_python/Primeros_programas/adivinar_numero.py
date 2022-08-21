import random
num = int(input("Introduce un numero del 1 al 10: "))
num_ganador = random.randint(1, 10)

if num == num_ganador:
    print("Has ganado, enhorabuena!!")

if num > 10:
    print("Te has pasado, el número es inferior a 10.")

if num < 1:
    print("Te has quedado corto, el número es superior a 1")

print("El numero ganadaor era el: {}" .format(num_ganador))