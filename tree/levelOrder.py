from collections import deque, defaultdict
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

# Hashing version of level order traversal
""" Runtime O(n), Space O(n)
    - Need to visit every node
    - Need to store every node """
def levelOrderTraverse_hash(root):
    mem = defaultdict(list)

    def store_tree(root, level, mem):
        # preorder traversal to store tree to mem
        if not root:
            return

        # store value at the given level
        mem[level].append(root.val)
        store_tree(root.left, level + 1, mem)
        store_tree(root.right, level + 1, mem)

    # Traverse here
    store_tree(root, 1, mem)

    # Iterate and print all nodes between given levels
    for _, val in mem.items():
        # use comprehension to print efficiently
        # out_str = " ".join([str(num) for num in val])
        for num in val:
            print(num)


# TODO: Write tests
if __name__ == '__main__':
    test_in = build_tree([1,2,3,4,5])
    levelOrderTraverse(test_in)
    levelOrderTraverse_iter(test_in)
    levelOrderTraverse_hash(test_in)
