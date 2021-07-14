
def solution(s):
    x=1
    a=2
    lenth=len(s)
    if lenth % 2 != 0:
        s=s+"_"
    for i in s:
        if x % 2 == 0:
            s=str(s)
            s=s.split(' ')
            print("with in loop")
            print(s)
        x+=1
    #sprint (s)
    print("b")
solution("abcdef")
