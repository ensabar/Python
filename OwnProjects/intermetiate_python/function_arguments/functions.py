import numbers


def foo(a, b, c):
    print(a, b, c)

foo(1, 2, 3)
foo(a=1, b=2, c=3)
foo(c=1, a=2, b=3)

def fooo(a, b, c, d=4): # with default parameter
    print(a, b, c, d)

fooo(1, 2, 3)


def foooo(a, b, *args, **kwargs):
    print(a, b)
    for args in args:
        print(args)
    for key in kwargs:
        print(key, kwargs[key])

foooo(1, 2, 3, 4, 5, 6, six=6, seven=7)

# Force and unforce arguments

#def foo(a, b, *args, c, d):
#    print(a, b, c, d)
#
#print(1, 2, c=4, d=5)

def foo(*args, last):
    for arg in args:
        print(arg)
    print(last)

foo(1, 2, last=100)

# Unpacking arguments

def foo(a, b, c):
    print(a, b, c)

mylist =  [0, 1, 2]
foo(*mylist)

mydict = {'a': 1, 'b': 2, 'c': 3} # keys have to match parameters function
foo(**mydict)

# Local vs global variables
def foo_local_global():
    global number
    x = number
    number = 3
    print('number inside function', x)


number = 0
foo_local_global()
print('number out function', number)

# parameter passing

def foo(a_list):
    a_list.append(4)
    a_list[0] = -100

mylist = [1, 2, 3]
foo(mylist)
print(mylist)


