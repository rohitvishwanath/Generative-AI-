# #WAP to print factorial of a number .
# n=int(input("Enter the Number of n:"))
# fact=1
# for i in range (1,n+1):
#     fact *=i
# print(f'factorial of 1 to {n} is {fact}')




# num=int(input("Enter a number: "))
# fact=1
# for i in range(1,num+1):
#     fact=fact * i

# print("The factorial of number" , fact)



#Recurssion 
def fact(n):
    if n==0:
        return 1
    else:
        return n * fact(n-1)

n=int(input("Enter a number: "))
f=fact(n)
print(f"The factorial of number:{f}")

    