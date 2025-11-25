num=int(input("Enter a three digit number: "))

hundred=num // 100
tens=(num//10)%10
ones=num %10

total=hundred+tens+ones
print(f'Sum of Three Digits is:{total}')


