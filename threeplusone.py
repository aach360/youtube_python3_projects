def threexplusone(num):
    y=0
    while num != 1:
        if num % 2 == 0:
            num = num/2
            y+=1
            
        else:
            num = num *3
            num = num + 1
            y+=1
            
    print(y)
threexplusone(69)