#area of triangle
height=int(input("Enter a height of triangle: "))
base=int(input("Enter a breadth of the triangle: "))
area_triangle=0.5* height * base
print(f"Area of the rectangle: {area_triangle}")

#area of rectangle

def area_rectangle(length,breadth):
    return length * breadth


length=float(input("Enter a length of rectangle: "))
breadth=float(input("Enter a bredth of rectangle: "))
convert=area_rectangle(length,breadth)
print(f"the area of rectangle is: {convert}")