for i in range(10_000,999,-1):
    s=[]
    i2=str(i)
    for o in range(len(i2)-1):
        s.append(int(i2[o])+int(i2[o+1]))
    s.sort()
    s = map(str,s[1:])
    R=''.join(s)
    if R=='1014':
        print(i)
        break
