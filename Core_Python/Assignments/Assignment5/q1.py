id="Ram"
password=12345

attempts=3

for i in range(attempts):
    user_id=input("Enter your id:")
    user_pass=int(input("Enter the user password:"))

    if user_id==id and user_pass==password:
        print("you login succesfully")
        break
    else:
        print("Incorrect input")
else:
    print("Too many attemps Try later")