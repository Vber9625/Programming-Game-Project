import os
from random import randint
from time import sleep as wait


# Makes the console empty
def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# Determines whether or not the user made a valid selection.
def selectionValidity(number, maximum):
    if not number.isnumeric():
        print("You must make a valid selection")
        wait(1)
        return False
    else:
        number = int(number)
        if number <= 0:
            print("You must make a valid selection")
            wait(1)
            return False
        elif number > maximum:
            print("You must make a valid selection")
            wait(1)
            return False
        else:
            wait(1)
            return True


global balance
balance = 100
betValues = [5, 10, 25, 50, 100]
gameCount = 0


# Has the user make a bet in varying values.
def bet():
    betSelection = input("How much would you like to bet?\n1: $5\n2: $10\n3: $25\n4: $50\n5: $100\nSelection: ")
    betConfirmation = False
    while not betConfirmation:
        if not selectionValidity(betSelection, 5):
            clear()
            print("Your current balance is $", balance)
            betSelection = input("How much would you like to bet?\n1: $5\n2: $10\n3: $25\n4: $50\n5: $100\nSelection: ")
        else:
            betSelection = int(betSelection)
            if betValues[betSelection - 1] > balance:
                print("You don't have enough money to bet this.")
                wait(1)
                clear()
                print("Your current balance is $", balance)
                betSelection = input(
                    "How much would you like to bet?\n1: $5\n2: $10\n3: $25\n4: $50\n5: $100\nSelection: ")
            else:
                betConfirmation = True
                return betValues[betSelection - 1]


# Introduces the user to the game.
def intro():
    print(
        "Hello and welcome to Higher or Lower! In this game you will bet whether or not a number between 0 and 100 ("
        "not inclusive) will increase or decrease!")
    gameSelection = input("Enter anything to continue! ")
    if len(gameSelection) >= 0:
        game()


# The actual game itself.
def game():
    global balance
    global randomNumber1
    global gameCount
    clear()
    print("Your current balance is $", balance)
    userBet = bet()
    print("You have bet $", userBet)
    clear()
    randomNumber1 = randint(1, 99)
    print("The number is", randomNumber1, )
# Has the user make a choice on whether or not the number will increase or decrease.
    choice = input("Will the number be:\n1: Higher\nor\n2: Lower?\nSelection: ")
    choiceConfirmation = False
    while not choiceConfirmation:
        if not selectionValidity(choice, 2):
            clear()
            choice = input("Will the number be:\n1: Higher\nor\n2: Lower?\nSelection: ")
        else:
            choiceConfirmation = True
            choice = int(choice)
# Creates a second random number and determines whether it is higher or lower than the previous number.
        randomNumber2 = randint(1, 99)
        if randomNumber2 == randomNumber1:
            randomNumber2 = randint(1, 99)
        elif randomNumber2 > randomNumber1:
            correctChoice = 1
        elif randomNumber2 < randomNumber1:
            correctChoice = 2
        print("The new number is", randomNumber2)
# Checks if the user guessed correctly and rewards or punishes them.
        if choice == correctChoice:
            print("You guessed correctly and earned $", userBet, "!")
            balance = balance + userBet
            wait(1)
            game()
        elif choice != correctChoice:
            print("Sorry, you guess incorrectly and lost $", userBet, ".")
            balance = balance - userBet
            wait(5)
            randomNumber1 = randomNumber2
            gameCount = gameCount + 1
            if balance == 0:
                clear()
                return print("You lost all of your money.\nGame Over")
            else:
                game()


intro()
