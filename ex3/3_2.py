from ipaddress import *
cnt=0
ip_net = ip_network('174.101.64.62/255.255.240.0',0)
for i in ip_net:
    b = int(i)
    b2 = bin(b)[2:].zfill(32)
    if b2[16:].count('1')%2==0:
        if sum(map(int,str(i).split('.')[2:]))%2!=0:
            flag=1
            for a in str(i).split('.'):
                if len(a)!=len(set(a)):
                    flag=0
            if flag == 1:
                cnt+=1
print(cnt)
