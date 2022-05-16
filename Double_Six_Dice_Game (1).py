from random import randint 
from time import sleep 

class Dice:
    def __init__(self,player1,player2):
        self.player2 = player2 
        self.player1 = player1


    def roll_dice(self, player):
        dice1 = 0 
        dice2 = 0 
        attempt = 0 
        while dice1 + dice2 != 12:
            dice1 = randint(1,6)
            dice2 = randint(1,6)
            attempt += 1 
            if dice1 + dice2 !=12:
                print("{0} is rolling the dices.\nFirst dice is {1} and second dice is {2}".format(player,dice1,dice2))
            else:
                print("{0} is rolling the dices.\nFirst dice is {1} and second dice is {2} \n {3} got Double Six Dices in {4} attempts".format(player,dice1,dice2,player,attempt))
            sleep(0.2)

        return attempt
    def paly(self):
        a = self.roll_dice(self.player1)
        while True :
            k = input("Press s to start your turn {0}: ".format(self.player2))
            if k.lower() == "s":
                b = self.roll_dice(self.player2)
            if k.lower() != "s":
                print("Press s to start, please!")
                continue 
            if b != 0:
                break 

        if a < b:
            print("{0} did {1} attempts {2} did {3}\n {4} won the game, congratulations!!!".format(self.player1,a,self.player2,b,self.player1))

        elif a > b:
            print("{0} did {1} attempts {2} did {3}\n {4} won the game, congratulations!!!".format(self.player2,b,self.player1,a,self.player2))

        else:
            print("{0} did {1} attempts {2} did {3]}\n the game ended in a draw, congratulations!!!".format(self.player2,b,self.player1,a))
print("""
            ___________________________
            |                          |
            |   Double Six Dice Game   |
            |__________________________|\n""")

a = Dice(input("Player1 enter your name: "),input("Player2 enter your name: "))
a.paly()
while True:
    p = input("Press r to restart the game and q to quit: ")
    if p == "r":
        a.paly()
    if p == "q":
        print("Thank for playing our game!!!")
        break 
    if p != "r":
        print("Press r to restart the game")
        continue 