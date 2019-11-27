'''
Queue: FIFO 先進先出。
Stack: LIFO 後進先出。只需用append、pop即可完成下面指令。
'''

class Queue(object):
    
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
        self.size=0
        
    def push(self,val):
        self.stack_in.append(val)
        self.size+=1
        
    def pop(self):
        if len(self.stack_out) > 0:
            tmp=self.stack_out.pop()
            self.size-=1
            return tmp
        elif len(self.stack_in)==0:
            return 'The Queue is empty.'
        else:
            while len(self.stack_in) > 0:
                tmp=self.stack_in.pop()
                self.stack_out.append(tmp)
            tmp=self.stack_out.pop()
            self.size-=1
            return tmp
    
    def peek(self):
        if len(self.stack_out) > 0:
            return self.stack_out[-1]
        elif len(self.stack_in)==0:
            return 'The Queue is empty.'
        else:
            return self.stack_in[0]
    
    def isEmpty(self):
        if self.size==0:
            return True
        else:
            return False
    
    def order(self):
        if self.isEmpty()==True:
            return 'The Queue is empty.'
        else:
            for i in self.stack_out[::-1]:
                print(i,end=' ')
            for i in self.stack_in:
                print(i,end=' ')

Q=Queue()
for i in [1,2,3,4]:
    Q.push(i)
Q.order() #1 2 3 4 
Q.stack_in #[1, 2, 3, 4]
Q.stack_out #[]
Q.size #4

Q.pop() #1
Q.order() #2 3 4
Q.stack_in #[]
Q.stack_out #[4, 3, 2]
Q.size #3

Q.peek() #2

Q.isEmpty() #The Queue is empty.

while Q.size > 0:
    Q.pop()
Q.order() #'The Queue is empty.'
Q.stack_in #[]
Q.stack_out #[]
Q.size #0


        
        
        
        
        
        
        
        
        
        
    
    