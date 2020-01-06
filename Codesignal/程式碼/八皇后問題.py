def  tryit(i):    #  search and backtrack routine 
    global  sn, a, b, c, x
    for  j  in range(8) :
        if  a[j]==True and b[i+j]==True and c[i-j+7]==True :
            x[i]=j+1
            a[j]=False
            b[i+j]=False
            c[i-j+7]=False
            if  i<7 :
                tryit(i+1)
            else :
                sn+=1  # count the solution 
                print(" Solution %2d: %s" % (sn,x) )
            a[j]=True
            b[i+j]=True
            c[i-j+7]=True
x=[None]*8    # queen position in the i-th column 
a=[True]*8        # queen occupies the i-th row 
b=[True]*15     # queen occupies the right diagonal 
c=[True]*15     # queen occupies the left diagonal 
sn=0     # solution counter 
tryit(0)
print(" Total solutions: %d\n" % sn)