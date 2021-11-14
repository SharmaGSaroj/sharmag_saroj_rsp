def winlose(status):
    print("you " + status)

    choice = input("do you want to play again? y/n: ")

    if choice == "n":
        print("========= see ya! (loser) ==========")
        exit()
    elif choice == "y":
        playerLives = 5
        computerLives = 5
        player = False