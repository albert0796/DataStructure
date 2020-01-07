class Node(object):
    
    def __init__(self, val):
        
        self.val = val
        self.next =None

class MyLinkedList(object):
    
    def __init__(self):
        
        self.head = None
        self.size = 0
    
    def addAtHead(self, val):

        tmp = self.head
        self.head = Node(val)
        self.head.next = tmp
        self.size += 1
    
    def addAtTail(self, val):
        
        if self.head == None:
            self.head = Node(val)
            self.size += 1
        
        else:
            curNode = self.head
            
            while curNode.next != None:
                curNode = curNode.next
            
            curNode.next = Node(val)
            self.size += 1
            
    def get(self, index):
        
        if index < 0 or index >= self.size:
            return -1
        
        else:
            curNode = self.head
            tier = 0
            
            while curNode != None:
                
                if tier == index:
                    return curNode.val
                
                curNode = curNode.next
                tier += 1
                  
            return -1
    
    def addAtIndex(self, index, val):
        
        if index < 0 or index > self.size:
            return -1

        elif index == 0:
            self.addAtHead(val)
        
        else:
            preNode = self.head
            curNode = self.head.next
            tier = 1
            
            while True:
                
                if tier == index:
                    tmp = curNode
                    preNode.next = Node(val)
                    preNode.next.next = tmp
                    self.size += 1
                    return 
                
                preNode = curNode
                curNode = curNode.next
                tier += 1
            
    def deleteAtIndex(self, index):
        
        if index < 0 or index >= self.size:
            return -1
        
        elif index == 0:
            tmp = self.head.next
            self.head = tmp
            self.size -= 1
        
        else:
            preNode = self.head
            curNode = self.head.next
            tier = 1
            
            while True:
                
                if tier == index:
                    tmp = curNode.next
                    preNode.next = tmp
                    self.size -= 1
                    return
        
                preNode = curNode
                curNode = curNode.next
                tier += 1
                
k=MyLinkedList()
for i in [1,2,3,4,5,6,7,8,9,10]:
    k.addAtTail(i)
k.order() #1 2 3 4 5 6 7 8 9 10 
k.size #10

l=MyLinkedList()
for i in [1,2,3,4,5,6,7,8,9,10]:
    l.addAtHead(i)
l.order() #10 9 8 7 6 5 4 3 2 1 
l.size #10

l.get(0) #10
l.get(4) #6
l.get(9) #1
l.get(-1) #The index is out of range.
l.get(10) #The index is out of range.

l.addAtIndex(0,11)
l.get(0) #11
l.order() #11 10 9 8 7 6 5 4 3 2 1
l.size #11
l.addAtIndex(5,100)
l.get(5) #100
l.order() #11 10 9 8 7 100 6 5 4 3 2 1 
l.size #12
l.addAtIndex(12,300)
l.get(12) #300
l.order() #11 10 9 8 7 100 6 5 4 3 2 1 300 
l.size #13
l.addAtIndex(14,10000) #The index is out of range.

l.deleteAtIndex(0) #10 9 8 7 100 6 5 4 3 2 1 300 
l.order() #10 9 8 7 100 6 5 4 3 2 1 300 
l.size #12
l.deleteAtIndex(4)
l.order() #10 9 8 7 6 5 4 3 2 1 300 
l.size #11
l.deleteAtIndex(10)
l.order() #10 9 8 7 6 5 4 3 2 1 
l.size #10
l.deleteAtIndex(11) #The index is out of range.            
        
















               
                
                