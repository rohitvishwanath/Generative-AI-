amount = int(input("Enter the amount: "))

notes = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
total_notes = 0

print("\nMinimum number of notes:\n")

for n in notes:
    count = amount // n
    if count > 0:
        print(f"{n} x {count}")
        total_notes += count
    amount = amount % n

print("\nTotal number of notes needed =", total_notes)