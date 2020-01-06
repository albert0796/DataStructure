def fib_r(n):
    if n==0 or n==1:
        fib=n
    else:
        fib=fib_r(n-2)+fib_r(n-1)
    return fib
for i in range(20):
    print(fib_r(i))
