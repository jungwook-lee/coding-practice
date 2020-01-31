# TODO: Implement feature to print "inorder", "preorder", "postorder"
def print_tree(self):
    """ Simple In-order Print of a Tree object """
    if self.head is None:
        print ("Tree is empty!")
        
    def print_h(head):
        if head is None:
            print('None')
        else:
            print(head)
            print_h(head.left)
            print_h(head.right)

    return print_h(self.head)

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
