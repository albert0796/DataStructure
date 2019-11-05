class Solution(object):
    def heap_sort(self,data):
        if len(data)==0:
            return 'no element in the list'
        dummy=min(data)-1
        data=[dummy]+data
        D=[]
        self.Tree(data)
        self.Pop(data,D)
        while len(data) > 1:
            self.DeleteMin(data)
            self.Pop(data,D)
        return D
                
    def Tree(self,data):
        p=0
        for i in data[1:]:
            p+=1
            index=p
            element=i
            while data[index//2] > element:
                data[index]=data[index//2]
                index=index//2
            data[index]=element
        return data
    
    def DeleteMin(self,data):
        last=len(data)-1
        element=data[1]
        index_root=1
        index_c=index_root*2
        while index_c <= last:
            if index_c < last:
                if data[index_c] > data[index_c+1]:
                    index_c=index_c+1
            if element > data[index_c]:
                data[index_root]=data[index_c]
                index_root=index_c
                index_c=index_c*2
            else:
                break
        data[index_root]=element
        return data
    
    def Pop(self,data,D):
        data[1],data[-1]=data[-1],data[1]
        k=data.pop(-1)
        D.append(k)
        return D
'''   
data= [8,7,6,5,4,3,2,1]
Solution().heap_sort(data)
data= [-7,6,-5,4,-3,2,1]
Solution().heap_sort(data)
data= [2,2,4,4,-3,2,1]
Solution().heap_sort(data)
data=[1]
Solution().heap_sort(data)
data=[]
Solution().heap_sort(data)
data= [6,5,4,3,2,1]
Solution().heap_sort(data)
data= [2,1]
Solution().heap_sort(data)
'''

