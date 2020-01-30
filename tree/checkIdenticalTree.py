from tree import TreeNode, Tree

""" Check if two binary trees are identical or not.
    Assumptions:
        - two separate instances of binary trees
"""
# Runtime O(nodes), Space O(nodes)
def checkIdenticalTree(t1, t2):
    if not t1 and not t2:
        return True
    elif (not t1) ^ (not t2):
        return False
    elif t1.val == t2.val:
        return checkIdenticalTree(t1.left, t2.left) and \
               checkIdenticalTree(t1.right, t2.right)
    else:
        return False

# TODO:iterative, no stack ("Morris Traversal")
# def print_preorder(t1, t2):
#     # how to traverse iteratively?
#     while t1:
#         while t1:
#             t1 = t1.left
#         # print left value
#         print(t1.val)
#         if t1.right:
#             t1 = t1.right

# TODO: iterative with extra memory (stack)
def print_inorder(t1):
    cur, stack = t1, []
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
        print(node.val)
        # push the right node value if one exists
        cur = node.right

