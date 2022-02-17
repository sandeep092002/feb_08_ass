a=-1 
b=1 
n=int(input("Enter n: "))
sum=0
for i in range(1,n+1): 
    c=a+b 
    sum=sum+c 
    a=b 
    b=c
print("Sum of",n,'fibonocci numbers is',sum)
