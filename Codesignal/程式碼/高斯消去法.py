import numpy as np

def argumented(A, b):
    return np.c_[A,b]

def swaprows(A, i, j):
    A = A
    A[[i,j]] = A[[j,i]]
    return A

def multiplying(A,i,j):
    A[i]=A[i]/A[i,j]
    return A

def rowoperation(A,i,k,j):
    A[j]=A[j]+A[i]*k
    return A

A = np.mat([[1., 2., -4., -4.],
            [2., 4., 0., 0.],
            [2., 3., 2., 1.],
            [-1., 1., 3., 6.]])
    
b = np.mat([[5.],
            [2.],
            [5.],
            [5.]])
    
mat=argumented(A,b)
#row=mat.shape[0]
#columns=mat.shape[1]

multiplying(mat,0,0)
rowoperation(mat,0,-2,1)
rowoperation(mat,0,-2,2)
rowoperation(mat,0,1,3)

swaprows(mat,1,2)

multiplying(mat,1,1)
rowoperation(mat,1,0,2)
rowoperation(mat,1,-3,3)

multiplying(mat,2,2)
rowoperation(mat,2,-29,3)



'''
a=np.array([1,2,-4,-4],[2,4,0,0],[2,3,2,1],[-1,1,3,6])
b=np.array([5],[2],[5],[5]) 
x=np.linalg.solve(a,b)

'''