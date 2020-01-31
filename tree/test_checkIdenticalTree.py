import unittest

from tree import TreeNode, build_tree
from checkIdenticalTree import checkIdenticalTree

class CheckIdenticalTreeTestCase(unittest.TestCase):
    def test_identical_tree(self):
        test_in = [1,2,3,4,5]
        t1 = build_tree(test_in)
        t2 = build_tree(test_in)
        self.assertTrue(checkIdenticalTree(t1, t2))

    def test_not_same_tree(self):
        test_in = [1,2,3,4,5]
        t1 = build_tree(test_in)
        t2 = build_tree([1])
        self.assertFalse(checkIdenticalTree(t1, t2))

    def test_empty_trees(self):
        t1 = build_tree([])
        t2 = build_tree([])
        self.assertTrue(checkIdenticalTree(t1, t2))

if __name__ == '__main__':
    unittest.main()
