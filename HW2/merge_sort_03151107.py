class Solution:
    def Check(self,data):
        import numpy as np
        t=np.array(data)
        if len(t.shape)==1:
            return True
        elif len(t.shape)==2:
            return False 
    
    def Sup(self,data):
        n=len(data)
        k=0
        base=1
        while base < n:
            base=base*2
            k+=1
        num_dummy=2**k-n
        if num_dummy!=0:
            self.dummy=max(data)+1
            #dummy=9999
            data_dummy=data+[self.dummy]*num_dummy
            return data_dummy
        else:  
            self.dummy=None
            return data
    
    def Convert(self,data):
        L=[]
        for i in data:
            e=[i]
            L.append(e)
        return L
    
    def Merge(self,d1,d2):
        D=[]
        i=0
        j=0
        while i<len(d1) and j<len(d2):
            if d1[i] < d2[j]:
                D.append(d1[i])
                i+=1
            else:
                D.append(d2[j])
                j+=1        
        while i<len(d1):
            D.append(d1[i])
            i+=1
        while j<len(d2):
            D.append(d2[j])
            j+=1    
        return D    
    
    def merge_sort(self,data):
        if self.Check(data)==True:
            if len(data)==0:
                return 'no element in the list'
            if len(data)==1:
                return data
            data_dummy = self.Sup(data)
            data = self.Convert(data_dummy)    
        if self.Check(data)==False:
            if len(data)==1:
                data_final=data[0]
                while self.dummy in data_final:
                    data_final.remove(self.dummy)
                return data_final           
        begin = 0
        end = len(data)
        D=[]
        for i in range(begin,end,2):
            d1,d2=data[i],data[i+1]
            D.append(self.Merge(d1,d2))
        return self.merge_sort(D)

'''
data=[6,5,4,3,2,1]
data=[5,4,3,2,1]
data=[4,3,2,1]
data=[1]
data=[]
data=[-1,-2,-3]
Solution().merge_sort(data)
'''


