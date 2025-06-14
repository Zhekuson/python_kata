SECRET = 'AABBBCDw2e3412'
class A:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
some_object = A(1, 2, 3)
user_input = input()
print(user_input.format(obj=some_object))
# {obj.__init__.__globals__[SECRET]}