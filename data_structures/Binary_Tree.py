## Binary Tree ✔

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    #Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left == None:
                    self.lef = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data 

    #Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

root = Node(12)
root.insert(14)
root.insert(34)
root.insert(54)
root.insert(4)
root.insert(1)
root.insert(1)

root.PrintTree()



    