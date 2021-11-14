from  random import randint
import winlose
import gameplayer

while gameplayer.player is False:

    gameplayer.player= input("Choose rock , paper or scissor:")
    gameplayer.computer= gameplayer.choices[randint(0,2)]

    print("player chose:" + gameplayer.player)

    print("computer chose:"+ gameplayer.computer)
    if gameplayer.player == gameplayer.computer:
        print("tie")
    elif (gameplayer.player == "rock"):
        if(gameplayer.computer =="paper"):
            print("You Lose")
            gameplayer.playerlives = gameplayer.playerlives - 1
        else:
            print("You win")
            gameplayer.computerlives = gameplayer.computerlives - 1
    elif (gameplayer.player == "paper"):
        if(gameplayer.computer =="scissor"):
            print("You Lose")
            gameplayer.playerlives = gameplayer.playerlives - 1
        else:
            print("YOu win")
            gameplayer.computerlives = gameplayer.computerlives - 1
        
    elif (gameplayer.player == "scissor"):
        if(gameplayer.computer =="rock "):
            print("You Lose")
            gameplayer.playerlives = gameplayer.playerlives - 1
        else:
            print("YOu win")
            gameplayer.computerlives = gameplayer.computerlives - 1
        

    print("computerlives:" + str(gameplayer.computerlives))
    print("playerlives:" + str(gameplayer.playerlives))


    if gameplayer.playerlives == 0:
        winlose.winlose("lost")

    elif gameplayer.computerlives == 0:
        winlose.winlose("won")

    gameplayer.player = False
