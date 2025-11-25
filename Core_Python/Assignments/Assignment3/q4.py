sp=int(input("Enter a sp: "))
cp=int(input("Enter a cp: "))

if sp>cp:
    profit=sp-cp
    print(profit, "this much profit is done")
elif cp>sp:
    loss=cp-sp
    print(loss,"this much loss is done")
else:
    print("NO prfoit , NO loss")