import unittest

from tree import TreeNode, Tree
from checkIdenticalTree import checkIdenticalTree

class CheckIdenticalTreeTestCase(unittest.TestCase):
    def test_identical_tree(self):
        test_in = [1,2,3,4,5]
        t1 = Tree(test_in)
        t2 = Tree(test_in)
        self.assertTrue(checkIdenticalTree(t1.head, t2.head))

    def test_not_same_tree(self):
        test_in = [1,2,3,4,5]
        t1 = Tree(test_in)
        t2 = Tree([1])
        self.assertFalse(checkIdenticalTree(t1.head, t2.head))

    def test_empty_trees(self):
        t1 = Tree([])
        t2 = Tree([])
        self.assertTrue(checkIdenticalTree(t1.head, t2.head))

if __name__ == '__main__':
    unittest.main()
