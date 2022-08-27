# Sets: unordered, mutable, no duplciates
from re import S


myset = {1, 2, 3, 4, 5, 6}
print(myset)
myset = {1, 2, 3, 1, 2, 3}
print(myset)

myset = set([1, 2, 3])
print(myset)

myset = set('Hello')
print(myset)

myset = {1, 2, 3, 4, 5, 6}

myset.add(8)
myset.add(9)
print(myset)


myset.discard(5)
print(myset)


myset.clear()
print(myset)
myset = {1, 2, 3, 4, 5, 6}
myset.pop() # delete last item
print(myset)


# iterate a set
print('Iteare a set')

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

for x in myset:
    print(x)


# chech if an element is in our set

if 4 in myset:
    print('yes')

# Union an intersection of sets

odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

u = odds.union(evens)
print(u)

i = evens.intersection(primes)
print(i)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

diffA = setA.difference(setB)

print(diffA)


diffB = setB.difference(setA)

print(diffB)

#Simetric different method

diffC = setB.symmetric_difference(setA)

print(diffC)

setA.update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.intersection_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
setA.difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setA.symmetric_difference_update(setB)
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
print(setB.issubset(setA))

print(setA.issuperset(setB))

setC = {7, 8}
print(setA.isdisjoint(setC))

# copying sets
setA = {1, 2, 3, 4, 5, 6}

setB = setA

setA.add(7)

print(setA)
print(setB)

setA = {1, 2, 3, 4, 5, 6}
setB = set(setA)

setA.add(7)

print(setA)
print(setB)

# Frozen a set

a = frozenset([1, 2, 3, 4])
 
# You cant update this set usin union, intersection, add, remove, update...


