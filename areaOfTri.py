



side1 = float(input("enter side1:"))
side2 = float(input("enter side2:"))
side3 = float(input("enter side3:"))
s = (side1 * side2 * side3 / 2)
areaOfTri = (s*(s-side1)*(s-side2)*(s-side3)) ** 0.5
print("area of triangle is :" , areaOfTri)