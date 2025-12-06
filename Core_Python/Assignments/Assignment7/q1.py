n = 7
for i in range(n):
    for j in range(n):
        if (
            (i == 0 and 2 <= j <= 4) or
            (i == n-1 and 2 <= j <= 4) or
            (j == 0 and 2 <= i <= 4) or
            (j == n-1 and 2 <= i <= 4) or
            (i == 1 and (j == 1 or j == 5)) or
            (i == 5 and (j == 1 or j == 5))
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()