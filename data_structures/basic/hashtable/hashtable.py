
class HashTable:
    def __init__(self, hash_func=None):
        self.hash_func = hash_func if hash_func is not None else self.__hash__
        self.total_elements = 0

    def insert(self, key, value):

