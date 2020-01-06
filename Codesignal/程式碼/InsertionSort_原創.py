def sortInsertion(ary):
    
    if len(ary) == 0:
        return 'The array is empty'
    
    for i in range(1, len(ary)):
        
        element = ary[i]
        index = i
        
        for j in range(i-1, -1, -1):
            
            if element < ary[j]:
                ary[index], ary[j] = ary[j], ary[index]
                index -= 1
                
            else:
                break
            
    return ary


data = [6,5,4,3]
data = [10,9,8,7,6,5,4,3]
data = [1]
data = []
data = [1,1,1]
sortInsertion(data)
    
    