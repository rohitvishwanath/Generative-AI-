#8. Write a program to solve the following series :
#a. 1! + 2! + 3! + 4! + .....n!
#b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
#c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
#d. S = a + (a^2) / 2 + (a^3)/ 3 + ...... + (a^10) / 10
#e. x – (x^2)/3 + (x^3)/5 – (x^4)/7 + .... to n terms

n = int(input("Enter n: "))
sum = 0

for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum += fact

print("Sum =", sum)

#b
N = int(input("Enter N: "))
sum = 0

for i in range(1, N+1):
    sum += N ** i

print("Sum =", sum)

#c
a = int(input("Enter value of a: "))
sum = 0

for i in range(1, 11):
    sum += (a ** i) / i

print("Sum =", sum)

#D
x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(1, n+1):
    term = (x ** i) / i
    if i % 2 == 0:
        term = -term
    sum += term

print("Sum =", sum)

