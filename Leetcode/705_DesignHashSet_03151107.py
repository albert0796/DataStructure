class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
    
    def addAtTail(self,val):
        if self.head == None:
            self.head = ListNode(val)
            return
        curnode = self.head
        while curnode.next != None:
            curnode = curnode.next
        curnode.next = ListNode(val)
    
    def deleteValue(self,val):
        while self.searchValue(val)==True:
            if self.head.val==val:
                tmp=self.head.next
                self.head=tmp
            else:
                pre=self.head
                curnode=self.head
                while curnode!=None:
                    if curnode.val==val:
                        pre.next=curnode.next
                        break
                    pre=curnode
                    curnode=curnode.next              

    def searchValue(self,val):
        curnode=self.head
        while curnode!=None:
            if curnode.val==val:
                return True
            curnode=curnode.next
        return False

class MyHashSet:
    def __init__(self, capacity=1000):
        self.capacity = capacity
        self.data = [MyLinkedList() for x in range(0, capacity)] 

    def add(self, key):
        index = self.hash(key)
        linkedlist = self.data[index]
        linkedlist.addAtTail(key)
        
    def remove(self, key):
        index = self.hash(key)
        linkedlist = self.data[index]
        linkedlist.deleteValue(key)
               
    def contains(self, key):
        index = self.hash(key)
        linkedlist = self.data[index]
        outcome=linkedlist.searchValue(key)
        return outcome
    
    def hash(self,key):
        index = key % self.capacity
        return index
    
    
    
    
    
    