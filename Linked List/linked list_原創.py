'''
前題假設:
1. 不能有空的Node。
2. Node的val為int
'''

class Node(object):
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList(object):
    def __init__(self):
        self.head = None
        self.size=0
        
    def get(self, index: int):
        if index < 0 or index >= self.size:
            return 'The index is out of range.'
        cur = 0
        curnode = self.head
        while curnode != None:
            if index == cur :
                return curnode.val
            cur += 1 
            curnode = curnode.next
        
    def addAtHead(self,val: int):
        tmp=self.head
        self.head=Node(val)
        self.head.next=tmp
        self.size+=1
    
    def addAtTail(self,val: int):
        if self.head == None:
            self.head = Node(val)
            self.size+=1
            return
        curnode = self.head
        while curnode.next != None:
            curnode = curnode.next
        curnode.next = Node(val)
        self.size+=1

    def addAtIndex(self, index: int, val: int):        
        if index <= 0:
            self.addAtHead(val)
            return
        elif  index > self.size:
            return  'The index is out of range.'
        elif index <= self.size:
            i=0
            curnode=self.head
            pre=curnode
            while True:
                if i == index:
                    tmp=pre.next
                    pre.next=Node(val)
                    pre.next.next=tmp
                    self.size+=1
                    return
                pre=curnode
                curnode=curnode.next
                i+=1

    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            return  'The index is out of range.'       
        elif index==0:
            tmp=self.head.next
            self.head=tmp
            self.size-=1
            return          
        elif index < self.size:
            i=0
            curnode=self.head
            pre=curnode
            while curnode != None:
                if index==i:
                    pre.next=curnode.next
                    self.size-=1
                    return
                i+=1
                pre=curnode
                curnode=curnode.next

    def order(self):
        curnode = self.head
        while curnode!=None:
            print(curnode.val,end=' ')
            curnode = curnode.next
      
        
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
l.get(9) #10
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
l.size #12
l.deleteAtIndex(10)
l.order() #10 9 8 7 6 5 4 3 2 1 
l.size #10
l.deleteAtIndex(11) #The index is out of range.




            