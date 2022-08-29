# Dictionaries: Collection of Key-value pais, unordered, mutable

from msilib.schema import MsiDigitalCertificate


mydict = {
    'name': 'Max',
    'age': 29,
    'city': 'New York'
}
print(mydict)

mydict2 = dict(name = 'Mary', age = 23, city= 'Boston')
print(mydict2)
#Access to the values
print(mydict['name'])

# Add a key-value to a dict

mydict['email'] = 'max@xaxa.com'
print(mydict)

# Delete items
del mydict['name']
print(mydict)

mydict.pop('age')
print(mydict)

mydict.popitem() # remove last par key-value
print(mydict)

# Check if a key is in dictionary

if 'name' in mydict:
    print(mydict['name'])
else:
    print('jejej')

try:
    mydict(mydict['name'])
except:
    print('Error')

# Loop through a dictionari
mydict = {
    'name': 'Max',
    'age': 29,
    'city': 'New York'
}
for key in mydict.keys(): # return a list with all keys from list
    print(key)

for key in mydict.values(): # return a list with all keys from list
    print(key)
print('Complete loop')
for key, value in mydict.items(): # return a list with all keys from list
    print(key, value)

# Copying a dictionary
mydict = {
    'name': 'Max',
    'age': 29,
    'city': 'New York'
}

mydict_cpy = mydict

mydict_cpy['email'] = 'MAx@xyz.com'

print(mydict)
print(mydict_cpy)


mydict = {
    'name': 'Max',
    'age': 29,
    'city': 'New York'
}
mydict_cpy = mydict.copy()

mydict_cpy['email'] = 'MAx@xyz.com'
print(mydict)
print(mydict_cpy)

mydict = {
    'name': 'Max',
    'age': 29,
    'city': 'New York'
}
mydict_cpy = dict(mydict)

mydict_cpy['email'] = 'MAx@xyz.com'
print(mydict)
print(mydict_cpy)

# Merge two dictionaries
print('Merge two dictionaries')
mydict = {
    'name': 'Max',
    'age': 29,
    'city': 'New York',
    'email': 'max@xyz.com'
}
mydict2 = dict(name = 'Mary', age = 23, city= 'Boston')

mydict.update(mydict2)
print(mydict)

# Posible key types

mydict =  {
    3: 9,
    6: 36,
    9: 81
}
print(mydict)

print(mydict[3])

# tuple as a key
mytuple = (8,7)
mydict = {mytuple: 15}
print(mydict)




