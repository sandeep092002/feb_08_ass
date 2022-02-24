n=int(input('Enter n: '))
l=[]
for i in range(n):
    l.append(int(input()))
a=[]
b=[]
for j in l:
    if j%2==0:
        a.append(j)
    else:
        b.append(j)
print('Even--',a,'Odd--',b)
