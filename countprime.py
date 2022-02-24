n=int(input('Enter n: '))
l=[]
for i in range(n):
    l.append(int(input()))
c=0
for j in l:
    s=0
    for k in range(2,j+1):
        if j%k==0:
            s=s+1
    if s==1:
        c=c+1
print('Total No of prime numbers in',l,'are',c)
