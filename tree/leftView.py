from collections import defaultdict
from tree import build_tree

def leftView(root):
    # Strategy: store level order, print first item in each level
    mem = defaultdict(list)
    
    def store_tree(root, level, mem):
        if not root:
            return
        mem[level].append(root.val)
        store_tree(root.left, level+1, mem)
        store_tree(root.right, level+1, mem)

    store_tree(root, 1, mem)
    for _, val in mem.items():
        print(val[0])


def leftView_recur(root):
    # Strategy: have flag for last level to be printed, while preorder traversal
    if not root:
        return
    # pass in a mutable object
    last = [0]
    def printFirstInLevel(root, level, last):
        if not root:
            return False
        if last[0] < level:
            print(root.val)
            last[0] = level
        printFirstInLevel(root.left, level+1, last)
        printFirstInLevel(root.right, level+1, last)

    printFirstInLevel(root, 1, last)

if __name__ == '__main__':
   test_in = build_tree([1,2,3,None,4,5,6,None,None,None,None,None,7,8])
   leftView(test_in)
   leftView_recur(test_in)


