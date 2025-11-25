# Lambda functions
square_area = lambda a: a * a
rectangle_area = lambda l, w: l * w
triangle_area = lambda b, h: 0.5 * b * h

# User inputs
a = float(input("Enter side of square: "))
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
b = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))

# Results
print("Area of square:", square_area(a))
print("Area of rectangle:", rectangle_area(l, w))
print("Area of triangle:", triangle_area(b, h))