def greet(name):
    return 'Hello, ' + name + '!'

print(greet.__code__.co_code)
print(greet.__code__.co_consts)
print(greet.__code__.co_varnames)

import dis
print(dis.dis(greet))

