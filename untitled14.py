class Node(object):
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class MyLinkedList(object):

    def __init__(self, head = None):
        self.head = head
        self.size=0
        
    def get(self, index):
        cur = 0
        cur_node = self.head
        nexxt_node = cur_node.next
        while cur_node != None:
            if index == cur :
                node = cur_node
                return node.data
            cur += 1 
            cur_node = nexxt_node    
        return -1
        
    def addAtHead(self,data):
        if data is None:
            return None
        node = Node(data,self.head)
        self.head = node
        self.size+=1
        return node
    
    def addAtTail(self,data):
        if data is None:
            return None
        
        node = Node(data)
        if self.head is None:
            self.head = node
            self.size+=1
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        self.size+=1
        return node
        
    def addAtIndex(self, index: int, data: int):
        
        if index <= 0:
            self.addAtHead(data)
            return

        elif index <= self.size:
            i=0
            curNode=self.head
            pre=curNode
            while True:
                if i == index:
                    pre.next=Node(data,curNode)
                    self.size+=1
                    return
                pre=curNode
                curNode=curNode.next
                i+=1
       
    def deleteAtIndex(self, index: int):
        if index < 0:
            return 
        
        elif index==0:
            if self.head==None:
                return
            tmp=self.head
            self.head=self.head.next
            tmp.next=None
            self.size-=1
            
        elif index < self.size:
            i=0
            curNode=self.head
            pre=curNode
            while curNode is not None:
                if index==i:
                    pre.next=curNode.next
                    curNode.next=None
                    self.size-=1
                    return
                i+=1
                pre=curNode
                curNode=curNode.next





l=MyLinkedList()
l.addAtHead(1)
l.addAtHead(2)
l.addAtTail(3)
l.addAtTail(4)
