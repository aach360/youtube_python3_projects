import random
comp = random.randint(1, 3)
b = int(input("Choose 1 for Rock, 2 for Paper, or 3 for Scissors: "))
# 1 = rock, 2 = paper, 3 = scissors
while comp == b:
    print("")
    print("We tied. Try again.")
    b = int(input("Choose 1 for Rock, 2 for Paper, or 3 for Scissors: "))
    comp = random.randint(1, 3)
if comp == 1 and b == 2 or comp == 2 and b == 3 or comp == 3 and b == 1:
    print("You Won")
else:
    print("I won")