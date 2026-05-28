def Amp(n,m):
    r=bin(n&m)[2:]
    R=''
    for i in r:
        if i=='1':
            R+='0'
        if i=='0':
            R+='1'
    return int(R,2)
def S(A,x,y):
    return (Amp(x,51)==0)<=((Amp(A,29)!=0)<=(Amp(y,x)==0))

for A in range(100,1000):
    if all(S(A,x,y) for x in range(1,100) for y in  range(1,100)):
        print (A)
        break
