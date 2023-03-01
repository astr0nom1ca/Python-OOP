import random

listicle = [1,2,3,4]

pick = random.choice(listicle)
if pick == 1:
    print("Dark Academia is " + str(pick))
elif pick== 2:
    print("Y2k is " + str(pick))
elif pick == 3:
    print("Chaotic Academia is " + str(pick))
else:
    print("All aesthetics are cool")

