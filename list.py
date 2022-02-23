l=[]
n=int(input('enter the value'))
for i in range(n):
        e=int(input())
        l.append(e)
min=l[0]
max=l[0]
for i in range(1,n):
        if l[i]<min:
                min = l[i]
        if l[i]>max:
                max=l[i]
print ('min = ',min,'max = ',max)
