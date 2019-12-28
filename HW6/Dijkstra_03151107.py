class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        
        self.graph = [[None for column in range(vertices)] for row in range(vertices)] 
        self.outcome = dict()
        self.finished = [False] * vertices
        
        self.graph2 = []
        self.outcome2 = dict()
        self.dj = dict()
        
    def addEdge(self,u,v,w): 
        self.graph2.append((w, u, v))
        
        if u not in self.dj.keys():
            self.dj[u] = u
            
        if v not in self.dj.keys():
            self.dj[v] = v
        
    def Dijkstra(self, s, initialize = True): 
        if initialize == True:
            
            for i, j in zip(range(self.V), self.graph[s]):
                self.outcome[str(i)] = j
                
            self.finished[s] = True
        
        else:
            
            base = self.outcome[str(s)]
            
            for i in range(self.V):
                if s != i and self.graph[s][i] != 0:
                    d = base + self.graph[s][i]
                    
                    if self.outcome[str(i)] == 0 and self.finished[i] == False:
                        self.outcome[str(i)] = d
                        
                    elif self.outcome[str(i)] != 0 and d < self.outcome[str(i)]:
                        self.outcome[str(i)] = d      
                        
            self.finished[s] = True
            
        if False in self.finished:
            order = sorted(self.outcome.items(), key = lambda item:item[1])
            target = None
            
            for i in order:
                if self.finished[int(i[0])] == False and i[1] != 0:
                    target = int(i[0])
                    break
                
            return self.Dijkstra(target, initialize = False)
        
        else:
            return self.outcome
    
    def Kruskal(self):
        self.graph2 = sorted(self.graph2, key = lambda item:item[0])
        
        for edge in self.graph2:
            w, s, d = edge[0], edge[1], edge[2]
            
            if self.dj[d] != self.dj[s]:
                tmp = self.dj[d]
                self.dj[d] = self.dj[s]
                
                for point in self.dj.keys():
                    if self.dj[point] == tmp:
                       self.dj[point] = self.dj[s]
                       
                key = str(s) + '-' + str(d)
                self.outcome2[key] = w
                
            if len(self.outcome2) == self.V - 1:
                break
        
        return self.outcome2

'''
g = Graph(9)
g.addEdge(7,6,1)
g.addEdge(8,2,2)
g.addEdge(6,5,2)
g.addEdge(0,1,4)
g.addEdge(2,5,4)
g.addEdge(8,6,6)
g.addEdge(2,3,7)
g.addEdge(7,8,7)
g.addEdge(0,7,8)
g.addEdge(1,2,8)
g.addEdge(3,4,9)
g.addEdge(5,4,10)
g.addEdge(1,7,11)
g.addEdge(3,5,14)
g.graph2
g.dj  
print(g.Kruskal())

g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
           [4,0,8,0,0,0,0,11,0],
           [0,8,0,7,0,4,0,0,2],
           [0,0,7,0,9,14,0,0,0],
           [0,0,0,9,0,10,0,0,0],
           [0,0,4,14,10,0,2,0,0],
           [0,0,0,0,0,2,0,1,6],
           [8,11,0,0,0,0,1,0,7],
           [0,0,2,0,0,0,6,7,0]]
print(g.Dijkstra(0))
'''
        
        
        
        
        
        
        