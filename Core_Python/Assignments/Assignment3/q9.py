num = int(input("Enter a number: "))
rev = 0
n = num

while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print("Palindrome" if num == rev else "Not palindrome")