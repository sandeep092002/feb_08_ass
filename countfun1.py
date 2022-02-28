n=int(input("Enter n: "))
s=[]
for i in range(n):
    s.append(int(input()))
l=[]
for j in s:
    if s.count(j)%2!=0:
        if j not in l:
            l.append(j)
print(l)
