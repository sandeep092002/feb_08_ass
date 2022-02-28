n=int(input("Enter n: "))
s=[]
for i in range(n):
    s.append(int(input()))
l=[]
for j in s:
    if s.count(j)==1:
        if j not in l:
            l.append(j)
print(l)
