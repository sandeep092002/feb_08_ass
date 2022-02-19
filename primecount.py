def is_prime(n):
	for i in range(2,n):
		if n%i==0:
			return False
	return True
n=int(input("Enter n: "))
count=0
for i in range(2,n+1):
	if is_prime(i):
		count=count+1
print(count)
