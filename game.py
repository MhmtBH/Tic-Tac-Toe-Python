import os                               # The library we need to use the os.system("cls") command
import colorama                         # Colorama library is used to color text. 
from colorama import Fore , Style

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

currentPlayer = Style.BRIGHT + Fore.RED + "X" + Fore.WHITE  # First player
winner = None                                               # Winner status
gameRunning = True                                          # Game status

# print the game board --------------------------------------------
def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])


# take player input --------------------------------------------
def playerInput(board):   
    inp = int(input("\nEnter a number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = (currentPlayer)
    else:
        print("Player is already in that spot!")

    os.system('cls') # Code used to prevent image pollution


# check for win or tie --------------------------------------------

    #check for horizontal win
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
    
    #check for row win
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
    #check for diagonal win
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

    #check for tie
def checkTie(board):
    global winner
    if "-" not in board:
        print("Tie!\n")
        gameRunning = False

    #check for win
def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}\n")




# switch player --------------------------------------------
def switchPlayer():
    global currentPlayer
    if currentPlayer == Style.BRIGHT + Fore.RED + "X" + Fore.WHITE:
        currentPlayer= Style.BRIGHT + Fore.BLUE + "O" + Fore.WHITE
    else:
        currentPlayer= Style.BRIGHT + Fore.RED + "X" + Fore.WHITE


while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer() 


    