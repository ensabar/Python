
vocales = ["a", "e", "i", "o", "u"]
frase = "Hoy estoy aprendiendo Python"
vocales_encontradas = 0

for letra in frase:
    if letra in vocales:
        vocales_encontradas += 1
        print("Ha encontrado la vocal: {}" .format(letra))

print("Vocales encontradas: {}".format(vocales_encontradas))