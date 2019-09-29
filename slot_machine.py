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
import sys


symbols=('@', '$', '*', '7', '%', '#', '^')

def pullLever(x):
    prize=[]
    for x in range(0, 3):
        prize.append(random.choice(symbols))
    return (prize)

jackpot=0
balance=round(0, 2)
while balance==0:
    try:
        balance=float(input("Deposit money to play the slot machine! "))

    except ValueError:
        print("You can't deposit that!")

while balance>0:
    x=0
    jackpot+=10
    print(balance,"  This is your balance.")
    print("Jackpot is at ", jackpot)
    bet=float(input("Place your bet! "))
    print('------------------------')
    print()
    if bet>balance:
        i=input("Insufficient funds. Use remaining balance for bet? Y/N :")
        if i=="y" or i=="yes" or i=="Y":
            print("Your bet will be ", balance)
            print()
            print('------------------------')
            print()
            bet=balance
        else:
            continue
    
    
    
    #time.sleep(.5)
    
    for x in range(15):
        prize1=random.choice(symbols)
        prize2=random.choice(symbols)
        prize3=random.choice(symbols)

        out=(prize1 + prize2 + prize3)
        sys.stdout.write(str('\r'+'     '+ prize1+ '   '+ prize2+ '   '+ prize3+ '     '))
        sys.stdout.flush()
        time.sleep(.1)
    
    prize=str(out)

    if '@@@' == prize:
        print("\nHey! You won ",(bet*2))
        print()
        print('------------------------')
        balance=round((balance+(bet*2)), 2)
    elif '$$$' == prize:
        print("\nWhoa! You won ",(bet*4))
        print()
        print('------------------------')
        balance=round(balance+(bet*4), 2)
    elif '***' == prize:
        print("\nYowza! You won ",(bet*8))
        print()
        print('------------------------')
        balance=round(balance+(bet*8), 2)
    elif '777' == prize:
        print("\nDING DING DING DING DING!!!! \nYOU WON THE JACKPOT OF ",jackpot)
        print()
        print('------------------------')
        balance=round((balance+jackpot), 2)
    elif '@' in prize and '$' in prize and '*' in prize:
        print("\nYou won your bet! Not bad!")
        print()
        print('------------------------')
        balance=round((balance+bet), 2)
    else:
        balance=round((balance-bet), 3)
        print("\nBetter luck next time!")
        print()
        print('------------------------')