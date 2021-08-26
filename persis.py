#which is the number of times you must multiply the digits in num until you reach a single digit.
def persistence(n):
    a = 0
    while n > 9:
        b = 1
        for x in str(n):
            b = b * int(x)
        a = a + 1
        n = b
    return a
