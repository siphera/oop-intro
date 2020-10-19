from tkinter import *


class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def triangle_area(self):
        answer = (1/2) * self.base * self.height
        return round(answer, 2)


calcu = Triangle(0, 0)

calcu.base = float(input("Enter your base: "))
calcu.height = float(input("Enter your height: "))
print("The area is: ", calcu.triangle_area())

