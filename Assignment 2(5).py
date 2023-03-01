class numero:
    def __init__(self,number):
        self.number = number

    def factos(self):
        fact = 1

        for i in range(1,self.number + 1):
            fact = fact * i

        print("The factorial of " + str(self.number) + " is: " + str(fact))

print("FACTORIAL CALCULATOR")
num = int(input("Enter a number: "))

holder = numero(num)

holder.factos()