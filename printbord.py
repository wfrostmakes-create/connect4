player1 = ""
player2 = ""
def print_start():
    print("Game started!")
def addnames():
    global player1, player2
    player1 = input("Enter name for Player 1: ")
    player2 = input("Enter name for Player 2: ")
    print(f"Player 1: {player1}, Player 2: {player2}")
def print_bord(board):
    print("Current game board:")
    columns = "ABCDEFG"
    rows = range(7, 0, -1)
    cell_width = 3
    border = "  +" + "+".join("-" * cell_width for _ in columns) + "+"

    print(" " * (3 + cell_width // 2) + (" " * cell_width).join(columns))
    print(border)

    for row in rows:
        cells = []
        for column in columns:
            pieces = board.get(column, "")
            piece = pieces[row - 1] if row <= len(pieces) else " "
            cells.append(f"{piece:^{cell_width}}")
        print(f"{row}  " + " ".join(cells))
        print(border)
def player_move(player, retry):
    global player1, player2
    if player == "Player 1":
        playerr = player1 
    else:
        playerr = player2

    muves = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    while True:
        if retry == True:
            print("Column is full, please choose another column.")
        move = input(f"{playerr}, choose your column (e.g., A): ")
        
        if move not in muves:
            print("Invalid move. Please try again.")
            continue
        return move,retry
        