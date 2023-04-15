def vik(l):
    return sorted(l, key=lambda x: x[1])
n=int(input())
l=[]
for i in range(n):
    w,r=map(str,input().split())
    r=int(r)
    l.append((w,r))
k=vik(l)
for i in k:
    print(*i)
