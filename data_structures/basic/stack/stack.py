class Stack:
    def __init__(self):
        self._stack = []
        self.length = 0

    def peek(self):
        if self.length > 0:
            return self._stack[self.length - 1]
        else:
            return None

    def push(self, item):
        self._stack.append(item)
        self.length += 1

    def pop(self):
        item = self._stack[self.length - 1]
        self._stack.pop()
        self.length -= 1
        return item

    def __len__(self):
        return self.length
