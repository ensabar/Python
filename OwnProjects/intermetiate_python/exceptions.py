# Error and exceptions

# Forcing an exception
from email import message
from multiprocessing.sharedctypes import Value
from typing import Type


#x = -5
#if x < 0:
#    raise Exception('x should be greater than zero.')

# Assert statement
#assert(x>=0), 'x is not positive'

# Handle exceptions
#try:
#    a = 5 / 0
#    b = a + 4
#except ZeroDivisionError as e:
#    print(e)
#except TypeError as e:
#    print(e)
#else:
#    print('everything is fine')
#finally:
#    print('cleaning up...')

# Define our own exceptions
class ValueTooHighError(Exception):
    pass
class ValuetooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value


def test_value(x):
    if x > 100:
        raise ValueTooHighError('Value is too high')
    if x < 5:
        raise ValuetooSmallError('Value is too small',x)




try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValuetooSmallError as e:
    print(e.message,e.value)
