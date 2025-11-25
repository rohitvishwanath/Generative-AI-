start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
print("Armstrong numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    digits = len(str(num))
    sum_pow = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum_pow += digit ** digits
        temp //= 10
        
    if sum_pow == num:
        print(num, end=" ")