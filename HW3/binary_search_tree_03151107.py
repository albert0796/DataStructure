class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution(object): 
    def __init__(self):
        self.r=[]
        self.h=[]
        self.m=[]
    
    def insert(self,root,val):
        cur=None
        if root.val==None:
            root.val=val
        else:
            if root!=None:
                if val <= root.val:
                    if root.left==None:
                        root.left=TreeNode(val)
                        return root.left
                    else:
                        root=root.left
                        cur=self.insert(root,val)
                        
                elif val > root.val:
                    if root.right==None:
                        root.right=TreeNode(val)
                        return root.right
                    else:
                        root=root.right
                        cur=self.insert(root,val)
        return cur
                        
    def search(self,root,target):
        cur=None
        if root!=None:            
            if root.val==None:
                return None
            if target==root.val:
                return root
            else:   
                if target < root.val:
                    root=root.left
                    cur=self.search(root,target)
                elif target > root.val:
                    root=root.right
                    cur=self.search(root,target)
        else:
            return None
        return cur
        
    def delete(self,root,target):
        import copy
        root_original=copy.deepcopy(root)
        while self.search(root,target) != None:
            self.delete_once(root,target)
        if self.max_height(root) > self.max_height(root_original):
            self.rebuild(root,root_original)
        return root
    
    def delete_once(self,root,target):
        pre_cur=root
        cur=root
        while cur!=None:        
           if cur.val!=target:
                pre_cur=cur
                if cur.val >= target:
                    cur=cur.left
                elif cur.val < target:
                    cur=cur.right
           else:
               break
        if cur==None:
            return       
        if cur.left==None and cur.right==None:
            if pre_cur.left==None and pre_cur.right==None:
                cur.val=None
            else:
                if pre_cur.left==cur:
                    pre_cur.left=None
                elif pre_cur.right==cur:
                    pre_cur.right=None                   
        elif cur.left==None or cur.right==None:
            if cur.left!=None:
                cur.val=cur.left.val                        
                cur.right=cur.left.right  #注意順序
                cur.left=cur.left.left                                                                                                                                                 
            elif cur.right!=None:
                cur.val=cur.right.val
                cur.left=cur.right.left  #注意順序
                cur.right=cur.right.right                        
        elif cur.left!=None and cur.right!=None:
            cur2=cur
            cur2=cur.right                    
            if cur2.left==None:
                cur.val=cur2.val
                cur.right=cur2.right
            else:     
                while cur2.left != None:
                    cur2=cur2.left
                cur2.left=cur.left
                cur.val=cur.right.val
                cur.left=cur.right.left  #注意順序
                cur.right=cur.right.right
            
    def rebuild(self,root,root_original):
        if root.val==None:
            return
        if self.max_height(root) <= 2:
            return
        HH=self.max_height(root_original)
        l=self.pop(root)
        l_m=self.median(l)        
        performance_median=False
        n=TreeNode(l_m[0])                
        for i in l_m[1::]:
            self.insert(n,i)
        h=self.max_height(n)
        if h <= HH:
            L=l_m
            performance_median=True            
        if performance_median==False:            
            H=999
            L=None
            for k in range(20):
                l=self.sampling(l)
                n=TreeNode(l[0])
                for i in l[1:]:
                    self.insert(n,i)
                h=self.max_height(n)
                if h <= HH:
                    L=l
                    break
                if h <= H:
                    H=h
                    L=l
        for i in l:
            self.delete_once(root,i)
        for i in L:
            self.insert(root,i)    
        return root
              
    def modify(self,root,target,new_val):
        if root.val==None:
            return
        HH=self.max_height(root)
        ll=self.pop(root)
        l=self.replace(target,new_val,ll)
        l_m=self.median(l)
        performance_median=False
        n=TreeNode(l_m[0])                
        for i in l_m[1::]:
            self.insert(n,i)
        h=self.max_height(n)
        if h <= HH:
            L=l_m
            performance_median=True            
        if performance_median==False:            
            H=999
            L=None
            for k in range(20):
                l=self.sampling(l)
                n=TreeNode(l[0])
                for i in l[1:]:
                    self.insert(n,i)
                h=self.max_height(n)
                if h <= HH:
                    L=l
                    break
                if h <= H:
                    H=h
                    L=l
        for i in ll:
            self.delete_once(root,i)
        for i in L:
            self.insert(root,i)    
        return root
                   
    def max_height(self,root):
        num=0
        self.count_height(root,num)
        maximum=max(self.h)
        self.h=[]
        return maximum
               
    def count_height(self,root,num):
        if root!=None:
            num+=1
            self.count_height(root.left,num)
            self.count_height(root.right,num)
        else:
            self.h.append(num)    
    
    def pop(self,root):
        if root!=None:
            self.r.append(root.val)
            self.pop(root.left)
            self.pop(root.right)
        ll=self.r
        return ll
    
    def replace(self,target,new_val,ll):
        self.r=[]
        l=[]
        for i in range(len(ll)):
            if ll[i]==target:
                l.append(new_val)
            else:
                l.append(ll[i])
        return l
    
    def median(self,ary):
        self.pop_median(ary)
        ary_median=self.m
        self.r=[]
        self.m=[]
        ary=sorted(ary)
        ary_median.append(ary[0])
        return ary_median
    
    def pop_median(self,ary):
        ary=sorted(ary)
        length=len(ary)
        if length > 1:
            base = length // 2
            self.m.append(ary[base])
            left=ary[:base]
            right=ary[base:]
            self.pop_median(left)
            self.pop_median(right)
            
    def sampling(self,l):
        import random
        return random.sample(l,len(l))      
    
    def pre_order(self,root):
        if root!=None:
            print(root.val,'',end='')
            self.pre_order(root.left)
            self.pre_order(root.right)
