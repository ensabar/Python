# lambda arguments: expression

add10 = lambda x: x + 10

print(add10(5))

def add10_func(x):
    return x + 10

mult =  lambda x,y: x*y

print(mult(2,5))

# ordered by y position
print('Ordered by x position')
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D)
print(points2D)
print(points2D_sorted)

# ordered by y position
print('Ordered by y position')
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

# ordered by sum of each tuple
print('Ordered by sum of each tuple')
points2D = [(1, 2), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D, key=lambda x: x[0] + x[1])
print(points2D)
print(points2D_sorted)

# map (func, seq)
print('Usin map funciton')
a = [1, 2, 3, 4, 5]
b = map(lambda x: x*2, a)
print(a)
print(list(b))

# same with list comprehension
print('With list comprehension')
c = [x*2 for x in a]
print(a)
print(c)

# filter(func, seq)
print('Filtering usin filter function')
a = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x%2 == 0, a)
print(a)
print(list(b))

print('Filtering usin list comprehension')
a = [1, 2, 3, 4, 5, 6]
b = [x for x in a if x%2 == 0]
print(a)
print(b)

# reduce(func, seq)
from functools import reduce
print('Reducing usin reduce function')
a = [1, 2, 3, 4]
product_a = reduce(lambda x,y: x*y, a)
print(product_a)



