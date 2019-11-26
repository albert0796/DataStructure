def QuickSort(ary):
    if len(ary)>1:
        index=0
        pivot=ary[0]
        for k in range(1,len(ary)):
            if ary[k] <= pivot:
                index+=1
                ary[index],ary[k] = ary[k],ary[index]
        ary[0],ary[index] = ary[index],ary[0]
        left=ary[0:index]
        right=ary[index+1:len(ary)]
        QuickSort(left)
        QuickSort(right)
        ary[0:index]=left
        ary[index+1:len(ary)]=right
    return ary











def QuickSort(ary,first=None,last=None):
    if first==None or last==None:
        first=0
        last=len(ary)-1
    if first < last:
        index=first
        pivot=ary[first]
        for k in range(first+1,last+1):
            if ary[k] <= pivot:
                index+=1
                ary[index],ary[k] = ary[k],ary[index]
        ary[first],ary[index] = ary[index],ary[first]
        QuickSort(ary,first,index-1)
        QuickSort(ary,index+1,last)
    return ary
