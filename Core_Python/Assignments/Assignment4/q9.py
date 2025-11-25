start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))
div = int(input("Enter the number to check divisibility: "))
print("Numbers divisible by", div, "in the range are:")


for i in range(start, end + 1):
    if i % div == 0:
        print(i, end=" ")
