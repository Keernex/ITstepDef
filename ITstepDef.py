def Kll(q):
    p=[]
    for i in q:
        if i not in p:
            p.append(i)
    return p
q=list(map(int,input().split()))
l=Kll(q)
print(*l)
