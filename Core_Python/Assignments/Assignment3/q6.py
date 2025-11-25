# 8. Write a program to prompt user to enter userid and password. After verifying
# userid and password display a 4 digit random number and ask user to enter the
# same. If user enters the same number then show him success message otherwise
# failed. (Something like captcha)
id="rohit"
password="1234"

user_id=input("Enter a USER_ID: ")
user_password=input("Enter a Password: ")

if user_id==id and user_password==password:
    print("Login sucssesfully ")
else:
    print("Invalid login and password")

code=1234
c=int(input("Enter a code Verification: "))

if code==c:
    print("You have done with your verification")
else:
    print("Your have not correct")