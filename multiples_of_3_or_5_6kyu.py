# Returns the sum of all the multiples of 3 or 5 below the number passed in.
#IN :10 -> x5: 5 -> x3: 3, 6 and 9. -> FIND THE SUM -> OUT: 23.
def solution(number):
    a=int(input("Enter multiple 1: "))
    b=int(input("Enter multiple 2: "))
    #Defining variables for further use.
    x = 0
    xlist=[]
# Iterating through a while loop to restrict the x value to be greater than the highest number.
    while x < number:
        # Adding a multiple of 3 each time
        x = x+a
        # make sure that it dosen't return a value above the number.
        if x >= number:
            break
        # Add the value into a list.
        xlist.append(x)
            # Same thing as above but for multiples of 5
    y = 0
    ylist=[]
    while y < number:
        y = y+b
        if y >= number:
            break
        ylist.append(y)
    # combine both lists of multiples of 5, 3.
    comb = ylist + xlist
    #remove duplicate numbers (multiples of 3 and 5)
    fin = set(comb)
        # Add all values in final list.
    ans = sum(fin)
    # print the answers
    print (ans)
solution(10)
