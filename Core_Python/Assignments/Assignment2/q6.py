## Program to calculate total salary of an employee
basic=float(input("Enter a basic salary of employee: "))
da=0.10 * basic # 10% of salary
ta=0.12 * basic # 12% of salary
hra=0.15 * basic # 15% of basic

total_salary=basic +da +ta +hra
print("DA =", da)
print("TA =", ta)
print("HRA =", hra)
print("Total Salary =", total_salary)



