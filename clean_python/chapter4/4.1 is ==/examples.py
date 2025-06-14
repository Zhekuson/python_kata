a = [1, 2, 3]
b = [4, 5, 6]
c = [1, 2, 3]
d = a

# == by value, is by reference
print(f"a == b: {a == b}")
print(f"a == c: {a == c}")
print(f"a is c: {a is c}")
print(f"a is d: {a is d}")
print(f"a == d: {a == d}")