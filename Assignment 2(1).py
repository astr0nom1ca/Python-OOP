class variables:
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2


    def calculator(self):

        addition = self.v1 + self.v2
        subtraction = self.v1 - self.v2
        multiplication = self.v1 * self.v2
        division = self.v1 / self.v2
        modulus = self.v1 % self.v2
        floordiv = self.v1 // self.v2
        exponential = self.v1 ** self.v2

        print("The sum of the numbers is:" + str(addition))
        print("The difference between the numbers is:" + str(subtraction))
        print("The product of the numbers is:" + str(multiplication))
        print("When the numbers are divided,we get:" + str(division))
        print("The remainder of the numbers when divided is:" + str(modulus))
        print("Floor division of the numbers yields:" + str(floordiv))
        print("When " + str(self.v1) + " is raised to the power of " + str(self.v2)+ " we get:" + str(exponential))


var1 = int(input("Enter first number:"))
var2 = int(input("Enter second number:"))
var = variables(var1,var2)

var.calculator()