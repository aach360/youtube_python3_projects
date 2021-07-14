def solution(number):
    x = 0
    xlist=[]
    while x < number:
        x = x+3
        if x >= number:
            break
        xlist.append(x)
    y = 0
    ylist=[]
    while y < number:
        y = y+5
        if y >= number:
            break
        ylist.append(y)
    comb = ylist + xlist
    fin = set(comb)
    print(fin)
    ans = sum(fin)
    print (ans)
solution(37)