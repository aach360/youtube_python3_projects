'''
You were driving and you realise that your fuel is running out
nearest pump is 50 miles away
Your car runs on about 25 miles per gallon
There are 2 gallons left.
'''
def zero_fuel(distance_to_pump, mpg, fuel_left):
    a = mpg*fuel_left
    if a >= distance_to_pump:
        return True
    else: 
        return False