class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Dll:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_last(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newnode = Node(data)
            self.tail.next = newnode
            newnode.prev = self.tail
            self.tail = newnode

    def add_first(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            newnode = Node(data)
            self.head.prev = newnode
            newnode.next = self.head
            self.head = newnode

    def add_middle(self,data,pos):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            temp = self.head
            newnode = Node(data)
            while temp is not None and pos-1 != 0:
                pos -= 1
                temp = temp.next
            newnode.next = temp.next
            temp.next.prev = newnode
            temp.next = newnode
            newnode.prev = temp


    def print(self):
        temp = self.head
        print(None,end = " <-> ")
        while(temp != None):
            print(temp.data, end=" <-> ")
            temp = temp.next
        print(None)

    def printrev(self):
        temp = self.tail
        print(None,end = " <-> ")
        while(temp != None):
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print(None)




    def search(self,key):
        temp1 = self.head
        temp2 = self.tail
        k=0
        while temp1.prev != temp2 :
            if temp1.data == key or temp2.data == key :  #or temp1.next.data == key
                print("Element found", k)
                return
            else:
                temp1 = temp1.next
                temp2 = temp2.prev
        print("element not found",k)
    



    def even_odd(self):
        temp1 = self.head
        temp2 = self.tail
        while True:
            if temp1 == temp2:
                print("ODD LIST!!")
                return
            elif temp1.prev == temp2:
                print("EVEN LIST!!")
                return
            temp1 = temp1.next
            temp2 = temp2.prev




    def palindrome(self):
        temp1 = self.head
        temp2 = self.tail
        flag = 0
        while temp1 != temp2 and temp1 != temp2.next:
            print(temp1.data)
            print(temp2.data)
            if temp1.data == temp2.data :
                flag = 1
            else:
                flag = 0
                return "Not Palindrome"
            temp1 = temp1.next
            temp2 = temp2.prev

        if flag == 1:
            return "Palindrome"
        
    
    def half(self):
        temp1 = self.head
        temp2 = self.tail
        while temp1.next != temp2:
            temp1 = temp1.next
            temp2 = temp2.prev
        
        self.tail.next = self.head
        self.head.prev = self.tail
        temp1.next, temp2.prev = None, None
        self.tail = temp1 
        self.head = temp2 

    def changepairs(self):
        temp = self.head
        ref = None
        h = None
        while(temp.next.next):
            temp1 = temp.next
            temp2 = temp.next.next
            temp1.next = temp
            temp.prev = temp1
            temp.next = temp2
            temp2.prev = temp
            temp = temp2
            ref = temp.prev
            ref.next = temp
    def balanced_parenthesis(self):
        d={')':'(','}':'{',']':'['}
        l1=[]
        current=self.head
        k=0
        while(current):
            if(current.data not in d):
                k+=1
                l1.append(current.data)
                current=current.next
            else:
                if d[current.data]==l1[len(l1)-1]:
                    k+=1
                    l1.pop()
                else:
                    return k+1
                current=current.next
        if(len(l1)==0):
            return -1
        else:
            return k
        
    def evenoddsumdiff(self,temp,sum):
        if temp == None:
            return sum 
        if temp.data%2 == 0:
            sum += temp.data
        else:
            sum -= temp.data
        return self.evenoddsumdiff(temp.next,sum)
            
    def count_primes(self,temp, c):
        if temp== None:
            return c
        def primeornot(s,n,c1)

l1 = Dll()
l2 = Dll()
l1.add_last(5)
l1.add_last(7)
l1.add_last(8)
l1.add_last(2)
l1.add_last(1)
# l1.add_last(4)
#l1.add_last(15)
# l1.add_last(20)



l1.print()
# l1.printrev()

# l1.search(20)
l1.even_odd()
print(l1.palindrome())

# l1.half()
l1.print()


l2.add_last('{')
l2.add_last('(')
l2.add_last('[')
l2.add_last(']')
l2.add_last(')')
l2.add_last('}')

print(l2.balanced_parenthesis())
l2.print()
# l1.changepairs()
# l1.print()
# 10 20 30 40


temp = l1.head
print(abs(l1.evenoddsumdiff(temp,0)))


