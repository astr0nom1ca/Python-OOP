class results:
    def __init__(self,score):
        self.score = score

    def grades(self):
        if self.score >= 70 and self.score <= 100:
            print("Score:" + str(self.score))
            print("Grade: A")
        elif self.score >= 60 and self.score <= 69:
            print("Score:" + str(self.score ))
            print("Grade: B")
        elif self.score >= 50 and self.score <= 59:
            print("Score:" + str(self.score))
            print("Grade: C")
        elif self.score >= 45 and self.score <= 49:
            print("Score:" + str(self.score))
            print("Grade: D")
        elif self.score >= 0 and self.score <= 45:
            print("Score:" + str(self.score))
            print("Grade: F")
        else:
            print("Invalid Input!")

scor = int(input("Enter student score: "))

scores = results(scor)

scores.grades()






