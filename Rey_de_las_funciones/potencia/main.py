
def potencia(number, *args):
    for n in args:
        return float(args) ** number
    return 2 ** number




def main():
    print(potencia(4))
    print(potencia(4, 7))



if __name__ == "__main__":
    main()