from typing import final


zeros = [0, 2] * 8
print(zeros)

# *args and **kwargs
def foo(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

foo(1, 2, 3, 4, 5, 6, six = 6, seven = 7)

# Unpacking

def foo(a, b, c):
    print(a, b, c)

mylist = [0, 1, 2]
foo(*mylist)

mytuple = (0, 1, 2)
foo(*mytuple)

mydict = {'a': 1, 'b': 2, 'c': 3}
foo(**mydict)


numbers = [1, 2, 3, 4, 5, 6]
beginning, *middle,  last = numbers
print(beginning)
print(last)

mytuple = (1, 2, 3)
mylist = [4, 5, 6]

newlist = [*mytuple, *mylist]
print(newlist)

dict_a = {'a': 1, 'b': 2}
dict_b = {'c': 3, 'd': 4}

mydict = {**dict_a, **dict_b}
print(mydict)





