# Given the radius of a circle and the area of a square, return True if the circumference
# of the circle is greater than the square's perimeter and False if the square's perimeter
# is greater than the circumference of the circle.
import math

def circle_square(radius, Area_Square):
    Circum = 2 * 3.14 * radius
    Area = math.sqrt(Area_Square) * 4
    if Circum > Area:
        return True
    else:
        return False

radius = float(input("Enter the ardius of the circle:"))
Area_Square = float(input("Enter area of Square:"))

print("The final points is:", circle_square(radius, Area_Square))
