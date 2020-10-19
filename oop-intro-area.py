class Rectangle:        # creating a class

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):         # adding a method
        rec_area = self.length * self.width
        return rec_area


calculate = Rectangle()         # creating an object

# attributes of the object
calculate.length = int(input("please enter length: "))
calculate.width = int(input("please enter width: "))

calculate.area()        # calling the area method
print(calculate.area())