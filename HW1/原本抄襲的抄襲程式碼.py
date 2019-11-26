#來源: 使用python資料結構 9.3節，李淑馨著，深石出版社
def sortQuick(Ary, first=0, last=None):
    if last==None:
        last=len(Ary)-1
    if first < last:
        pivotIndex=Division(Ary, first, last)
        sortQuick(Ary, first, pivotIndex-1)
        sortQuick(Ary, pivotIndex+1, last)
    return Ary

def Division(Ary, first, last):
    index=first
    pivot=Ary[first]
    for k in range(first+1, last+1):
        if Ary[k] <= pivot:
            index+=1
            Ary[k], Ary[index] = Ary[index], Ary[k]
    left=Ary[first]
    Ary[first]=Ary[index]
    Ary[index]=left
    return index

