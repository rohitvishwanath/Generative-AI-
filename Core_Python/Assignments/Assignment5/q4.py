##4. Write a program to check if given number is Armstrong number or not.
##(Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +
##4*4*4*4)


num=int(input("Enter a number: "))
temp=num
sum=0
digit=len(str(num))

while temp >0:
    r =temp % 10
    sum += r ** digit
    temp //= 10

if sum == num:
    print("number is armstrong")
else:
    print("not aramstrong")