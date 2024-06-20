class Node:
    def __init__(self,data):
        self.value=data
        self.right=None
        self.left=None
class tree:
    def __init__(self):
        self.root=None
    def insert(self,root,value):
        if root is None:
            return Node(value)
        if value>root.value:
            root.right=self.insert(root.right,value)
        elif value<=root.value:
            root.left=self.insert(root.left,value)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.value,end=' ')
            self.inorder(root.right)
            return root
    def preorder(self,root):
        if root:
            print(root.value, end=' ')
            self.inorder(root.left)
            self.inorder(root.right)
            return root
    def postorder(self,root):
        if root:
            self.inorder(root.left)
            self.inorder(root.right)
            print(root.value, end=' ')
            return root

    def adding_of_all_nodes(self,root):
        if root == None:
            return 0
        return root.value + self.adding_of_all_nodes(root.left)+ self.adding_of_all_nodes(root.right)
    
    def add_even(self,root):
        if root == None:
            return 0
        if root.value % 2 == 0:
            return root.value + self.add_even(root.left)+ self.add_even(root.right)
        else:
            return self.add_even(root.left) + self.add_even(root.right)
    
    def add_odd(self,root):
        if root == None:
            return 0
        if root.value % 2 != 0:
            return root.value + self.add_odd(root.left)+ self.add_odd(root.right)
        else:
            return self.add_odd(root.left) + self.add_odd(root.right)
    
    def abs_esum_osum(self):
        print(abs(self.add_even(self.root) - self.add_odd(self.root)))
    
    def height_of_tree(self,root):
        if root == None:
            return -1
        return max(self.height_of_tree(root.left),self.height_of_tree(root.right)) +1 
    def bal(self,root):
        return abs(self.height_of_tree(root.left) - self.height_of_tree(root.right)) <= 1
    
    def no_of_leaf_nodes(self,root):
        if root == None:
            return 0
        if root.left is None and root.right is None:
            return 1   
        return self.no_of_leaf_nodes(root.left) + self.no_of_leaf_nodes(root.right)
    
    def sum_of_leaf_nodes(self,root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return root.value  
        else:
            return self.sum_of_leaf_nodes(root.left) + self.sum_of_leaf_nodes(root.right)
        
    def search(self, root, key):
        if root == None:
            return False
        if  root.value == key:
            return True
        if key < root.value:
            return self.search(root.left,key)
        else:
            return self.search(root.right, key)
        
    def depth(self,root, key,k):
        if root is None:
            return "No Element"
        if root.value == key:
            return k
        if key < root.value:
            return self.depth(root.left,key,k+1)
        else:
           return self.depth(root.right,key,k+1)
    
    def topview(self,root):
        if root == None:
            return
        d = {}
        l = []
        i = 0
        l.append([root,root.value,i])
        while len(l) > 0:
            k = l.pop(0)
            if k[2] not in d:
                d[k[2]] = k[1]
            if k[0].left is not None:
                l.append([k[0].left, k[0].left.value , k[2]-1])
            if k[0].right is not None:
                l.append([k[0].right, k[0].right.value , k[2]+1])
        print((list(d.values()).sort()))
    

        
    

    def leftview(self,root,c,l1):
        if root == None:
            return 
        if c not in l1 :
            print(root.value,end=" ")
            l1.append(c)
        self.leftview(root.left,c+1,l1)
        self.leftview(root.right,c+1,l1)

        

t=tree()
# print(t.root)
t.root=t.insert(t.root,10)
t.insert(t.root,5)
t.insert(t.root,20)
t.insert(t.root,2)
t.insert(t.root,7)
# t.inorder(t.root)
# print()
# t.preorder(t.root)
# print()
# t.postorder(t.root)
# print()

# print(t.adding_of_all_nodes(t.root))
# print(t.add_even(t.root))
# print(t.add_odd(t.root))
# t.abs_esum_osum()

# print(t.height_of_tree(t.root))

# if t.bal(t.root):
#     print("Balanced")
# else:
#     print("Not Balanced")

# print(t.no_of_leaf_nodes(t.root))
# print(t.sum_of_leaf_nodes(t.root))
# print("search = ", t.search(t.root,7))
# print(t.depth(t.root , 890 , 0))

# t.topview(t.root)

# t.leftview(t.root, 0, [])
t.topview(t.root)
