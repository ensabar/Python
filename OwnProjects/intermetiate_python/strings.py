# Strings: ordered, immutable, text representation

from re import sub


my_string = 'Hello world'
print(my_string)

my_string = 'I\'m a programmer'
print(my_string)

my_string = """Its used for multiple lines of comments 
For example, its used for documentation
"""
print(my_string)

my_string = 'Hello world'

char = my_string[0]
print(char)

# Slicing 
substring = my_string[1:5]
print(substring)

substring = my_string[:5]
print(substring)


substring = my_string[2:]
print(substring)

substring = my_string[::2]
print(substring)

substring = my_string[::-1]
print(substring)

# Concatenating strings
greetin = 'Hello'
name = 'Tom'

sentence = greetin + ' ' + name
print(sentence)

# Iteration for string

for i in sentence:
    print(i)


# Check if a character is in string

if 'e' in greetin:
    print('yes')
else:
    print('no')

my_string = '     Hello world    '
print(my_string)

# Clear white spaces
my_string = my_string.strip()
print(my_string)

# Conver to uppercase
print(my_string.upper())

# Conver to lowercase
print(my_string.lower())

# Start with
print(my_string.startswith('World'))

# End with
print(my_string.endswith('World'))

# Index of
my_string = 'Hello World'
print(my_string.index('W'))

# find
my_string = 'Hello world'
print(my_string.find('l'))

# Count
print(my_string.count('p'))

# Replace
my_string = 'Hello World'
print(my_string.replace('World','Universe'))

# Lists and strings

my_string = 'how are you doing'
my_list = my_string.split()
print(my_list)

my_string = 'how,are,you,doing'
my_list = my_string.split(',')
print(my_list)

new_string = ' '.join(my_list)
print(new_string)

my_list = ['a']*6
print(my_list)

my_string = ''.join(my_list)
print(my_string)


from timeit import default_timer as timer
my_list = ['a']* 1000000

# bad code

start = timer()
my_string = ''
for i in my_list:
    my_string += i 
stop = timer()
print(stop - start)

# good code 

start = timer()
my_string = ''.join(my_list)
stop = timer()
print(stop - start)

# Fromat string
# %, .format(), f-strings
# %s for string~, %d for integer, 
# %f for float and 6 digits by default
# %.decimalsf for specific digits
var = 3.12362344523

my_string = 'the variable is %.5f' % var
print(my_string)

var = 3.12362344523
var2 = 6
# {:.2f} for 2 decimal digits
my_string = 'the variable is {:.2f} and {}' .format(var, var2)
print(my_string)

# f-String
my_string = f'the variable is {var*2} and {var2}'
print(my_string)



