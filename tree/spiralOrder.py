from collections import deque, defaultdict

# Recursive version of spiral order traversal
""" Runtime O(n^2) """
def spiralOrderTraverse(root):
    if not root:
        return
    level = 1
    swap = False
    while printLevel(root, level, swap):
        level += 1
        # swap print order
        if swap:
            swap = False
        else:
            swap = True

def printLevel(root, level, swap):
    if not root:
        return 
    if level == 1:
        print (root.val)
        return True

    if swap:
        l_bool = printLevel(root.right, level - 1, swap)
        r_bool = printLevel(root.left, level - 1, swap)
    else:
        l_bool = printLevel(root.left, level - 1, swap)
        r_bool = printLevel(root.right, level - 1, swap)

    return l_bool or r_bool

# Iterative version
""" Runtime O(n), Space O(n) """
def spiralOrderTraverse_iter(root):
    if not root:
        return
    # First write a regular level order traversal
    q = deque([])
    q.append(root)
    even = True
    while q:
        size = len(q)
        while even and size > 0:
            node = q.popleft()
            print(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            size -= 1
        while not even and size > 0:
            node = q.pop()
            print(node.val)
            if node.right:
                q.appendleft(node.right)
            if node.left:
                q.appendleft(node.left)
            size -= 1

        even = not even

# Hashing version
""" Runtime O(n), Space O(n) """
def spiralOrderTraverse_hash(root):
    # declare memory
    mem = defaultdict(list)
    
    def store_tree(root, level, mem):
        if not root:
            return
        mem[level].append(root.val)
        store_tree(root.left, level + 1, mem)
        store_tree(root.right, level + 1, mem)

    store_tree(root, 1, mem)
    # print the tree in reverse
    for key, val in mem.items():
        if (key % 2):
            val = reversed(val)
        for num in val:
            print(num)

# TODO: Write tests
if __name__ == '__main__':
    from tree import build_tree
    test_in = build_tree([1,2,3,4,5,6,7])
    spiralOrderTraverse(test_in)
    spiralOrderTraverse_iter(test_in)
    spiralOrderTraverse_hash(test_in)

