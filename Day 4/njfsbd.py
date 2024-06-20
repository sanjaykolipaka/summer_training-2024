class node:
    def __init__(self,u):
        self.data = u 
        self.next = None

class sll:
    def __init__(self) :
        self.head = None

    def add_at_end(self,data):
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = node(data)

    
    def display(self):
        temp = self.head
        while temp is not None :
            print(temp.data, end = "->")
            temp = temp.next
        print(None)

    def search(self,key):
        temp = self.head
        while temp is not None:
            if temp.data == key:
                return ("Element Found!!")
            else:
                temp = temp.next
        return "Element Not Found"
    
    def mid_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        print("Middle Element = ", slow.data)

    def even_odd(self):
        fast = self.head
        c = 0
        while fast is not None and fast.next is not None:
            fast = fast.next.next
        if fast == None:
            print("Even")
        else:
            print("Odd")

    def max_sequence(self):
        temp = self.head
        c = 1
        maxlen = 1
        while temp.next is not None:
            if temp.data + 1  == temp.next.data:
                c += 1
            else:
                c = 1
            temp = temp.next
            maxlen = max(maxlen,c)   
        print(maxlen)
    

    def printpairs(self):
        temp = self.head
        while temp.next is not None:
            temp1 = self.head.next
            while temp1 is not None:
                print(temp.data,temp1.data)
                temp1 = temp1.next
            temp = temp.next

    def bubble_sort(self):
        if self.head is None:
            return
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            while current.next is not None:
                next_node = current.next
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                    swapped = True
                current = next_node

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev


    def del_last(self,key):
        temp = self.head
        while temp.next and temp.next.next:
            if temp.next.data == key:
                temp.next = temp.next.next
            temp = temp.next
        

    def fun(self):
        temp = dummy = self.head
        whi

    
l1 = sll()
l2 = sll()


l2.head = node(500)
l1.head = node(1)


l1.add_at_end(2)
l1.add_at_end(3)
l1.add_at_end(4)
l1.add_at_end(6)
l1.add_at_end(7)
l1.add_at_end(8)
l1.add_at_end(9)
l1.add_at_end(10)


l2.add_at_end(300)
l2.add_at_end(200)
l2.add_at_end(400)
l2.add_at_end(100)

l1.display()
l2.display()

l1.display()

print(l1.search(50))
l2.mid_node()

l1.even_odd()
l2.even_odd()

l1.max_sequence()
l1.printpairs()

l2.bubble_sort()
l2.display()

l2.reverse()
l2.display()

l2.del_last(300)
l2.display()


