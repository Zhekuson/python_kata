import unittest

from data_structures.basic.queue.queue import Queue


class TestQueue(unittest.TestCase):
    def test_add(self):
        q = Queue()
        q.enqueue(0)
        q.enqueue(1)
        q.enqueue(2)
        print('initial')
        print(q)
        self.assertEqual(q.dequeue(), 0)
        print('removed 0')
        print(q)


if __name__ == '__main__':
    unittest.main()
