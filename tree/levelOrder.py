from collections import deque
from tree import build_tree

# Iterative implementation of level order travel
""" Runtime of O(n), Space of O(n) """
def levelOrderTraverse_iter(root):
    if not root:
        return None
    q = deque([])
    q.append(root)
    while q:
        node = q.popleft()
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Recursive implementation of level order traversal
""" Runtime O(n^2)"""
def printLevel(root, level):
    if not root:
        return False
    if level == 1:
        print (root.val)
        return True
    l_bool = printLevel(root.left, level - 1)
    r_bool = printLevel(root.right, level - 1)
    return l_bool or r_bool

def levelOrderTraverse(root):
    if not root:
        return
    level = 1
    while printLevel(root, level):
        level += 1

# TODO: Implement hashing version


# TODO: Write tests
if __name__ == '__main__':
    test_in = build_tree([1,2,3,4,5])
    levelOrderTraverse(test_in)
    levelOrderTraverse_iter(test_in)
