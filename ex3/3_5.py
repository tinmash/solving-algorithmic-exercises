from ipaddress import *
cnt=0
net = ip_network('141.14.138.235/255.255.224.0',0)
for i in net:
    s = list(map(int,str(i).split('.')))
    if int(s[-1])%2==0:
            if s[0]==141:
                flag = 1
                for o in s:
                    if o > 200:
                        flag = 0
                if flag == 1:
                    cnt+=1
print(cnt)