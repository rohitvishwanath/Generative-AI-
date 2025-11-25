s1=int(input("Enter a s1 marks: "))
s2=int(input("Enter a s2 marks: "))
s3=int(input("Enter a s3 marks: "))
s4=int(input("Enter a s4 marks: "))
s5=int(input("Enter s s5 marks: "))
total= s1+s2+s3+s4+s5

if total > 350:
    print("First class")
elif total > 250:
    print("second class")
else:
    print("Third class")