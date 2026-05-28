def S(x,A):
    return ((x%A==0)and(x%16==0))<=((not(x%16==0))or(x%111==0))
for A in range(1,1000):
    if all(S(x,A)==1 for x in range(1,2000)):
        print(A)
        break
