#3. Write a program to find sum of following series using functions :
#a. 1+ 2 + 3 + 4+..... + n
#b. 1!+ 2! + 3! + 4!+..... + n!
#c. 1^1 + 2^2 + 3^3+ ...... n^n

def sum_sereis(n):
    return sum(range(1,n+1))
n=int(input("Enter the number:"))

print("Sum of The series",sum_sereis(n))

def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def sum_fact(x):
    s=0
    for i in range(1,x+1):
        s+=fact(i)
    return s
x=int(input("Enter the  number:"))

print("Sum",sum_fact(x))


def power_series(n):
    s=0
    for i in range(1,n+1):
        s+=i**i
    return s
n=int(input("enter the Number:"))

print("power sum:",power_series(n))
