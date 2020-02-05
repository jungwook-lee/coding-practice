from collections import deque

# recursive solution
""" runtime O(n), space O(n) """
def getHeight(root):
    if not root:
        return 0
    return 1 + max(getHeight(root.left), getHeight(root.right))

# max height of the tree should be max height of stack
""" runtime O(n), space O(n) """
def getHeight_iter(root):
    if not root:
        return 0
    max_h = 0
    q = deque([])
    q.append(root)
    # perform a level order traversal
    while q:
        size = len(q)
        for _ in range(size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        max_h += 1
    return max_h
