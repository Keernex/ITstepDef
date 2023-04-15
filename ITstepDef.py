def sk(q,w):
    p=0
    for i in range(len(q)):
        p+= q[i]*w[i]
    return p
q=list(map(int,input().split()))
w=list(map(int,input().split()))
l=sk(q,w)
print(l)
