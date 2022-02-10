edad = int(input("Digame su edad: "))
carnet = input("Dime tu tipo de carnet (E estudiante / P pensionista / F familia numerosa / N Nada): ")

if (25 <= edad <= 35 and carnet == "E") or edad <= 10 or (edad >= 65 and carnet == "P") or (carnet == "F"):
    print("Se te aplica el descuento.")
else:
    print("No se te aplica el descuento")

