class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
    
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
    def add(self, key):
        key_num, index = self.hash(key)
        if self.data[index]==None:
            self.data[index]=ListNode(None)
        node = self.data[index]
        if node.val==None:
            node.val=key_num
        else:
            curnode = node
            while curnode.next != None:
                curnode = curnode.next
            curnode.next = ListNode(key_num)
        
    def remove(self, key):
        key_num, index = self.hash(key)
        if self.data[index]==None:
            return
        node = self.data[index]        
        while self.searchValue(key_num,node)==True:
            if node.val==key_num:
                if node.next==None:
                    self.data[index]=None
                    return
                else:
                    node.val=node.next.val
                    node.next=node.next.next  
            else:
                pre=node
                curnode=node
                while curnode!=None:
                    if curnode.val==key_num:
                        pre.next=curnode.next
                        break
                    pre=curnode
                    curnode=curnode.next
        
    def contains(self, key):
        key_num, index = self.hash(key)
        if self.data[index]==None:
            return False
        node = self.data[index]
        outcome=self.searchValue(key_num,node)
        return outcome
        
    def hash(self,key):
        from Cryptodome.Hash import MD5 
        h = int(MD5.new(key.encode('utf-8')).hexdigest(),16)
        index = h % self.capacity
        return h,index
        
    def orderAll(self):
        for i,j in zip(self.data,range(0, self.capacity)):
            print(j,end=' ')
            self.order(i)
        
    def searchValue(self,key,node):
        curnode=node
        while curnode!=None:
            if curnode.val==key:
                return True
            curnode=curnode.next
        return False
        
    def order(self,node):
        curnode = node
        while curnode!=None:
            print(curnode.val,end=' ')
            curnode = curnode.next
        print('\n')
        






    