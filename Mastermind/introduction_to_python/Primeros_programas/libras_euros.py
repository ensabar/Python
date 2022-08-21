dolar_euro = 0.91
libra_euro = 1.18
conversion = input("Introduce el tipo de conversion a realizar:\n"
                     "A - Dolar a euro\n"
                     "B - Euro a dolar\n"
                     "C - Libra a euro\n"
                     "D - Euro a libra:\n")
texto_usuario = "Introduce la cantidad de {} a convertir: "

if conversion == "A":
    cantidad = float(input(texto_usuario.format("dolares")))
    print("Son: {}".format(cantidad*dolar_euro) + " euros.")
elif conversion == "B":
    cantidad = float(input(texto_usuario.format("euros")))
    print("Son: {}".format(cantidad/dolar_euro) + " dolares.")
elif conversion == "C":
    cantidad = float(input(texto_usuario.format("libras")))
    print("Son: {}".format(cantidad*libra_euro) + " euros.")
elif conversion == "D":
    cantidad = float(input(texto_usuario.format("euros")))
    print("Son: {}".format(cantidad/libra_euro) + " libras.")
else:
    print("No ha elegido ninguna opcion valida")
