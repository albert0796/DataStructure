#bubble sort
data=[7,6,5,3]

for n in range(len(data)-1,0,-1):
    for i in range(n):
        if data[i]>data[i+1]:
            data[i+1],data[i]=data[i],data[i+1]
######################################################
data=[3,5,6,7]

for n in range(len(data)-1,0,-1):
    for i in range(n,0,-1):
        if data[i]>data[i-1]:
            data[i-1],data[i]=data[i],data[i-1]
#####################################################

def SortBubble(data):
    for n in range(len(data)-1,0,-1):
        for i in range(n):
            if data[i]>data[i+1]:
                data[i+1],data[i]=data[i],data[i+1]
    return data

SortBubble(data)













