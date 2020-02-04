import unittest

from tree import TreeNode, build_tree
from print_tree import print_recursive, print_inorder_iter, print_preorder_iter

class PrintTestCase(unittest.TestCase):
    def test_print_recursive(self):
        root = build_tree([])
        self.assertEqual(print_recursive(root), [])

        root = build_tree([1,2,3,4,5,6,7])
        exp = [1,2,4,5,3,6,7]
        self.assertEqual(print_recursive(root, order="pre"), exp)

        root = build_tree([1,2,3,4,5,6,7])
        exp = [4,2,5,1,6,3,7]
        self.assertEqual(print_recursive(root, order="in"), exp)

        root = build_tree([1,2,3,4,5,6,7])
        exp = [4,5,2,6,7,3,1]
        self.assertEqual(print_recursive(root, order="post"), exp)

    def test_print_preorder_iter(self):
        root = build_tree([])
        self.assertEqual(print_preorder_iter(root), [])

        root = build_tree([1,2,3,4,5,6,7])
        exp = [1,2,4,5,3,6,7]
        self.assertEqual(print_preorder_iter(root), exp)

    def test_print_inorder_iter(self):
        root = build_tree([])
        self.assertEqual(print_inorder_iter(root), [])

        root = build_tree([1,2,3,4,5,6,7])
        exp = [4,2,5,1,6,3,7]
        self.assertEqual(print_inorder_iter(root), exp)

#    def test_print_postorder_iter(self):
#        root = build_tree([])
#        self.assertEqual(print_postorder_iter(root), [])
#
#        root = build_tree([1,2,3,4,5,6,7])
#        exp = [4,5,2,6,7,3,1]
#        self.assertEqual(print_postorder_iter(root), exp)


