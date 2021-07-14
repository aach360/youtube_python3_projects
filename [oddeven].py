#add all values of a list and determine if it is odd or even
def odd_or_even(list):
    fin = 0
    for x in list:
        fin = fin + x
    if fin % 2 == 0:
        return"even"
    else:
        return "odd"
print(odd_or_even([1, 2, 3]))