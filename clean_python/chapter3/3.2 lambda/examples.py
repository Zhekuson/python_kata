add = lambda x, y: x + y
print(add(1, 2))

print((lambda x, y: x + y)(5, 3))

tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
print(sorted(tuples, key=lambda x: x[1]))