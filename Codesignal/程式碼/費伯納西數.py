def fib_i(n):
    _1,_2=0,1
    for i in range(n+1): 
        _1,_2=_2,_1+_2
    return _1
for i in range(10):
    print(fib_i(i),end="")

def fib_r(n):
    if n==0 or n==1:
        fib=n
    else:
        fib=fib_r(n-2)+fib_r(n-1)
    return fib
for i in range(20):
    print(fib_r(i))