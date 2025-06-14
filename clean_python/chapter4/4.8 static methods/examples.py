class MyClass:
    def methodA(self):
        return 'instance method', self
    @classmethod
    def methodB(cls):
        return 'class method', cls
    @staticmethod
    def methodC():
        return 'static method'

print(MyClass().methodA())
print(MyClass().methodB())
print(MyClass().methodC())

class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
    def __repr__(self):
        return f'Pizza({self.ingredients!r})'
    @classmethod
    def margherita(cls):
        return cls(['mozarella', 'tomatoes'])
    @classmethod
    def prosciutto(cls):
        return cls(['mozarella', 'tomatoes', 'ham'])