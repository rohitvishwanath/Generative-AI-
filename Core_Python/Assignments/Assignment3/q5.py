id="vasnat"
Pass="123456"

# userId=input("Enter a userID: ")
# password=input("Enter a password: ")

# if userId==id and password==Pass:
#     print("your sucssefully login in your account") 
# else:
#     print("devi aur sajjno ap galat he, firse kosis kare ")

def login(user_Id,Password):
    if user_Id == id and Password == Pass:
        print("Your login sucssesfully in your account ")    
    else:
        print("kosis karne valo ki har nahi hoti, firse try kare")
    return user_Id,Password


user_Id=input("Enter Your USER_ID: ")
Password=input("Enter Your Password: ")
log=login(user_Id,Password)
print(log)