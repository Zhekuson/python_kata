def yell(text):
    return text.upper() + '!'

bark = yell
print(bark("AAA"))
del yell
print(bark.__name__)

# qualname since 3.3
class C:
    def f():
        pass
    class D:
        def g():
            pass
print(C.__qualname__)
print(C.f.__qualname__)
print(C.D.__qualname__)
print(C.D.g.__qualname__)

print(list(map(bark, ['a', 'b', 'c'])))


class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, x):
        return self.n + x

print(Adder(2)(3))
print(callable(Adder))


