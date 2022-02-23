l=[]
n=int(input('Enter the value:'))
for i in range(n):
        e=int(input())
        l.append(e)
m=[]
for j in range((len(l)-1),-1,-1):
        m.append(l[j])
print(l,m)
