#given a number (n) returns the n-th number in the Fibonacci Sequence. 
#the first two numbers in the Fibonacci sequence are 0 and 1, and each subsequent number is the sum of the previous two.
def nth_fib(n): 
    ans0 = 0
    ans1 = 1
    if n < 0:
        print("Something is Wrong")
    elif n == 0:
        return 0
    elif n == 1:
        return ans0
    else: 
        for x in range(2,n):
            ans3 = ans0 + ans1 
            ans0 = ans1 
            ans1 = ans3 
        return ans1