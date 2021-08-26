sign = input("sign up y/n: ")
if sign == "y":
    user = input("Create Username: ")
    passw = input("Create Password: ")
    log = input("Login y/n: ")
    if log == "y":
        euser = input("enter username: ")
        epass = input("enter password: ")
        trys = 0
        while epass != passw or euser != user:
            print ("Invalid Username or password")
            euser = input("enter username: ")
            epass = input("enter password: ")
            trys += 1
            if trys == 3:
                print("Too many unsuccesful attempts. Account Locked.")
                break
        else:
            print("Authentication successful!")
    else:
        print("Okay Byeeee!")
else:
    print("Okay Byeeee!")