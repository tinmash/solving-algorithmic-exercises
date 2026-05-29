from ipaddress import *
cnt=0
ip_net = ip_network('124.101.22.62/255.255.255.128',0)
for i in ip_net:
    p = str(i)
    f = sum(map(int,p.split('.')[2:]))
    if f>140:
        cnt+=1
print(cnt)
