# TE 2nd Tic-Tac-Toe in Pseudocode.
import time
#TicTacToe, a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three O's or three X's drawn in the spaces of a grid of nine squares.
def tic_tac_toe():
    print("Hello.")
    time.sleep(1)
    print("")
    print("Welcome to TicTacToe, a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three O's or three X's drawn in the spaces of a grid of nine squares.")
    time.sleep(2)
    print("")
    #Imports needed: Random
    import random
    #Variables needed: Board
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    #Restart function that lets the player choose to play again
    def restart():
        board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        play = input("\nWant to play again? (Say lowercase yes or no.) ")
        if play == "no":
            exit()
        else:
            game()
        
    #Function that checks to see if the game is over(Win, Lose, Draw)
    def win():
        if board [0]==board[1]==board[2] !="":
            if board[0] == "X":
                print("Congratulations! You won one of the easiest game ever!")     
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
        if board [3]==board[4]==board[5] !="":
            if board[3] == "X":
                print("Congratulations! You won one of the easiest game ever!")
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
        if board [6]==board[7]==board[8] !="":
            if board[6] == "X":
                print("Congratulations! You won one of the easiest game ever!")
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
        if board [0]==board[4]==board[8] !="":
            if board[0] == "X":
                print("Congratulations! You won one of the easiest game ever!")
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
        if board [2]==board[4]==board[6] !="":
            if board[2] == "X":
                print("Congratulations! You won one of the easiest game ever!")
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
        if board [0]==board[3]==board[6] !="":
            if board[0] == "X":
                print("Congratulations! You won one of the easiest game ever!")
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
        if board [1]==board[4]==board[7] !="":
            if board[1] == "X":
                print("Congratulations! You won one of the easiest game ever!")
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
        if board [2]==board[5]==board[8] !="":
            if board[2] == "X":
                print("Congratulations! You won one of the easiest game ever!")
                restart()
            else:
                print("You Lost\n\n Honestly\n\n How Did You Lose?")
                restart()
    #Function that checks to see if space is available (can also place in the space)
    def space_check(plr,sym):
        while True:
            if board[plr-1] != "O" and board[plr-1] != "X":
                board.pop(plr-1)
                board.insert(plr-1, sym)
                break
            else:
                if sym == "X":
                    print("That spot was taken.")
                    plr = int(input("Where do you want to place your 'X'"))  
                else:
                    plr = random.randint(1,9)
    #Function to run the game
    def game():
        while True:
        
    #Put this in a while loop
    #Display the board
            print(""+board[0]+" | "+board[1]+" | "+board[2]+"\n---------\n"+board[3]+" | "+board[4]+" | "+board[5]+"\n---------\n"+board[6]+" | "+board[7]+" | "+board[8]+"")
            print("")
    #Let player select where to place on the board
            choice = int(input("Where would you like to place your 'X'?\n(Please Enter a Number): "))
    #See if the space is availabe
            space_check(choice, "X")
    #Check if the game is over
            win()
    #Computers turn
    #See if the space is availabe
            computerChoice = random.randint(1,9)
            space_check(computerChoice, "O")
    #Check if the game is over
            win()
tic_tac_toe()
    