# Reversed number

def reverse_num(num , rev=0):
    if num==0:
        return rev
    digit =num % 10
    rev= rev * 10 + digit
    return reverse_num(num // 10,rev)

num=int(input("Enter number: "))
print("Reveresd =", reverse_num(num))

