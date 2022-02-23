n=int(input("Enter the value: "))
for i in range(1,n+1):
        for k in range(1,i+1):
                print(k,end=' ')
        print()
for m in range(i-1,0,-1):
        for k in range(1,m+1):
                print(k,end=' ')
        print()
