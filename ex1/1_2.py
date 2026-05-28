def summa(s):
    chet=[]
    for n in s:
        if int(n)%2==0:
            chet.append(int(n))
    if chet:
        return sum(chet)
    else:
        return 0

def summ_2(s):
    summ=0
    if len(s)==1:
        return 0
    else:
        for i in range(len(s)-1):
            if i%2!=0:
                summ+=int(s[i])
    return summ
for i in range(1,2000):
    s = str(i)
    R=abs(summa(s)-summ_2(s))
    if R==15:
        print(i)
        break
