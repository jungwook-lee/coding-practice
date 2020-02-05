from collections import deque
from tree import build_tree

# Iteratvie implementation of level order travel
""" Runtime of O(n), Space of O(n) """
def levelOrderTraverse(root):
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

if __name__ == '__main__':
    test_in = build_tree([1,2,3,4,5])
    levelOrderTraverse(test_in)
