import unittest 
from tree import TreeNode, Tree

class TreeNodeTestCase(unittest.TestCase):
    def test_default_init(self):
        new_node = TreeNode(0)
        self.assertEqual(new_node.val, 0)

    def test_print_node(self):
        new_node = TreeNode(0)
        self.assertEqual(str(new_node), "<TreeNode 0>")

class TreeTestCase(unittest.TestCase):
    def test_init(self):
        test_in = [0]
        tree = Tree(test_in)
        self.assertEqual(tree.head.val, 0)

        test_in = [0, 1, 2]
        tree = Tree(test_in)
        self.assertEqual(tree.head.val, 0)
        self.assertEqual(tree.head.left.val, 1)
        self.assertEqual(tree.head.right.val, 2)

    # TODO: Write tests for printing trees!

if __name__ == '__main__':
    unittest.main()
