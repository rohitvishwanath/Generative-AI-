# Reverse a number using recursion

def reverse_num(num, rev=0):
    if num == 0:
        return rev
    else:
        digit= num % 10
        rev = rev * 10 + digit
        return reverse_num(num // 10, rev)
    
num = int(input("Enter number: "))
print(reverse_num(num))