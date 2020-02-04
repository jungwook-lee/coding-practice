from tree import TreeNode, build_tree

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

# Runtime O(n) and O(n)
def checkIdenticalTree_iter(t1, t2):
    cur1, cur2, stack1, stack2 = t1, t2, [], []
    while True:
        while cur1 and cur2:
            stack1.append(cur1)
            stack2.append(cur2)
            cur1 = cur1.left
            cur2 = cur2.left
            # note that ^ operator don't support []
            if (not cur1)^(not cur2):
                return False
        if not stack1 and not stack2:
            return True
        elif (not stack1) ^ (not stack2):
            return False
        else:
            node1 = stack1.pop()
            node2 = stack2.pop()
        if node1.val != node2.val:
            return False
        cur1 = node1.right
        cur2 = node2.right
