F=[0]*1300
G=[0]*1300
for n in range(1,1300):
    if n==1 or n==2:
        F[n]=2
        G[n]=2
    if n>2:
        F[n]=F[n-1]*2 - F[n-2] + n**3
        G[n]=G[n- 1] + G[n - 2] + n * n - int(G[n-1]*0.9)
s=F[G[17]]
print(s)
summ=0
for i in str(s):
    summ+=int(i)
print(oct(summ)[2:])

