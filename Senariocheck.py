'''
You were driving and you realise that your fuel is running out
nearest pump is 50 miles away! 
Your car runs on about 25 miles per gallon
There are 2 gallons left.
Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return true (1 in Prolog) if it is possible and false (0 in Prolog) if not. The input values are always positive.
'''
def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg*fuel_left
    if a >= distance_to_pump:
        return True
    else: 
        return False