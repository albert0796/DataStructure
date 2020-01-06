def gcd_r(a,b):
    if b==0:
        gcd=a
    else:
        gcd=gcd_r(b,a%b)
    return gcd
print(gcd_i(36,11))
