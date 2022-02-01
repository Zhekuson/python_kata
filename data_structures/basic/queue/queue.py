class Queue:
    def __init__(self):
        self._q = []

    def enqueue(self, item):
        self._q.insert(0, item)

    def dequeue(self):
        return self._q.pop()

    def __str__(self):
        return str(self._q)
