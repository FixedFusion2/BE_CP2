tic.py is clean — no bare function call at the bottom. ✓
But it has two bugs that will cause problems:

exit() in restart() — kills your entire GUI
game() is never called at the end of tic_tac_toe() — the game never actually starts

Here's the fixed file:
pythonimport time
import random

def tic_tac_toe():
    print("Hello.")
    time.sleep(1)
    print("")
    print("Welcome to TicTacToe, a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three O's or three X's drawn in the spaces of a grid of nine squares.")
    time.sleep(2)
    print("")

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def restart():
        nonlocal board
        play = input("\nWant to play again? (Say lowercase yes or no.) ")
        if play == "no":
            return  # ← Fixed: was exit(), which kills your entire GUI
        else:
            board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            game()

    def win():
        if board[0]==board[1]==board[2] !="":
            if board[0] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()
        if board[3]==board[4]==board[5] !="":
            if board[3] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()
        if board[6]==board[7]==board[8] !="":
            if board[6] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()
        if board[0]==board[4]==board[8] !="":
            if board[0] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()
        if board[2]==board[4]==board[6] !="":
            if board[2] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()
        if board[0]==board[3]==board[6] !="":
            if board[0] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()
        if board[1]==board[4]==board[7] !="":
            if board[1] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()
        if board[2]==board[5]==board[8] !="":
            if board[2] == "X":
                print("Congratulations! You won one of the easiest game ever!")
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
            restart()

    def space_check(plr, sym):
        while True:
            if board[plr-1] != "O" and board[plr-1] != "X":
                board.pop(plr-1)
                board.insert(plr-1, sym)
                break
            else:
                if sym == "X":
                    print("That spot was taken.")
                    plr = int(input("Where do you want to place your 'X': "))
                else:
                    plr = random.randint(1, 9)

    def game():
        while True:
            print(""+board[0]+" | "+board[1]+" | "+board[2]+"\n---------\n"+board[3]+" | "+board[4]+" | "+board[5]+"\n---------\n"+board[6]+" | "+board[7]+" | "+board[8]+"")
            print("")
            choice = int(input("Where would you like to place your 'X'?\n(Please Enter a Number): "))
            space_check(choice, "X")
            win()
            computerChoice = random.randint(1, 9)
            space_check(computerChoice, "O")
            win()

    game()  # ← Fixed: was missing, so the game never started

if __name__ == "__main__":
    tic_tac_toe()