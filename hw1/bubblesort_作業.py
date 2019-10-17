def SortBubble(data):
    for n in range(len(data)-1,0,-1):
        for i in range(n):
            if data[i]>data[i+1]:
                data[i+1],data[i]=data[i],data[i+1]
    return data













