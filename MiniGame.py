
import random

print("Welcome to the luck room")
UserWallet = 1000

def DiceRoll():
    print("\nYou have picked dice roll.")
    while True:
        global UserWallet 
        UserBet = input("Pick how much you want to bet!\n")
        if UserBet.isdigit():
            if float(UserBet) > UserWallet:
                print("\nYou are betting more money that you have, try again.")
                continue
            else:
                UserWallet -= float(UserBet)
            break
        else:
            print("\nYour bet amount was not a proper number.")

    print("\nYou have picked to bet $" + str(UserBet) + ".00")
    while True:
        UserPick = input("Pick a number between 1 and 6\n")
        if UserPick.isdigit():
            if int(UserPick) in range(1, 7):
                DiceRollResult = random.randrange(1, 7)
                break
            else:
                print("\nYou have picked a number outside 1 and 6.")

        else:
            print("\nValue invalid")

    print("\nThe dice roll was: " + str(DiceRollResult))
    if int(UserPick) == int(DiceRollResult):
        UserBet = float(UserBet) * 6
        UserWallet += float(UserBet)
        print("Congratulations, You have correctly picked the dice number!\n")
    else: 
        print("Bad luck, you guessed wrong!\n")

    print("You know have: $" + str(UserWallet))

    print("\nWould you like to play again?")
    while True:
        UserContinue = input("To play again, type: 'again'. To select a new game, type: 'home'\n").strip().lower()
        if UserContinue == "again":
            return "again"
        elif UserContinue == "home":
            return "home"
        else:
            print("\nThere is no option for: " + UserContinue)

def GamePick():
    global Game
    Game = input("\nChoose what game you would like to play:\n1) Dice roll\n2) Coin flip\n3) Wheel spin\n4) Card pick\n").strip().lower()

while True:
    GamePick()
    if Game == "dice roll" or Game == "1":
        while True:
            result = DiceRoll()
            if result == "again":
                continue
            elif result == "home":
                break

    elif Game == "coin flip" or Game == "2":
        pass

    elif Game == "wheel spin":
        pass

    elif Game == "card pick":
        pass

    else:
        pass
        