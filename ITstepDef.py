
def rad(q):
    p=""
    if len(q)<6:
        return "Недостатньо символів"
    else:
        return q[0:3]+q[-3::]
q=input()
l=rad(q)
print(l)
