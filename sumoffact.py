def sum_of_fact(n):
        fact=1
        sum=0
        for i in range(1,n+1):
                fact=fact*i
                sum=sum+fact
        print("sum of factorial numbers:",sum)
n=int(input("Enter a number:"))
sum_of_fact(n)
