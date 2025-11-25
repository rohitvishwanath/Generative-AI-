gender=input("Enter the gender of person: ")
age=int(input("Enter a age: "))

if age>=21 and gender=="male":
    print("the person is ready to marride")
elif age>=18 and gender=="female":
    print("the person is ready to marride")
else:
    print("person is not ready to marrage")
