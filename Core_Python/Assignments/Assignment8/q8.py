##9. Write a program to check if entered number is a palindrome or
#not.

def palindrome(n):
    return  n==int(str(n) [::-1])

n=int(input("Enter a number: "))

if palindrome(n):
    print("Number is palindrome: ")
else:
    print("Number is not palinfrome: 2")