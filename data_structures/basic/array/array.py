class StaticArray:
    def __init__(self, length):
        self._arr = [0] * length

    def __getitem__(self, item):
        return self._arr[item]

    def __len__(self):
        return len(self._arr)

    def __setitem__(self, key, value):
        self._arr[key] = value

    def __iter__(self):
        return self._arr.__iter__()

    def __contains__(self, item):
        return item in self._arr
