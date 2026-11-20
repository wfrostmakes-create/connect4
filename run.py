import add
import printbordjumper
import funintro
import os
import winCheck
'0000'
board = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []}
add.show_ad()
funintro.print_intro()
printbordjumper.print_start()
printbordjumper.addnames()
#printbordjumper.print_bord(board)
while True:
    printbordjumper.print_bord(board)
    # Player 1 move
    retry = False
    while True:
        (move, retry) = printbordjumper.player_move("Player 1", retry)
        # print(f"Player 1 chose column: {move}")
        # print(f"Retry status: {retry}")
        # check if move is valid
        if move not in board:
            print("Invalid move. Please try again.")
            retry = True
            continue
        # column checker
        elif len(board[move]) >= 7:
            print("Column is full, please choose another column.")
            retry = True
            continue
        # add the move to the board
        else:
            board[move].append('X')
            break
    #check for wins
    if winCheck.check_win(board):
        printbordjumper.print_winner("Player 1")
        exit()
    # player 2 move
    os.system('cls')
    printbordjumper.print_bord(board)
    retry = False
    while True:
        (move, retry) = printbordjumper.player_move("Player 2", retry)
        # print(f"Player 2 chose column: {move}")
        # print(f"Retry status: {retry}")
        # check if move is valid
        if move not in board:
            print("Invalid move. Please try again.")
            retry = True
            continue
        # column checker
        elif len(board[move]) >= 7:
            print("Column is full, please choose another column.")
            retry = True
            continue
        # add the move to the board
        else:
            board[move].append('O')
            break
    # check for wins
    if winCheck.check_win(board):
        printbordjumper.print_winner("Player 2")
        exit()
    os.system('cls')