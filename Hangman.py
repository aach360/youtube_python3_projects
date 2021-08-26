print("You are in your house and about to eat lunch from outside.")
food = input("You can eat a (sandwich) or drink (soda).")
if food == "sandwich":
   print ("You entered in another dimension and a giant gorilla is chasing you.")
   act  = input("(run/hide)")
   if act == "run":
      print("The gorrilla is gaining on you but on your right you see a village and on your left you see a cave.")
      dir = input ("(right/left)")
      if dir == "right":
         print ("The villagers own the gorilla and help you escape. They give you a choice of soda or sandwich")
         food2 = input("(sandwich/soda)")
         if food2 == "sandwich":
            print("You returned back to your home. YOU WON!")
         elif food2 == "soda":
            print("You were poisend. LEARN FROM YOUR MISTAKES!")
         else:
            print("Invalid input. You lost")
      elif dir == "left":
         print("The cavemen thought you were and intruder and killed you")
      else:
         print("Invalid input. You lost")
   elif act == "hide":
      print ("The gorilla spots you out and eats you.")
   else:
      print("Invalid input. You lost")
elif food == "soda":
   print("You were poisoned. You lost")
else:
   print("Invalid input. You lost")