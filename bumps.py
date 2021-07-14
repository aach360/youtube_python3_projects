#car can surrvive 15 bumps _ is flat n is bump.
def bumps(road):
    b = 0
    for x in road:
        if x == "n":
            b+=1
    if b > 15:
        print("Car Died")
    else:
        print("You continue on your Journy!")
bumps("nnnnnnnnnnnnnnnn")