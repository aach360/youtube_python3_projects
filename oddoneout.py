# Find the oodd number out in the list and return its index ex: [7, 7, 7, 8, 7, 7, 7, 7] 8 is the odd number
def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            #list.count counts how many times a spesific value appers.
            return x
#https://www.codewars.com/kata/57f609022f4d534f05000024/solutions/python/me/best_practice