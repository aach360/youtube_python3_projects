import math
def find_next_square(sq):
    sqrt = math.sqrt(sq)
    sqrt = str(sqrt)
    if '.0' in sqrt:
        sqrt = sqrt[:-2]
        sqrt = int(sqrt)
        sqrt += 1
        a = sqrt*sqrt
        print(a)
    else:
        print(-1)
find_next_square(144)
#https://www.codewars.com/kata/56269eb78ad2e4ced1000013/solutions/python/all/newest