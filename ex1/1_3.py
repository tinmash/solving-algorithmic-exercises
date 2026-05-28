def ch(n):
    s=''
    while n>0:
        d = n%4
        s = str(d)+s
        n = n//4
    return s
for N in range(1,255):
    n4 = ch (N)
    if n4.count('3') > 2:
        n = n4 + '0'
    else:
        n = n4 + str(n4.count('3')%4)
    R = int (n, 4)
    if R > 461:
        print(N)
        break
