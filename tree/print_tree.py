# Simple recursive inorder print
def print_preorder(root):
    """ returns values of given tree as list """
    if not root:
        return []
    def convert(root, out):
        if not root:
            return
        out.append(root.val)
        if root.left:
            convert(root.left, out)
        if root.right:
            convert(root.right, out)
        return out
    return convert(root, [])

# Inorder method with stack
def print_inorder_iter(root):
    cur, stack, out = root, [], []
    while True:
        # while the left node exists keep pushing
        while cur:
            stack.append(cur)
            cur = cur.left
        if not stack:
            break
        # Once no more left, pop one out
        node = stack.pop()
        # Print value
        out.append(node.val)
        # push the right node value if one exists
        cur = node.right
    return out

# Preorder method with stack
def print_preorder_iter(root):
    cur, stack = root, []
    while True:
        print(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        if not stack:
            break
        cur = stack.pop()

