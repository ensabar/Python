# Lists: ordered, mutable, allow duplicate elements

from traceback import print_exc


mylist = ['banana', 'cherry', 'apple']

print(mylist)

# Allow different data types

mylist2 = [5, True, 'apple', 'apple']
print(mylist2[0]) # first item
print(mylist2[-1]) # last item

for i in mylist2:
    print(i)

# check if there is an item in your list

if 'banana' in mylist:
    print('banana is in our list')
else:
    print ('no')

# append elements to a list
mylist.append('lemon')
print(mylist)

# append in specific position
mylist.insert(1, 'blueberry')
print(mylist)

# remove last item from a list
mylist.pop()
print(mylist)

# remove specific element
mylist.remove('cherry')
print(mylist)

# clear the list
mylist.clear()
print(mylist)

mylist = ['banana', 'cherry', 'apple']

# reverse items

mylist.reverse()
print(mylist)

# ordering a list
mylist = [5, 1, -4, 9 , 0]
mylist.sort() # sorted(mylist)
print(mylist)

# creates a new with list same elements
mylist = [0] * 5
print(mylist)

mylist2 = [1, 2, 3, 4, 5]

new_list = mylist + mylist2
print(new_list)

# slicing
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]
b = mylist[:5]
c = mylist[2:]
print(mylist)
print(a)
print(b)
print(c)

d = mylist[::2]
print(d)
e = mylist[::-1]
print(e)

# Copying lists
list_org = ['banana', 'cherry', 'apple']
# with this assgiment both lists reference to same memory position
list_cpy = list_org

list_cpy.append('lemon')
print(list_org)
print(list_cpy)

# 3 ways to copy properly a list
list_cpy = list_org.copy()
list_cpy = list(list_org)
list_cpy = list_org[:]

# List comprehension. Create an new list from an existing list

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
b = [i*i for i in mylist]
print(mylist)
print(b)

