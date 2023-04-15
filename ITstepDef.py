def Kll(q):
    p=0
    gl=0
    q=q.lower()
    for i in q:
        if q.isalpha():
            if i in 'aeiou':
                gl+=1
            else:
                p+=1
    return "golos: "+str(gl),"prigolos: "+str(p)
q=input()
l=Kll(q)
print(*l)
