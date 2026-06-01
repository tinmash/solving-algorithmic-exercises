f = open('4_2_file.txt').readline()
f = f.split('Y')
max_l=0
for i in range(len(f)-1):
    if len(f[i])+len(f[i+1])+1 > max_l:
        max_l = len(f[i])+len(f[i+1])+1
print(max_l)
