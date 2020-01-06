data=[6,5,4,3]

for i in range(1,len(data)):
    key = data[i]
    pre = i-1
    
    while data[pre] > key and pre >= 0:
        data[pre+1] = data[pre]
        pre-=1
        
    data[pre+1]=key


def SortInsertion(data):
    for i in range(1,len(data)):
        key = data[i]
        pre = i-1
        
        while data[pre] > key and pre >= 0:
            data[pre+1] = data[pre]
            pre-=1
            
        data[pre+1]=key
    return data

SortInsertion(data)



