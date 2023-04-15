def vl(q):
    p=""
    s=0
    for i in range(len(q)):
        if q[i-1]==" " and q[i].isalpha():
            p+=q[i].capitalize()
        else:
            p+=q[i]
    return p
q=input()
q=" "+q
l=vl(q)
print(l)
