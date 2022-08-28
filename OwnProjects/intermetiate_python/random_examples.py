import random
from re import M

#a = random.random()
#print(a)
#
#b = random.uniform(1, 10)
#print(b)
#
#c = random.randint(1, 10) # include upper bound
#print(c)
#
#d = random.randrange(1, 10) # exclude upper bound
#print(d)
#
#mu = 0 # mean
#sigma = 1 # std. deviation
#e = random.normalvariate(0, 1) # normal distribution 
#print(e)
#
#mylist = list('ABCDEFGH')
#print(mylist)
#
#rnd_element = random.choice(mylist)
#print(rnd_element)
#
#rnd_elements = random.sample(mylist, 3)
#print(rnd_elements)
#
#rnd_elements_multiple = random.choices(mylist, k=3) # This method allow to pick multiples times same element
#print(rnd_elements_multiple)
#
#mylist = list('ABCDEFGH')
#random.shuffle(mylist)
#print(mylist)

##############################################################
#import random
#random.seed(1)
#
#print(random.random())
#print(random.randint(1, 10))
#
#random.seed(2)
#
#print(random.random())
#print(random.randint(1, 10))
#
#random.seed(1)
#
#print(random.random())
#print(random.randint(1, 10))
#
#random.seed(2)
#
#print(random.random())
#print(random.randint(1, 10))

##############################################################
#import secrets
#
#a = secrets.randbelow(10)
#print(a)
#
#b = secrets.randbits(4)
#print(b)
#
#mylist = list('ABCDEFGH')
#c = secrets.choice(mylist)
#print(c)

##############################################################
import numpy as np

a = np.random.rand(3)
print(a)

b = np.random.rand(3,3)
print(b)

c = np.random.randint(0, 10, (3,4))
print(c)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

np.random.shuffle(arr) # shuffle = barajar/ aleatorizar 
print(arr)


np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

