class Node():

    def __init__(self, value):

        self.left = None
        self.right = None
        self.value = value
    
    def add_child(self, value):
# Compare the new value with the parent node
        if self.value:
            if value < self.value:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.add_child(value)
            elif value > self.value:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.add_child(value)
        else:
            self.value = value
    
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.value),
        if self.right:
            self.right.PrintTree()

root = Node(9)
root.add_child(1)
root.add_child(2)
root.add_child(3)

root.PrintTree()