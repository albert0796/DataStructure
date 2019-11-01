class Node(object):
    def __init__(self, value, left=None, right=None, parent=None):
        self.val = value
        self.left = left
        self.right = right
        self.parent = parent

class Tree(object):

    def __init__(self, root = None):
        self.root = root
        self.size=0
    
    def addAtroot(self,value,direction):
        if direction == 'right':
            node=Node(value)
            temp=self.root
            self.root=node
            node.right=temp
        elif direction == 'left':
            node=Node(value)
            temp=self.root
            self.root=node
            node.left=temp
    
    
            

t=Tree()
t.addAtroot(10,'right')
t.root.val





