"""
Play the Slot machine! Deposit your money, place your bet in increments of $.05 up to $.50, 
and pull the lever! Match 3 symbols and win! 

@@@=2x your bet
$$$=4x your bet
***=8x your bet
777=Win the jackpot!
ope
"""
import random


symbols=('@', '$', '*', '7', '%', '#', '^')

def pullLever(bet):
    prize=[]
    for x in range(0, 3):
        prize.append(random.choice(symbols))
    return (prize)

jackpot=0
balance=0
balance=float(input("Deposit money to play the slot machine! "))
while balance>0:
    jackpot+=10
    print(balance,"  This is your balance")
    bet=float(input("Place your bet!"))
    prize=''.join(pullLever(bet))
    print(prize)
    if prize=='@@@':
        print("Hey! You won ",(bet*2))
        balance=balance+(bet*2)
    elif prize=='$$$':
        print("Whoa! You won ",(bet*4))
        balance=balance+(bet*4)
    elif prize=='***':
        print("Yowza! You won ",(bet*8))
        balance=balance+(bet*8)
    elif prize=='777':
        print("DING DING DING DING DING!!!! YOU WON THE JACKPOT OF ",jackpot)
        balance=balance+jackpot
    else:
        balance=balance-bet
        print("Better luck next time!")