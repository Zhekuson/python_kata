with open('hello.txt', 'w') as f:
    f.write('HW')
""""""
class ManagedFile:
    """
        __enter__, __exit__
    """
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        self.file = open(self.name, 'w')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('hello.txt') as f:
    f.write('AAAA')
    f.write('End')


""""""
from contextlib import contextmanager
@contextmanager
def managed_file(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_file('hello.txt') as f:
    f.write('AAAA')
    f.write('BBBB')

