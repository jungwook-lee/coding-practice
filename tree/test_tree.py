import unittest 
from tree import TreeNode, build_tree

class TreeNodeTestCase(unittest.TestCase):
    def test_default_init(self):
        new_node = build_tree([0])
        self.assertEqual(new_node.val, 0)

    def test_print_node(self):
        new_node = build_tree([0])
        self.assertEqual(str(new_node), "<TreeNode 0>")

class TreeTestCase(unittest.TestCase):
    def test_build_tree(self):
        root = build_tree([0])
        self.assertEqual(root.val, 0)

        root = build_tree([0,1,2])
        self.assertEqual(root.val, 0)
        self.assertEqual(root.left.val, 1)
        self.assertEqual(root.right.val, 2)

    def test_invalid_builds(self):
        # Note, raises need to be catched in a wrapper
        with self.assertRaises(TypeError): build_tree({})
        with self.assertRaises(TypeError): build_tree(0)

if __name__ == '__main__':
    unittest.main()
