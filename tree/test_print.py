import unittest

from tree import TreeNode, build_tree
from print_tree import print_preorder, print_inorder_iter

class PrintTestCase(unittest.TestCase):
    def test_print_preorder(self):
        root = build_tree([])
        self.assertEqual(print_preorder(root), [])

        root = build_tree([1,2,3,4,5,6,7])
        exp = [1,2,4,5,3,6,7]
        self.assertEqual(print_preorder(root), exp)

    def test_print_inorder_iter(self):
        root = build_tree([])
        self.assertEqual(print_inorder_iter(root), [])

        root = build_tree([1,2,3,4,5,6,7])
        exp = [4,2,5,1,6,3,7]
        self.assertEqual(print_inorder_iter(root), exp)

