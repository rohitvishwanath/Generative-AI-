#5. WAP to print Fibonacci series upto n.

# Fibonacci number
def fibonacci(n):
	if n<= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

#Taking input from user
num=int(input("Enter how many terms you want in the Fibobnacci series: "))

print("\nFibonacci Series:")
for i in range(num):
	print(fibonacci(i), end="")


