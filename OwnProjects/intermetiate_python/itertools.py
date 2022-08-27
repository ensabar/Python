# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators

# Product
from itertools import product
a = [1, 2]
b = [3, 4]
prod = product(a,b)
print(list(prod))

# permutations
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

perm = permutations(a,2)
print(list(perm))

# combinations
from itertools import combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

from itertools import combinations_with_replacement
a = [1, 2, 3, 4]
comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# Accumulate
from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func = operator.mul)
print(a)
print(list(acc))


a = [1, 2, 5, 3, 7, 4]
acc = accumulate(a, func = max)
print(a)
print(list(acc))

# groupby
from itertools import groupby
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key = smaller_than_3)


for key, value in group_obj:
    print(key, list(value))

a = [1, 2, 3, 4]
group_obj = groupby(a, key= lambda x: x<3)


for key, value in group_obj:
    print(key, list(value))


persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

# Group by age
group_obj = groupby(persons, key= lambda x: x['age'])
for key, value in group_obj:
    print(key, list(value))

# infinite operators
from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break

