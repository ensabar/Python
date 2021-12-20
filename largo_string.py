
def largo_string(my_string):
    largo = 0
    for n in my_string:
        largo +=1
    return largo

largo_de_string = largo_string("Hola mundo")
print(largo_de_string)