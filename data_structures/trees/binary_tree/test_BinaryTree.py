from unittest import TestCase

from data_structures.trees.binary_tree.BinaryTree import BinaryTree


class TestBinaryTree(TestCase):

    def test_something(self):
        tree = BinaryTree(1)
        tree.insert(2)
        tree.insert(4)
        tree.insert(3)
        tree.insert(3)
        tree.insert(0)
        tree.insert(1000)
        print(tree.get_depth())
        tree.print()

    pass
