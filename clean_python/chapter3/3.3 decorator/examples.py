def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.upper()
        return modified_result
    return wrapper

def lowercase(func):
    def wrapper():
        original_result = func()
        modified_result = original_result.lower()
        return modified_result
    return wrapper

# from bottom to top
@uppercase
@lowercase
def greet():
    return 'Hello, world!'
print(greet())

# args kwargs
import functools
def uppercase(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(some_string):
    """Some doc"""
    return f'Hi! {some_string}'
print(greet("Name"))
print(greet.__doc__)