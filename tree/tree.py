class TreeNode(object):
    def __repr__(self):
        return "<TreeNode {}>".format(self.val)

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree(arr):
    if not isinstance(arr, list):
        raise TypeError('build_tree only takes in lists')

    def build(i, arr):
        # Exit when list is too big
        if i >= len(arr):
            return None
        if arr[i] is None:
            return None

        # Add the new node
        new_node = TreeNode(arr[i])
        # Insert insert left, right
        new_node.left = build((i * 2) + 1, arr)
        new_node.right = build((i * 2) + 2, arr)
        return new_node

    return build(0, arr)
