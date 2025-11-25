n=int(input("Enter a number: "))
print("all odd number until n ", n)

for i in range(1,1+n):
    if i%2!=0:
        print(i,end="")
