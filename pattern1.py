n=int(input("Enter the value: "))
for i in range(1,n+1):
        for j in range(n-i,0,-1):
                print(' ',end='')
        for k in range(1,i+1):
                print('*',end=' ')
        print()
for m in range(i-1,0,-1):
        for j in range(n-m,0,-1):
                print(' ',end='')
        for k in range(1,m+1):
                print('*',end=' ')
        print()
