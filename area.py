def calculate_circle_area(radius):
    assert radius > 0
    total = 3.141559*(radius**2)
    return total



num = float(input("Enter the radius of a circle: "))
print("The area is --> ", round(calculate_circle_area(num)))
