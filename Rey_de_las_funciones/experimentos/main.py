
def medir_largos(iterable, *args, sumar_todo=False):

    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        if sumar_todo:
            largos = sum(largos)
        return largos
    return len(iterable)




def main():
    print(medir_largos("hola"))
    print(medir_largos("hola", "como", "estas", sumar_todo=True))



if __name__ == "__main__":
    main()