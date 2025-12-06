# 3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full.

passenger=int(input("Enter the number of Passenger: "))
ticket_cost=int(input("Enter the cost per ticket: "))

total_ammount=0
for i in range(passenger):
    age=int(input(f'Enter the age of Passengers{i+1}:'))
    if age<12:
        discount=0.3
    elif age>59:
        discount=0.5
    else:
        discount=0

    cost_after_discount=ticket_cost-(ticket_cost*discount)
    total_ammount +=cost_after_discount
    
    print("Total amount to be paid =", total_ammount)
