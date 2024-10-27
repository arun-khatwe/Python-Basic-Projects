import random
guesses=0
low = 0
high = 100
userinput = int(input("Enter the number: "))
num = random.randint(0, 100)
while True:
    guess = int(input())
    guess += 1
    if userinput>num:
        print("You gotta think lower")
        high = low + 1
    
    elif userinput  < num:
        print("You gotta think higher")
        low = high - 1
            
    else:
        print("Congratulations")
    print("Press a for hint & b to quit")
    if guesses<5:
        print("You're Lucky Toda!!")
        break

    