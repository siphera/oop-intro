class intro:        # creating a class
    def intro_oop(self):        # adding a method
        print("I am a ", self.name)
        print("My colour is ", self.colour)


obj_intro = intro()     # creating an object

obj_intro.name = "Triangle"
obj_intro.colour = "Red"
obj_intro.intro_oop()