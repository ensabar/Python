# Tabla de multiplicar que solo devuelve los numeros multiplos de 2
tabla = int(input("Que tabla de multiplicar desea el usuario?: "))

for n in range(1,11):
    if n % 2 == 0:
        print("{} * {} = {} ".format(tabla, n, tabla*n))