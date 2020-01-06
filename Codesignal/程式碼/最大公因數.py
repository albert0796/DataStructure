m,n=map(int,input("Input Two Common Era:").split())

m_factor=[]
for i in range(1,m+1):
    if m%i==0:
        m_factor.append(i)
n_factor=[]
for i in range(1,n+1):
    if n%i==0:
        n_factor.append(i)
factor_common=set(n_factor)&set(m_factor)
#factor_common=list(set(m_factor).intersection(set(n_factor)))
factor_common_highest=max(factor_common)        