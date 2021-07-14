#swap the case of lower to upper and vice versa
def alternateCase(s):
#    print(s.swapcase())
    y=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    z=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    for x in s:
        if x in y:
            s = x.lower()
        elif x in z:
            s = x.upper()
        print(s, end='')
alternateCase("lower       UPPER")