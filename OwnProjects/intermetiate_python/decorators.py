# Function decorators / Class decorators

#def start_end_decorator(func):
#
#    def wrapper():
#        print('Start')
#        func()
#        print('Stop')
#    return wrapper
#
#@start_end_decorator
#def print_name():
#    print('Alex')
#
#print_name()

#######################################################################
# If our function have arguments
#import functools
#def my_decorator(func):
#
#    @functools.wraps(func) # Preserve the name of the original function
#    def wrapper(*args, **kwargs):
#        # Do something before...
#        result = func(*args, **kwargs)
#        # Do something after... 
#        return result
#    return wrapper
#
#@my_decorator
#def add5(x):
#    return x + 5
#
#result = add5(10)
#print(result)
#
## Function identity
#print(help(add5))
#print(add5.__name__)

#######################################################################
#import functools
#
#def repeat(num_times):
#
#    def decorator_repeat(func):
#        @functools.wraps(func)
#        def wrapper(*args, **kwargs):
#            for _ in range(num_times):
#                result = func(*args, **kwargs)   
#            return result
#        return wrapper
#    return decorator_repeat             
#
#@repeat(num_times=3)
#def greet(name):
#    print(f'Hello {name}')
#
#greet('Alex')

#######################################################################
# Nested function decorators
#import functools
#
#def start_end_decorator(func):
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs):
#        print('Start')
#        result = func(*args, **kwargs)
#        print('Stop')
#        return result
#    return wrapper
#
#def debug(func):
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs):
#        args_repr = [repr(a) for a in args]
#        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
#        signature = ",".join(args_repr + kwargs_repr)
#        print(f'Calling {func.__name__}({signature})')
#        result = func(*args, **kwargs)
#        print(f'{func.__name__} returned {result!r}')
#        return result
#    return wrapper
#
#@debug
#@start_end_decorator
#def say_hello(name):
#    greeting = f'Hello {name}'
#    print(greeting)
#    return greeting
#
#say_hello('Alex')

#######################################################################
# Class decorators
class CountCalls:
    def __init__(self, func):
        self.func = func
        self._num_calls = 0
    
    def __call__(self, *args, **kwargs):
        self._num_calls += 1
        print(f'This is executed {self._num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()





