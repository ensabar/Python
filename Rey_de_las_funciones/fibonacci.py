# Utilizando la recursividad calcular una serie de Fibonacci:

def fibbonacci_recursivo(n):
    if (n <=1):
        return 1
    return fibbonacci_recursivo(n-1) + fibbonacci_recursivo(n-2)
    
    




def main():
   for f in range(8):
        print(fibbonacci_recursivo(f))


if __name__ == "__main__":
    main()