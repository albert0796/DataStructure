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










