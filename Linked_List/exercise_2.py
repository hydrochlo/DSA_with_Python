# Implement doubly linked list
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_the_beginning(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None, None)
            self.head = node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
    
        itr.next = Node(data, None, itr)
    
    def print_forward(self):
        if self.head is None:
            print("No elements in the LinkedList to print")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + " -> "
            itr = itr.next

        print(llstr)
        
    def print_backward(self):
        if self.head is None:
            print("No elements in the LinkedList to print")
            return
        
        llstr = ''
        x = self.head
        while x.next: 
            x = x.next
        
        while x:
            llstr += str(x.data) + " -> "
            x = x.prev
        print(llstr)
        
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_the_beginning(10)
    ll.insert_at_the_beginning(20)
    ll.insert_at_the_beginning(30)
    ll.insert_at_end(300)
    ll.insert_at_end(305)
    ll.insert_at_end(56)
    ll.print_forward()
    ll.print_backward()