n=int(input("Enter n value: "))
esum=0
osum=0
for i in range(1,n+1):
    if i%2==0:
        esum=esum+i
    else:
        osum=osum+i
print('Odd numbers sum upto',n,'is',osum)

print('Even numbers sum upto',n,'is',esum)
