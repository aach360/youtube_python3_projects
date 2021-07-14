'''
return multiplication table for number 1-10.
This string format:
1 * 5 = 5
2 * 5 = 10
3 * 5 = 15
4 * 5 = 20
5 * 5 = 25
6 * 5 = 30
7 * 5 = 35
8 * 5 = 40
9 * 5 = 45
10 * 5 = 50
'''
def multi_table(number):
    x = 1
    while x != 11:
        sol = x * number
        print(f"{x} * {number} = {sol}")
        x = x+1
        if x == 11:
            break 
multi_table (1678)