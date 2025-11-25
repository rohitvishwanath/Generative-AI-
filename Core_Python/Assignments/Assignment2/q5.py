def sellingprice(cp,discount):
    discount_amount=(discount /100) * cp
    sp=cp-discount_amount
    return sp
    

cp=int(input("Enter a cost price of book: "))
discount=int(input("Enter a discount: "))
sell=sellingprice(cp,discount)
print(f"The Selling price of book is {sell}.Rs")