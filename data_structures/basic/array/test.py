import unittest

from data_structures.basic.array.array import StaticArray


class ArrayTest(unittest.TestCase):
    def setUp(self) -> None:
        self.N = 10
        self.arr = StaticArray(self.N)
        for i in range(self.N):
            self.arr[i] = i

    def test_len(self):
        self.assertEqual(len(self.arr), self.N)

    def test_assigning(self):
        self.assertEqual(self.arr[9], 9)
        self.arr[5] = 888
        self.assertEqual(888, self.arr[5])


if __name__ == '__main__':
    unittest.main()
