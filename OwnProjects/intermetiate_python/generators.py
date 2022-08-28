
#def mygenerator():
#    yield 3
#    yield 2
#    yield 1


#g = mygenerator()

#value = next(g)
#print(value)
#
#value = next(g)
#print(value)

#print(sum(g))
#print(sorted(g))

###############################################################

#def countdown(num):
#    print('Starting')
#    while num > 0:
#        yield num
#        num -= 1
#
#cd = countdown(4)
#
#print(next(cd))
#print(next(cd))

###############################################################
#import sys
#
#def firstn(n):
#    nums = []
#    num = 0
#    while num < n:
#        nums.append(num)
#        num += 1
#    return nums
#
## usin a generator....
#
#def firstn_generator(n):
#    num = 0
#    while num < n:
#        yield num
#        num += 1
#
#print(sys.getsizeof(firstn(1000000)))
#print(sys.getsizeof(firstn_generator(1000000)))

###############################################################
# Fibonacci secuence

#def fibonacci(limit):
#    a, b = 0, 1
#    while a < limit:
#        yield a
#        a, b = b, a + b
#
#fib = fibonacci(30)
#for i in fib:
#    print(i)

###############################################################
# Gerenator with strings
import sys

mygenerator = (i for i in range (1000000) if i % 2 == 0)
print(sys.getsizeof(mygenerator))

mylist = [i for i in range (1000000) if i % 2 == 0]
print(sys.getsizeof(mylist))

