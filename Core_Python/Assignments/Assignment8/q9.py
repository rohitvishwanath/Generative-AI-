#10. Write a program to check if entered year is a leap year or not.
def is_leap(year):
    return (year % 400 == 0)or (year % 4==0 and year % 100 != 0)

year=int(input("Enter the year:"))

if is_leap(year):
    print(year,":is leap year")
else:
    print(year,":is not leap year")
