# Armstrong number  or not
#sum of each digit***(for 3 digit number)

def armstrong_sum(num):
    if num==0:
        return 0
    else:
        digit = num % 10
        return (digit ** 3) + armstrong_sum(num // 10)

num = int(input("Enter number: "))

if num == armstrong_sum(num):
    print("Arsmtrong number")
else:
    print("Not Armstrong number")


# without recurssion

# num= int(input("Enter number: "))
# temp=num
# sum=0

# while temp!=0:
#     digit = temp%10
#     sum += digit ** 3
#     temp //= 10

# if num == sum:
#     print("Armstrong number")
# else:
#     print("Not armstrong number")