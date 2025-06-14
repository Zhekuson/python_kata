print({True: 'yes', 1: 'no', 1.0: 'perhaps'})
# {True: 'perhaps'}

a = 10
b = a
print(a is b)
b = 11
print(a is b)
print(a, b)