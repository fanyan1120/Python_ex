import random

class game:
    def __init__(self):
        self.player = 1
        self.comp = 1
        self.label = ["Rock","Paper","Scissors"]
        pass

    def run(self):
        while(True):
            self.player = self.player_input()
            self.comp = self.comp_input()
            print "player %s" %(self.label[self.player - 1])
            print "computer %s" %(self.label[self.comp - 1])
            self.iswin(self.player,self.comp)
            pass

    def iswin(self,player,comp):
        if player == comp:
            print "Tie"
            return
        elif player > comp:
            if player == 3 and comp == 1:
                print "You lose"
                return
            else:
                print "You win"
                return
        else:
            if player == 1 and comp == 3:
                print "You win"
                return
            else:
                print "You lose"
                return

    def player_input(self):
        while(1):
            try:
                player = int(raw_input("Input 1 or 2 or 3:\n"))
                if player >= 1 and player <= 3:
                    return player
            except:
                print "Input Error, plese input 1, 2 or 3"

    def comp_input(self):
        return random.randint(1,3)

if __name__ == "__main__":
    print """
Hi guys, this script is named Rock Paper Scissors, you could play this game with PC"
In this game, 1 means Rock, 2 means Paper and 3 is Scissors
You could input 1, 2 or 3 after :
"""
    newgame = game()
    newgame.run()
