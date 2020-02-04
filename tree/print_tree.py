# Simple recursive print
def print_recursive(root, order="pre"):
    if not root:
        return []
    if not order in ["pre", "post", "in"]:
        raise ValueError("Invalid tree order method")
    def convert(root, out):
        if not root:
            return
        if order == "pre":
            out.append(root.val)
        convert(root.left, out)
        if order == "in":
            out.append(root.val)
        convert(root.right, out)
        if order == "post":
            out.append(root.val)
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
    if not root:
        return []
    cur, stack, out = root, [], []
    while True:
        out.append(cur.val)
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
        if not stack:
            break
        cur = stack.pop()
    return out

# TODO: Postorder method with stack
""" Leetcode [Hard] Problem, revisit """
def print_postorder_iter(root):
    if not root:
        return []
    cur, stack, out = root, [], []
    while True:
        while cur:
            stack.append(cur)
            if cur.right:
                stack.append(cur.right)
            cur = cur.left
        if not stack:
            break
        node = stack.pop()
        out.append(node.val)
        cur = node
