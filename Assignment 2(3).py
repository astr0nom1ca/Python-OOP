class circle:
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        areacal = 3.14 * (self.radius ** 2)
        print("The area of the circle is: " + str(round(areacal,2)))


    def circumference(self):
        circ = 2 * (3.14 * self.radius)
        print("The circumference of the circle is:" + str(round(circ,2)))



print("To determine the area and circumference of the circle, enter the given radius below: ")
rad = int(input("What is the given radius: "))

radinput = circle(rad)

radinput.area()
radinput.circumference()

