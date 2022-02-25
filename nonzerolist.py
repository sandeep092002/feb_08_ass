n=int(input('Enter a number: '))
m=[]
for a in range(n):
    b=int(input())
    m.append(b)
l=[]
k=[]
c=0
for i in m:
    if i==0:
        l.append(i)
    else:
        c+=1
        k.append(i)
print('non zero numbers list',k,'\ncount=',c)
