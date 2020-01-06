def  tryit(i):    # search and backtrack 
    global  h, a, b, sa, sb, maxv, capacity
    h[i] = 1    # select the object
    sa += a[i]; sb += b[i]
    if (i < 9) :
        tryit(i+1)
    else :
        if  sa >= maxv and sb <= capacity :
            maxv=sa
            prt()
    h[i] = 0    # discard the object 
    sa -= a[i];     sb -= b[i]
    if  i < 9 :
        tryit(i+1)
    else :
        if  sa >= maxv and sb <= capacity :
            maxv=sa
            prt()
def  prt() :
    print(" %5d    %5d    " % (sa, sb), end='  ' )
    print(h)
sa=0; sb=0; maxv=0
capacity = 269 
h=[0] * 10  # selected or not
a=[55, 10, 47,  5,  4, 50,  8, 61, 85, 87]  # profit 
b=[95,  4, 60, 32, 23, 72, 80, 62, 65, 46]  # size
print("\n   tprofit  tsize    selected or not")
tryit(0)
