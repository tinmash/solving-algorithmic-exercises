def S(x,A):
    return ((x%48==0)or(x%96==0))<=(x%A==0)
for A in range(1000,-100,-1):
    if all(S(x,A)==1 for x in range(1,100)):
        print(A)
        break
