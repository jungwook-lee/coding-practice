from tree import TreeNode, Tree

""" Check if two binary trees are identical or not.
    Assumptions:
        - two separate instances of binary trees
"""

# TODO:recursive
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

# TODO:iterative 
