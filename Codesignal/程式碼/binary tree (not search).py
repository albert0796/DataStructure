class Node:
    def __init__(self,val,depth):
        self.val=val
        self.depth=depth
        self.parent=None
        self.leftchild=None
        self.rightchild=None
        
    def insert(self,val,direction):
        if direction=='l':
            self.leftchild=Node(val,self.depth+1)
            self.leftchild.parent=self            
        elif direction=='r':
            self.rightchild=Node(val,self.depth+1)
            self.rightchild.parent=self
            
class Tree:
    def __init__(self,data):
        self.root=Node(data,1)
        self.s=[]
        
    def search(self,node,data):
        if node!=None:
            if node.val==data:
                self.s.append(node)
            self.search(node.leftchild,data)
            self.search(node.rightchild,data)
        if len(self.s)!=0:
            min_depth=999
            min_node=None
            for i in self.s:
                if i.depth <= min_depth:
                    min_depth=i.depth
                    min_node=i
            return min_node
        else:
            return 'the data is not in the tree'
        
    def replace(self,node,target,data):
        if node!=None:
            if node.val==target:
                node.val=data
            self.replace(node.leftchild,target,data)
            self.replace(node.rightchild,target,data)
    
    def delete(self,node,target):
        self.s=[]
        while self.search(node,target)!='the data is not in the tree':
            self.delete_once(node,target)
            self.s=[]
            
    def delete_once(self,node,target):
        if node!=None:
            if node.val==target:
                cur=node
                cur_parent=node.parent
                while cur.leftchild!=None or cur.rightchild!=None:
                    if cur.leftchild!=None:
                        cur_parent=cur
                        cur=cur.leftchild
                    elif cur.rightchild!=None:
                        cur_parent=cur
                        cur=cur.rightchild               
                if cur.parent==None:
                    cur.val=None
                else:
                    node.val=cur.val
                    if cur.parent.leftchild==cur:                                                                                                    
                        cur_parent.leftchild=None
                        cur.parent=None
                    elif cur.parent.rightchild==cur:                                                                                
                        cur_parent.rightchild=None
                        cur.parent=None
                      
            self.delete_once(node.leftchild,target)
            self.delete_once(node.rightchild,target)
        
            


    
        
            
T=Tree(1)
T.root.insert(2,'l')
T.root.insert(3,'r')
T.root.leftchild.insert(4,'l')
T.root.leftchild.insert(5,'r')

T.search(T.root,2).depth

T.replace(T.root,2,5)

T.delete_once(T.root,4)
T.search(T.root,4)
T.delete_once(T.root,2)
T.search(T.root,4).depth

T.delete(T.root,4)
T.search(T.root,4)

T=Tree(4)
T.root.insert(4,'l')
T.root.insert(4,'r')
T.root.leftchild.insert(4,'l')
T.root.leftchild.insert(4,'r')
T.delete(T.root,4)
T.search(T.root,4)











'''
T.search(T.root,4)
T.s

T.delete_once(T.root,4)
T.s=[]
T.search(T.root,4)
T.s

T.delete_once(T.root,4)
T.s=[]
T.search(T.root,4)
T.s

T.delete_once(T.root,4)
T.s=[]
T.search(T.root,4)
T.s
'''
'''
T.root.val
T.root.depth
T.root.leftchild.val
T.root.leftchild.depth
T.root.rightchild.val
T.root.rightchild.depth
T.root.leftchild.leftchild.val
T.root.leftchild.leftchild.depth
T.root.leftchild.rightchild.val
T.root.leftchild.rightchild.depth
'''

        
    
        
        