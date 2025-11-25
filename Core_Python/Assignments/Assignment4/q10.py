#10. WAP to check if given number is Perfect Number.
num=int(input("Ente a Number: "))
sum_div=0
for i in range(1,num):
    if i % num !=0 and num % i ==0:
        sum_div += i
if sum_div==num:
    print(num, "is a Perfect Number.")
else:
    print(num, "is not a Perfect Number.")
