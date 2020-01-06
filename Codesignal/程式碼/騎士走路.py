def  tryit(i,x,y) :    # search and backtrack 
    global h, a, b, sn
    for  k  in range(8) :
       u=x+a[k]    # select the next move 
       v=y+b[k]
       if  u>=0 and u<=4 and v>=0 and v<=4 : # must in chessboard
           if  h[u][v]==0 : # empty field 
               h[u][v]=i  # record the move 
               if  i<25 : # if chessboard is not full
                   tryit(i+1,u,v) # try next move 
               else : # print the solution 
                   sn+=1    
                   prt()
                   if sn==4 : # terminate 
                       h=[[1]*5]*5
               h[u][v]=0 # remove the move

def  prt() :    # print a solution 
    print("\n\nSolution %2d : " %sn)
    for  i  in range(5) :
        print()
        for  j  in range(5) :
            print("%2d"%h[i][j],end=' ') 
h= [[0 for j in range(5)] for i in range(5)]
a=[2,1,-1,-2,-2,-1,1,2]    # 8 possible moves 
b=[1,2,2,1,-1,-2,-2,-1]
sn=0    # solution counter
h[2][2]=1    # the start field
tryit(2,2,2)	# try next move 
print("\n\nTotal solutions: %d" % sn)
