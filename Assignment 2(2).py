import math
class equations:
    def __init__(self,u,a,t,c,b):
        self.u = u
        self.a = a
        self.t = t
        self.c = c
        self.b = b

    def eqn1(self):
        vform = self.u +(self.a * self.t)
        print("Applying formula: V = U + at")
        print("Result: " + str(vform))

    def eqn2(self):
        sform = (self.u * self.t) + (0.5 *(self.a * self.t)) * 2
        print("Applying formula: S = ut + 1/2at2")
        print("Result: " + str(sform))

    def eqn3(self):
        tform = (2 * self.a) + math.sqrt(self.b) + (9 * self.c)
        print("Applying formula: T = 2 * a + \/b + 9c")
        print("Result: " + str(round(tform,2)))


uval = int(input("Enter corresponding value of u:"))
aval = int(input("Enter corresponding value of a:"))
tval = int(input("Enter corresponding value of t:"))
cval = int(input("Enter corresponding value of c:"))
bval = int(input("Enter corresponding value of b:"))
container = equations(uval,aval,tval,cval,bval)

#something akin to a switch case function so the user can pick out a specific formula
print("Choose equation with which to evaluate input:")
print("For 'V = U + at',press one(1)")
print("For 'S = ut + 1/2at2',press two(2)")
print("For 'T = 2 * a + \/b + 9c',press three(3)")
print("For all formulas,enter four(4)")
ansr = int(input("Enter a number based on what you want to do with your input: "))

if ansr == 1:
    container.eqn1()
elif ansr == 2:
    container.eqn2()
elif ansr == 3:
    container.eqn3()
elif ansr == 4:
    container.eqn1()
    container.eqn2()
    container.eqn3()
else:
    print("Invalid response!")