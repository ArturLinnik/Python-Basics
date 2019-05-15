
import random

print("Welcome to the 'Rock Paper Scissors' game")

start = "yes"   # Variable to play again

name = str(input("Your name: "))

while start == "yes":
    
    your_choose = int(input("Press '1' to choose 'Rock', press '2' to choose 'Paper' and '3' to choose 'Scissors': "))
    comp_choose = random.randint(1,3)   # Random int between 1 and 3

    if (your_choose in range(1,4) and comp_choose in range(1,4)):
        if your_choose != comp_choose:
            if (your_choose == 1 and comp_choose == 2):
                print("Computer wins!")
            elif (your_choose == 1 and comp_choose == 3):
                print(name + " wins!")
            elif (your_choose == 2 and comp_choose == 1):
                print(name + " wins!")
            elif (your_choose == 2 and comp_choose == 3):
                print("Computer wins!")
            elif (your_choose == 3 and comp_choose == 1):
                print("Computer wins!")
            elif (your_choose == 3 and comp_choose == 2):
                print(name + " wins!")
        elif your_choose == comp_choose:
            print("It's a tie.")
    else:
        print ("You must choose a number between '1' and '3'")
    
    start = str(input("Do you want to play again? Enter 'yes': "))


    

    
