def div(s):
    divs = []
    for i in range(1,int(s**0.5)+1):
        if s%i==0:
            divs.append(i)
            if i!=s**0.5:
                divs.append(s//i)
    return divs

def inf(n,m):
    if div(n):
        return sum(div(n))%n*m

def S(x,A):
    return (inf(x,A)or (not(inf(x,80))))<=((not(inf(x,27)))or inf(x,40))

a15=[]
for A in range(1,500):
        if all(S(x,A) for x in range(1,1000)):
            if len(a15)<15:
                a15.append(A)
print(sum(a15))
