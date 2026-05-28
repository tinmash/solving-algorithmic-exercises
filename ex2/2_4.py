def div(s):
    divs = []
    for i in range(2,int(s**0.5)+1):
        if s%i==0:
            divs.append(i)
            if i!=s**0.5:
                divs.append(s//i)
    return divs

def S(x,y):
    return(x in C)<=((3<=x<=105)and(not(x in B)))

for y in range(4,100):
    B = div(206)
    C = div(y)
    if C:
        if all(S(x,y) for x in range(0,500)):
            print(y)
            break
        
    

