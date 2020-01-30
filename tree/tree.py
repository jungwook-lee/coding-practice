class TreeNode(object):
    def __repr__(self):
        return "<TreeNode {}>".format(self.val)

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    def __repr__(self):
        return "<Tree {}>".format(id(self.head))

    def __init__(self, x):
        """ Construct a tree from a heap """
        if not isinstance(x, list):
            raise TypeError('must be a list')
        self.head = self.__build(0, x)

    def __build(self, i, x):
        # Exit when list is too big
        if i >= len(x):
            return None
        if x[i] is None:
            return None
        # Add the new node
        new_node = TreeNode(x[i])
        # Insert insert left, right
        new_node.left = self.__build((i*2)+1, x)
        new_node.right = self.__build((i*2)+2, x)
        return new_node

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


