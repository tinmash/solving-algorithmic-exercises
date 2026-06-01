from ipaddress import *
cnt=0
net = ip_network('150.101.64.123/255.255.128.0',0)
for i in net:
    n = list(map(int,str(i).split('.')))[2:]
    if sum(n)<250:
        cnt+=1
print(cnt)
