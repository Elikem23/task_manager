# ask user to iput the length of the 3 sides of a triangle
x = float(input("enter the first side:"))
y = float(input("enter the second side:"))
z = float(input("enter the third side:"))
# if all sides are equal print equilateral
if x==y and y == z:
    print("equilateral")
# if 2 sides are equalprint iscosceles
elif x==y or y==z or x==z:
    print("isosceles")
# if no sides are equal print scalene
else:
    print("scalene")