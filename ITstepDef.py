def nbkz(q):
    w=""
    e=0
    for i in q:
        if q.count(i)>e:
            e = q.count(i)
            w = i
    return w
q=list(map(int,input().split()))
q.sort()
k=nbkz(q)
print(k)
