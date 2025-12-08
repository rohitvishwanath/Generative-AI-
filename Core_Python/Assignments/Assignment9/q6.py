# fibbonacci series
def fibbo(n):
    if n == 0 or n==1:
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)

n=int(input("Ente a number = "))

print("fibbonacci series")
for i in range(n):
    print(fibbo(i), end=" ")
