#que1
# check code for year is a leap or not 
year = int(input("Enter a year: "))

if(year % 400== 0):
    print(year, "is a leap year")
elif(year %100 == 0):
    print(year, "is not a leap year")
elif(year % 4 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#que2
# Write a program to accept 3 digit number. If first digit is double of second digit and half of
# third digit then display “Yes, you have done it”, otherwise display “Please try next time”.
# Eg : - 428 , 214 etc.

num=int(input("Enter a number"))

first=num // 100
second=(num // 10)%10
third=num %10


if first== 2* second and first * 2== third:
    print("Yes, you have done it")
else:
    print("please try next time")


#que3
# A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
# for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
# length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
# cost of fencing the field.

import math

radius=20.0
length=50.0
breadth=40.0
strands=5
cost_per_m=35.0

semicircle_arc= math.pi * radius
perimeter = 2*length +breadth + semicircle_arc

total_length= strands * perimeter
total_cost=  total_length * cost_per_m

print(f"Perimeter to fence(m): {perimeter: .4f}")
print(f"Total wire required(m): {perimeter: .4f}")
print(f"Total cost(Rs): {perimeter: .4f}")


# que4
# 4. Write a program to calculate the total cost of painting. The interior of building with four
# equal sized walls.

Rate=int(input("Enter the Rate per wall:"))
wall=int(input("Enter the number of wall:"))

price=Rate*wall

print(f'The price of th painting:{price}')


#que5
# 5. A man goes for shopping. He buys 5 products. Accept the price of all products and display
# the total bill after adding 18% GST


p1=int(input("Enter the price of product1:"))
p2=int(input("Enter the price of product2:"))
p3=int(input("Enter the price of product3:"))
p4=int(input("Enter the price of product4:"))
p5=int(input("Enter the price of product5:"))

total_price=p1+p2+p3+p4+p5

GST=total_price%18 *100

Final_price=total_price-GST
print(f'Total bill After adding 18% GST:{Final_price}')








