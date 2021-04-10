def prompt (Q, A1, A2, A3, A4, ans):
    print(Q)
    print("Answer choices: ")
    print(f"1. {A1}\n2. {A2}\n3. {A3}\n4. {A4}")
    user = int(input("Choose one number choice: "))
    if ans == user:
        print("Correct\n")
    else:
        print("Incorrect\n")
prompt("What is 2+2 ", "3", "8", "2", "4", 4)