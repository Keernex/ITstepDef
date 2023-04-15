def serA(q):
    l=sum(q)/len(q)
    return l
q=list(map(int,input().split()))
s=serA(q)
print(s)
