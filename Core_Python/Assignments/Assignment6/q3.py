#    1
#  1 1
# 1 2 1
#1 3 3 1

from math import factorial

n = 4

for i in range(n):
    print(" " * (n - i), end="")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()
