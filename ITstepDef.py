
def dil(q):
    p=[]
    for i in range(1,q+1):
        if q%i==0:
            p.append(i)
    return p
q=int(input())
l=dil(q)
print(*l)
