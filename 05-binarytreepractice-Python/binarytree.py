class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        if self.root:
            if type(self.root.value) != type(find_val):
                return False
            if self.root.value == find_val:
                return True
        currentNode = self.root
        while currentNode != None:
            result = self.preorder_search(currentNode, find_val)
            if result == True:
                return True
            currentNode = result
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        if self.root:
            print(self.root.value)
            self.preorder_print(self.root, self.root.left)
            self.preorder_print(self.root, self.root.right)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        # Your code goes here
        if type(start.value) != type(find_val):
            return None
        if start.value == find_val:
            return True
        elif start.value > find_val:
            return start.right
        else:
            return start.left

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        # Your code goes here
        if traversal is not None:
            print(traversal.value)
            self.preorder_print(traversal, traversal.left)
            self.preorder_print(traversal, traversal.right)
