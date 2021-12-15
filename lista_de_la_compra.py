from io import open_code


compra = []
opcion = None
while opcion != "Q":
    opcion = input("Que desea comprar? [Q para salir]")
    if opcion == "Q":
        pass
    elif opcion in compra:
        print("{} ya esta en la lista!".format(opcion))
    else:
        if input("Seguro que quiere añadir {} en la lista? S/N: " .format(opcion)) == "S":
            compra.append(opcion)
            print(opcion + " añadido a la lista de la compra.")
print("La lista de la compra es: \n {}" .format(compra))
