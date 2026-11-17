import printbordjumper
import funintro
import os

'0000'

board = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []}
funintro.print_intro()
printbordjumper.print_start()
printbordjumper.addnames()
printbordjumper.print_bord(board)
while True:
    printbordjumper.print_bord(board)
    # Player 1 move
    retry = False
    while True:
        (move, retry) = printbordjumper.player_move("Player 1", retry)
        # print(f"Player 1 chose column: {move}")
        # print(f"Retry status: {retry}")
        if move not in board:
            print("Invalid move. Please try again.")
            retry = True
            continue
        elif len(board[move]) >= 7:
            print("Column is full, please choose another column.")
            retry = True
            continue
        else:
            board[move].append('X')
            break
    if check_win(board):
        print("Player 1 wins!")
        exit()
    # player 2 move
    os.system('cls')
    printbordjumper.print_bord(board)
    retry = False
    while True:
        (move, retry) = printbordjumper.player_move("Player 2", retry)
        # print(f"Player 2 chose column: {move}")
        # print(f"Retry status: {retry}")
        if move not in board:
            print("Invalid move. Please try again.")
            retry = True
            continue
        elif len(board[move]) >= 7:
            print("Column is full, please choose another column.")
            retry = True
            continue
        else:
            board[move].append('O')
            break
    if check_win(board):
        print("Player 2 wins!")
        exit()
    os.system('cls')
    
