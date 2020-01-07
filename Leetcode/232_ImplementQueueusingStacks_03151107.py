class MyQueue(object):
    
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
        
    def push(self,val):
        self.stack_in.append(val)
        
    def pop(self):
        if len(self.stack_out) > 0:
            tmp=self.stack_out.pop()
            return tmp
        elif len(self.stack_in)==0:
            return
        else:
            while len(self.stack_in) > 0:
                tmp=self.stack_in.pop()
                self.stack_out.append(tmp)
            tmp=self.stack_out.pop()
            return tmp
    
    def peek(self):
        if len(self.stack_out) > 0:
            return self.stack_out[-1]
        elif len(self.stack_in)==0:
            return
        else:
            return self.stack_in[0]
    
    def empty(self) -> bool:
        if len(self.stack_out) == 0 and len(self.stack_in) == 0:
            return True
        else:
            return False
        
        
        
Q = MyQueue()
Q.push(1)
Q.push(2)
Q.peek()






        
        
        
        
        