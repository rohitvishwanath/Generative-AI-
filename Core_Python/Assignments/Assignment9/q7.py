#sum 0f digit

def sum_digit(num):
    if num == 0:
        return 0
    else:
        return (num % 10) + sum_digit(num //10)
    
num=int(input("Enter number: "))
print("sum of digit =", sum_digit(num))