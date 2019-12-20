from collections import defaultdict 

class Queue:  
    def __init__(self):
        self.stack_in=[]
        self.stack_out=[]
        
    def pop(self):
        if len(self.stack_out) > 0:
            return self.stack_out.pop()
        elif len(self.stack_in)==0:
            return
        else:
            while len(self.stack_in) > 0:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
        self.state1 = []
        self.state2 = []
        
    def addEdge(self,u,v): 
        self.graph[u].append(v) 

    def BFS(self, s, initialize=True):
        if initialize == True:
            self.state2.append(s)
        Q1 = Queue()
        Q1.stack_in = self.graph[s].copy()
        while True:
            v1=Q1.pop()
            if v1 not in self.state1 and v1 not in self.state2 and v1 != None:
                self.state1.append(v1)
            if len(Q1.stack_out) == 0:
                break
        Q2 = Queue()
        Q2.stack_in = self.state1.copy()
        v2 = Q2.pop()
        if len(self.state1) > 0:
            self.state1.remove(v2)
            self.state2.append(v2)
            return self.BFS(v2, initialize=False)
        elif len(self.state1) == 0:
            output=self.state2
            self.state2=[]
            return output
        
    def DFS(self, s, initialize=True):
        if initialize == True:
            self.state2.append(s)
        Q1 = Queue()
        Q1.stack_in = self.graph[s].copy()
        while True:
            v1=Q1.pop()
            if v1 not in self.state1 and v1 not in self.state2 and v1 != None:
                self.state1.append(v1)
            if len(Q1.stack_out) == 0:
                break
        if len(self.state1) > 0:
            v2 = self.state1.pop()
            self.state2.append(v2)
            return self.DFS(v2, initialize=False)
        if len(self.state1) == 0:
            output = self.state2
            self.state2 = []
            return output