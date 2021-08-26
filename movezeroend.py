'''
def move_zeros(array):
    y = 0
    for n in array:
        for x in n:
            if x == 0:
                y +=1
                array.remove(x)
    for i in range(y):
        array.append(0)
    print (array)
move_zeros([9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def is_palindrome(s):
    list = s.split()
    print(s)
    ans = ""
    if ans == s:
        return True
    else:
        return False
is_palindrome("yey")
'''
def ye (word):
    param = "`~!@#$%^&*()_+ -={}|[]\:;<>?,./'"
    a = 0
    for x in param:
        # Turn word into list to use "in"
        if x in word:
            a += 1
            break
    if "" == word:
        return False
    elif a == 1:
        return False
    else:
        return True
ye ("")
