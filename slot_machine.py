"""
Play the Slot machine! Deposit your money, place your bet in increments of $.05 up to $.50, 
and pull the lever! Match 3 symbols and win! 

@@@=2x your bet
$$$=4x your bet
***=8x your bet
777=Win the jackpot!

"""
import random
import time


symbols=('@', '$', '*', '7', '%', '#', '^')

def pullLever(x):
    prize=[]
    for x in range(0, 3):
        prize.append(random.choice(symbols))
    return (prize)

jackpot=0
balance=0
balance=float(input("Deposit money to play the slot machine! "))
while balance>0:
    x=0
    jackpot+=10
    print(balance,"  This is your balance")
    print("Jackpot is at ", jackpot)
    bet=float(input("Place your bet! "))
    print()
    if bet>balance:
        i=input("Insufficient funds. Use remaining balance for bet? Y/N :")
        if i=="y":
            print("Your bet will be ", balance)
            bet=balance
        else:
            continue
    prize=''.join(pullLever(x))
    time.sleep(.5)
    print(prize)
    if prize=='@@@':
        print("Hey! You won ",(bet*2))
        print('------------------------')
        balance=balance+(bet*2)
    elif prize=='$$$':
        print("Whoa! You won ",(bet*4))
        print('------------------------')
        balance=balance+(bet*4)
    elif prize=='***':
        print("Yowza! You won ",(bet*8))
        print('------------------------')
        balance=balance+(bet*8)
    elif prize=='777':
        print("DING DING DING DING DING!!!! YOU WON THE JACKPOT OF ",jackpot)
        print('------------------------')
        balance=balance+jackpot
    else:
        balance=balance-bet
        print("Better luck next time!")
        print('------------------------')