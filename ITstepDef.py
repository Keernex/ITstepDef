def fin(n):
    if n<=1:
        return n
    else:
        return fin(n-1) + fin(n-2)
q=int(input())
l=fin(q)
print(l)
