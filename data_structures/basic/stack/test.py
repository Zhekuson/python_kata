import unittest

from data_structures.basic.stack.stack import Stack


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack1 = Stack()
        self.stack1.push(1)
        self.stack1.push(2)

    def test_init(self):
        stack = Stack()

    def test_push(self):
        self.stack1.push(3)

    def test_peek(self):
        self.assertEquals(self.stack1.peek(), 2)

    def test_pop(self):
        self.stack1.pop()
        self.assertEquals(self.stack1.peek(), 1)


if __name__ == '__main__':
    unittest.main()
