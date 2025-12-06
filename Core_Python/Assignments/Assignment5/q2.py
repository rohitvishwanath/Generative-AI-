# 2.Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students.

num=int(input("Enter a number of student: "))
for i in range(num):
    print(f"Student{i+1}")
    total=0
    for j in range(5):
        marks=float(input("Enter a marks of student: "))
        total += marks
        per =total/5

    print(f"Total marks:,{total}")
    print(f"percentage:{per}")
