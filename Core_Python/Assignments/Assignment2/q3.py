feet=float(input("Enter a feet: "))
inches=float(input("Enter a inches: "))

meetrs_from_feet=feet*0.3048
cm_from_inches=inches*2.54
total_cm=cm_from_inches(meetrs_from_feet*100)
meters=int(total_cm // 10)
centimeters=total_cm%100

print(f"Distance in meters: {meters}")
print(f"The distance in centimters: {centimeters}")

