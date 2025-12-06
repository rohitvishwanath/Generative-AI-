##5. Write a program to accept an integer amount from user and tell minimum

amount=int(input("Enter a amount: "))

notes=[500,200,100,50,20,10]

print("mini notes required")

for i in notes :
    count=ammount//i
    if count>0:
        print(i,"X",count)
    ammount%=i
    