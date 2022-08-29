import sys
import timeit
# Tuple: ordered, immutable, allow duplicate elements
mytuple = ('Max', 28, 'Boston')
print(mytuple)
# if you want to create a tuple of one element
# mytuple = 'Max', # needs a coma at the end

print(mytuple[0]) # first item
print(mytuple[-1]) # last item
# change a value is not posible because a tuple is immutable
#mytuple[0] = 'pepe'

for i in mytuple:
    print(i)

#check if an element is in tuple
if 'TIM' in mytuple:
    print('yes')
else:
    print('no')
# Create a tuple with some letters
mytuple = ('a', 'p', 'p', 'l', 'e')

#number of elements
print(len(mytuple))
#count an element
print(mytuple.count('p'))
#find index of some element
print(mytuple.index('p'))

#convert a tuple to list and viceversa
mylist = list(mytuple)
print(mylist)
print(type(mylist))

mytuple2 = tuple(mylist)
print(mytuple2)
print(type(mytuple2))

# Slicing

mylist = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
b = mylist[2:5] # in a tuple values goes from 2 to 4 (5 not included)
c = mylist[:5]
d = mylist[2:]
print(mylist)
print(b)
e = mylist[::2]
f = mylist[:-1]
print(c)
print(d)
print(e)
print(f)

# Packaging and unpackaging

mytuple = ('Max', 28, 'Boston')

name, age, city = mytuple
print(name)
print(age)
print(city)


mytuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = mytuple

print(i1)
print(i3)
print(i2) # all elements between i1 and i3 and coverted to a list


# Comparison of length between list and tuple, so tuple is more efficent to iterate

my_list = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print(sys.getsizeof(my_list), 'bytes')
print(sys.getsizeof(my_tuple), 'bytes')

# Comparison between time of creation a list and a tuple

print(timeit.timeit(stmt='[0, 1, 2, 3 ,4 ,5]', number = 1000000))
print(timeit.timeit(stmt='(0, 1, 2, 3 ,4 ,5)', number = 1000000))

