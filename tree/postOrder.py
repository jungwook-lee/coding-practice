from tree import TreeNode, build_tree

# recursive version
def postOrder_r(root):
    if root is None:
        return
    postOrder_r(root.left)
    postOrder_r(root.right)
    print(root.val)

# come back later
# iterative version
def postOrder_i(root):
    if root is None:
        return
    stack, retList = [root], []
    while len(stack) != 0:
        while stack[-1].left:
            stack.append(stack[-1].left)
        # retList.append(stack[-1])
        print(stack[-1].val)
        stack.pop()
        if stack[-1].right:
            stack.append(stack[-1].right)


if __name__ == '__main__':
    tree = build_tree([1, 2, 3, 4, 5])
    postOrder_r(tree)
    postOrder_i(tree)
