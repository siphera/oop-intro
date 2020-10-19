from tkinter import *


class Circle:
    def __init__(self, radius, diameter):
        self.radius = radius
        self.diameter = diameter

    def circle_area(self):
        answer = 3.14159 * self.radius**2
        return round(answer, 2)

    def perimeter_circle(self):
        answer2 = 2 * 3.14159 * self.radius
        return round(answer2, 2)


calc = Circle(0, 0)

calc.radius = float(input("Enter radius: "))
print("The area is: ", calc.circle_area())
print("The perimeter is: ", calc.perimeter_circle())
