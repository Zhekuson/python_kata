class A:
    def __init__(self, x):
        self._var = x # private variable
    def get_me_var(self):
        return self._var + 1


# private functions
def external_func():
    return 23
def _internal_func():
    return 42
"""
>>> from my_module import *
>>> external_func()
23
>>> _internal_func() NameError: "name '_internal_func' is not defined"
"""

class Test:
    def __init__(self):
        self.foo = 11
        self._bar = 23
        self.__baz = 23 # hidden
t = Test()
print(dir(t))
"""
['_Test__baz', '__class__', ...
"""
