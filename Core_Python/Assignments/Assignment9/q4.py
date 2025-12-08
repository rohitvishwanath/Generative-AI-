# sum of n numbers

def sum_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_n(n - 1)

n = int(input("Enter n: "))
print("Sum of n numbers =", sum_n(n))