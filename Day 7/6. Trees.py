class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def add(self,data):
        if self.root is None:
            self.root = node(data)
        elif data < self.root:
            self.add(self.left)
            
            


t1 = Tree()
t1.root = node(20)
t1.left = node(10)
t1.right = node(30)
print(t1.root.data)
print(t1.left.data)
print(t1.right.data)