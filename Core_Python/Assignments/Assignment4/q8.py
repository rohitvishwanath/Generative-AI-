#8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
start=int(input("Enter the start range: "))
end=int(input("Enter the end range: "))
print("Numbers divisible by 7 and multiple of 5:")

for num in range(start, end+1):
    if num % 7==0 and num % 5==0:
        print(num, end=" ")