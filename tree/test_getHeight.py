import unittest
from tree import build_tree
from getHeight import getHeight, getHeight_iter

class GetHeightTestCase(unittest.TestCase):
    def test_empty_tree(self):
        test_in = build_tree([])
        self.assertEqual(getHeight(test_in), 0)
        self.assertEqual(getHeight_iter(test_in), 0)

    def test_skewed_tree(self):
        test_in = build_tree([1, 2, None, 4, None, None, None, 8])
        self.assertEqual(getHeight(test_in), 4)
        self.assertEqual(getHeight_iter(test_in), 4)

        test_in = build_tree([1, None, 3, None, None, None, 7])
        self.assertEqual(getHeight(test_in), 3)
        self.assertEqual(getHeight_iter(test_in), 3)

    def test_complete_tree(self):
        test_in = build_tree([1, 2, 3, 4, 5])
        self.assertEqual(getHeight(test_in), 3)
        self.assertEqual(getHeight_iter(test_in), 3)
