#7. Write a program to find sum of digits of a number.

def sum_digits(n):
    s=0
    while n>0:
        s+=n%10
        n//=10
    return s

n = int(input("Enter number: "))
print("sum of digits:", sum_digits(n))
