import re
f = open('4_1_file.txt')
cnt=0
max_e=0
for i in f:
    cnt+=1
    i=i.strip()
    d=re.fullmatch(r'[1-9][0-9]*(?:[+-/][1-9][0-9]*)*',i)
    if d is not None:
        if max_e < eval(i):
            max_e = eval(i)
            max_c = cnt
print(max_c)

