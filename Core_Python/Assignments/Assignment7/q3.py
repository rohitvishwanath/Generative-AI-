n = 4
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(i, i+i):
        print(j, end=" ")
    for j in range(i+i-2, i-1, -1):
        print(j, end=" ")
    print()