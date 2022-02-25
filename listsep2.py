n=int(input('Enter a number: '))
m=[]
for a in range(n):
    b=int(input())
    m.append(b)
l=[]
k=[]
for i in m:
    if i<0:
        l.append(i)
    else:
        k.append(i)
s=k+l
print(s)
