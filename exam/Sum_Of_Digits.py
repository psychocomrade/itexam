n=int(input("Enter a number-->"))
sum=0
while(n!=0):
	r=n%10
	sum=sum+int(r)
	n=n/10
print("Sum of digits= ", sum)
