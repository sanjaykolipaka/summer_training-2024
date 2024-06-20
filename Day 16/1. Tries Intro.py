# n = int(input("No of Queries: "))
# l = []
# while n > 0:
#     k = int(input("Enter Number : "))
#     s = input("String : ")
#     if k == 1:
#         if s not in l:
#             l.append(s)
#     elif k == 2:
#         print(s in l)
#     elif k == 4:
#         l.remove(s)
#     else:
#         flag = 0
#         for i in l:
#             if (s in i and i.index(s) == 0):
#                 flag += 1
#         print(flag)

#     n -= 1
# print(l)


class Node:
    def __init__(self):
        self.d = {}
        self.flag = 0

class Trie:
    def __init__(self):
        self.root = Node()
        
    def add(self, str):
        t = self.root
        for i in str:
            if i not in t.d:
                t.d[i] = Node()
            t = t.d[i]
        t.flag = 1
        
    def search(self, str):
        t = self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        return t.flag == 1
        
    def prefix_search(self, str):
        t = self.root
        for i in str:
            if i not in t.d:
                return False
            t = t.d[i]
        return True
        
    def print_with_prefix(self, str):
        def helper(t, s):
            if t.flag == 1:
                print(s)
                
            for i in t.d:
                helper(t.d[i], s + i)
                
        t = self.root
        s = ""
        for i in str:
            if i in t.d:
                s += i
                t = t.d[i]
            else:
                print("No such Prefix !!")
                return
        helper(t, s)

# Example usage
t1 = Trie()
t1.add("world")
t1.add("word")
t1.add("apple")
t1.add("woo")
t1.add("w")
t1.add("wor")
t1.print_with_prefix("wor")