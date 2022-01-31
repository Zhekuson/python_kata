import unittest

from data_structures.basic.linked_list.linked_list import LinkedList


class TestLinkedList(unittest.TestCase):
    def test_something(self):
        list = LinkedList()
        list.insert(0, 1)
        print(list)

    def test_insert_many_values(self):
        list = LinkedList()
        list.insert(0, 1)
        list.insert(0, 1)
        list.insert(0, 1)
        list.insert(0, 1)
        list.insert(1, 4)
        print(list)

    def test_delete_many_values(self):
        list = LinkedList()
        list.insert(0, 1)
        list.insert(1, 7)
        list.insert(0, 2)
        list.insert(0, 1)
        list.insert(1, 4)
        print('initial')
        print(list)
        list.remove_at(0)
        print('delete at 0')
        print(list)

        list.remove_at(3)
        print('delete at 3')
        print(list)

if __name__ == '__main__':
    unittest.main()
