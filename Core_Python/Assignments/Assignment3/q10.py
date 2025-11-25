##Accept age of five people and also per person ticket amount and then calculate total
##amount to ticket to travel for all of them based on following condition :
#3a. Children below 12 = 30% discount
##b. Senior citizen (above 59) = 50% discount
##c. Others need to pay full.
ticket_price=100
total_amount=0
ages=[]
for i in range(1,6):
    age = int(input(f"Enter age of person {i}: "))
    ages.append(age)
for age in ages:
    if age<12:
        amount=ticket_price*0.70
    elif age>59:
        amount=ticket_price*0.30
    else:
        amount=ticket_price
    
    total_amount += amount

print(f'The total ammount of ticket is:{total_amount}')


