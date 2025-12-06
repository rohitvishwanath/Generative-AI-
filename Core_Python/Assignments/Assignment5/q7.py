##7. Write a program to print first n prime numbers.

n=int(input("Enter how many numbers to print"))
count=0
num=2
while count<n:
    isprime=True
    for i in range(2,num):
        if num %i ==0:
            isprime=False
            break
    if isprime:
        print(num,end=" ")
        count+=1
    num +=1  
