import numpy as np

m=np.array([[5,2,2],
            [-1,1,2],
            [3,0,0]])



def Det(m):
    if m.shape[1]==1:
        return m.item(0)
             
    else:
        det=0
        for j in range(1,m.shape[1]+1):
            mt=m
            for i,k in zip(list([0,1]),list([0,j-1])):
                mt=np.delete(mt, k, axis=i)
            det+=((-1)**(1+j))*m.item(0,j-1)*Det(mt)
        return det
Det(m)
