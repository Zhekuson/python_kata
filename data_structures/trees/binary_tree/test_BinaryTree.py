from unittest import TestCase

from data_structures.trees.binary_tree.BinaryTree import BinaryTree


class TestBinaryTree(TestCase):

    def setUp(self) -> None:
        self.arr = ['F', 'B', 'G', 'I', 'H', 'D', 'E', 'C', 'A']
        tree = BinaryTree('F')
        self.arr.remove('F')
        for item in self.arr:
            tree.insert(item)
        tree.print()
        self.tree = tree

    def test_simple(self):
        assert self.tree.get_min() == min(self.arr)
        assert self.tree.get_max() == max(self.arr)

    def test_traversals(self):
        print('NLR', self.tree.pre_order())
        print('LNR', self.tree.in_order())
        print('LRN', self.tree.post_order())

    pass
