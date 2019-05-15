
print("Welcome to the 'Rock Paper Scissors' game")

start = "yes"   # Variable to play again

name1 = str(input("First player's name: "))
name2 = str(input("Second player's name: "))

while start == "yes":
    print("Press '1' to choose 'Rock', press '2' to choose 'Paper' and '3' to choose 'Scissors'")

    choose1 = int(input(name1 + "'s choose: "))
    choose2 = int(input(name2 + "'s choose: "))

    if (choose1 in range(1,4) and choose2 in range(1,4)):
        if choose1 != choose2:
            if (choose1 == 1 and choose2 == 2):
                print(name2 + " wins!")
            elif (choose1 == 1 and choose2 == 3):
                print(name1 + " wins!")
            elif (choose1 == 2 and choose2 == 1):
                print(name1 + " wins!")
            elif (choose1 == 2 and choose2 == 3):
                print(name2 + " wins!")
            elif (choose1 == 3 and choose2 == 1):
                print(name2 + " wins!")
            elif (choose1 == 3 and choose2 == 2):
                print(name1 + " wins!")
        elif choose1 == choose2:
            print("It's a tie.")
    else:
        print ("You must choose a number between '1' and '3'")
    
    start = str(input("Do you want to play again? Enter 'yes'"))