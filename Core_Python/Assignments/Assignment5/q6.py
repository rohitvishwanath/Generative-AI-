##6. Write a program to print prime numbers between 1 to 100.

for num in range(1,101):

    isprime=True
    for i in range(2,num):
        if num %i == 0:
            isprime=False
            break
    if isprime:
        print(num,end=" ")