
#Recursive function to calculate factorial
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return  n * fact(n-1)
    
#Recursive function to calculate sum of fact series
def sum_series(n):
    if n==1:
        return fact(1)
    else:
        return fact(n) + sum_series(n-1)
    
n= int(input("Enter value of n: "))
print("sum of series =", sum_series(n))


# without recurssion
# n=int(input("Enter a number: "))
# fact=1

# for i in range(1,n+1):
#     fact = fact * i

# print(fact)




