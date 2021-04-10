import time
x = int(input("Time to set the timer in sec: "))
while x:
    # // means to round down
    min = x // 60
    # % = when dividing, returns the remainder.
    sec = x % 60
    # Formating purposes. so that the for mat will be "00:00" an the first set = min . second set= sec
    timer = '{:02d}:{:02d}'.format(min, sec)
    # overwriting purposes. 
    print(timer, end="\r")
    # want 1 sec to pasS each time and decrease variable too
    time.sleep(1)
    x= x-1
print("BEEEP, BEEEP, BEEP time is up!!!")