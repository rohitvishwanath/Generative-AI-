# 1.wap to print first n prime numbers

n=int(input("Enter a number: "))

if n>1:
    for i in range(2,n//2+1):
        if n%i==0:
            print("Number is not prime")
            break
    else:
        print("Number is prime")
else:
    print("number is not prime")


#2.wap to calculate the sum of following series where
#n is input by user
#1/1! + 2/2! + 3/3! + 4/4! + n/n!

n=int(input("Enter the nnumber: "))
total =0

for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    total += i/fact

print("Sum of the series:",total)

#4.write a program to print pattern
# 10101
# 01010
# 10101
# 01010
# 10101

for i in range(5):
        if i % 2 == 0:
            print("10101")
        else:
            print("01010")


# 3.write a program to accept basic salary of n emp.(n should be accepted from user).if basic salary is below 20000 then 
#   da=10%,ta=12%,and hra=15% otherwise da=15%,ta=18% and hra=20%.Based on this clculate the total salary of each emp
#   and also total salary of all emp.


n=int(input("Enter number of employees: "))
total_salary_all = 0

for i in range(n):
    basic_salary = float(input(f"\nEnter basic salary of employee {i+1}: "))

    if basic_salary < 20000:
        da = basic_salary * 0.10
        ta = basic_salary * 0.12
        hra = basic_salary * 0.15
    else:
        da = basic_salary * 0.15
        ta = basic_salary * 0.18
        hra = basic_salary * 0.20

    total_salary = basic_salary + da + ta + hra
    total_salary_all += total_salary

    print(f"Total salary of employee {i+1}: {total_salary}")
print(f"\nTotal salary of all employees = {total_salary_all}")




