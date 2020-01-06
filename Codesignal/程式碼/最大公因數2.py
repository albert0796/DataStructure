
def gcd_i(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def gcd_r(a,b):
    if b==0:
        gcd=a
    else:
        gcd=gcd_r(b,a%b)
    return gcd
print(gcd_i(36,11))

import copy
def gcd_i(a,b):
    while b>=1:
        n=a%b
        if a%b==0:
            return b
        else:
            a=copy.copy(b)
            b=n
gcd_i(36,11)