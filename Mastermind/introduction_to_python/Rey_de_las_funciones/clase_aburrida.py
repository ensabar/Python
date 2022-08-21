import random

from numpy import empty


def string_mas_larga(*palabras):
    str_mas_larga = []
    for n in palabras:
        if len(str_mas_larga) < len(n):
            str_mas_larga = n
    return str_mas_larga


def suma(*lista):
    total = 0
    for n in lista:
        total +=n
    return total


def es_impar(numero):
    if(numero%2 == 0):
        return False
    return True


"""
def seguro():
   pregunta = input("Estas seguro? S o N: ") 
    decision = empty
    if(pregunta == "S"):
        decision = True
    else:
        decision = False
   return decision
   """

def a_mayus(palabra):
    cadena = []
    for n in palabra:
        mayus = ord(n)-32 # Obtienes el valor en ASCII y segun la tabla se resta 32 para obtener la mayuscula correspondiente
        cadena.append(chr(mayus))
    return cadena
        
def adivina():
    n = random.randint(1,100)

    acertar = False
    while acertar != True:
        numero = int(input("Introduce un numero del 1 al 100: "))
        if(numero == n):
            acertar = True
        else:
            print("No has acertado, vuelve a intentarlo... ")
    print("Has acertado el numero es {}" .format(n))

compra = ["agua", "cafe", "ternera"] 

def lista_compra(articulo):
    #articulo = input("Que deseas comprar: ")

    if articulo in compra:
        print("El articulo ya esta en la lista de la compra")
    else:
        compra.append(articulo)
        print("{} se ha anyadido a la lista de la compra" .format(articulo))





def main():
    """
    print(string_mas_larga("hola", "como", "estas",))
    print(suma(1, 2, 3, 4, 5))
    print(es_impar(3))
    print(es_impar(24))
    #print(seguro())
    print(a_mayus("hola"))
    adivina()
   """
    lista_compra("cafe")


if __name__ == "__main__":
    main()