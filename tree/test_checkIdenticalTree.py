import unittest

from tree import TreeNode, build_tree
from checkIdenticalTree import checkIdenticalTree, checkIdenticalTree_iter

class CheckIdenticalTreeTestCase(unittest.TestCase):
    def test_identical_tree(self):
        test_in = [1,2,3,4,5]
        t1 = build_tree(test_in)
        t2 = build_tree(test_in)
        self.assertTrue(checkIdenticalTree(t1, t2))
        self.assertTrue(checkIdenticalTree_iter(t1, t2))

    def test_not_same_tree(self):
        test_in = [1,2,3,4,5]
        t1 = build_tree(test_in)
        t2 = build_tree([1])
        self.assertFalse(checkIdenticalTree(t1, t2))
        self.assertFalse(checkIdenticalTree_iter(t1, t2))

        # Flip input trees
        test_in = [1,2,3,4,5]
        t2 = build_tree(test_in)
        t1 = build_tree([1])
        self.assertFalse(checkIdenticalTree(t1, t2))
        self.assertFalse(checkIdenticalTree_iter(t1, t2))

    def test_empty_trees(self):
        t1 = build_tree([])
        t2 = build_tree([])
        self.assertTrue(checkIdenticalTree(t1, t2))
        self.assertTrue(checkIdenticalTree_iter(t1, t2))

    def test_check_iter(self):
        t1 = build_tree([1,2,3,4])
        t2 = build_tree([1,2,3,4])
        self.assertTrue(checkIdenticalTree(t1, t2))

        t1 = build_tree([1,2,3,1])
        t2 = build_tree([1,2,3,4])
        self.assertFalse(checkIdenticalTree(t1, t2))

if __name__ == '__main__':
    unittest.main()
