# win check code
def check_win(board):
    # vertical check
    # looks for repeats in the string
    for column in board:
        pieces = board[column]
        for i in range(len(pieces) - 3):
            if pieces[i:i + 4] == ['X', 'X', 'X', 'X']:
                return True
            elif pieces[i:i + 4] == ['O', 'O', 'O', 'O']:
                return True
    # horizontal check
    #looks for repeats with the sam spot
    for row in range(7):
        for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            if row < len(board[col]):
                piece = board[col][row]
                if piece == 'X':
                    count = 1
                    for next_col in ['B', 'C', 'D', 'E', 'F', 'G']:
                        if next_col > col and row < len(board[next_col]) and board[next_col][row] == 'X':
                            count += 1
                            if count == 4:
                                return True
                        else:
                            break
                elif piece == 'O':
                    count = 1
                    for next_col in ['B', 'C', 'D', 'E', 'F', 'G']:
                        if next_col > col and row < len(board[next_col]) and board[next_col][row] == 'O':
                            count += 1
                            if count == 4:
                                return True
                        else:
                            break
    # diagonal check
    # left to right check
    for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        for row in range(7):
            if row < len(board[col]):
                piece = board[col][row]
                if piece == 'X':
                    count = 1
                    for i in range(1, 4):
                        nextCol = chr(ord(col) + i)
                        nextRow = row + i
                        if nextCol in board and nextRow < len(board[nextCol]) and board[nextCol][nextRow] == 'X':
                            count += 1
                            if count == 4:
                                return True
                        else:
                            break
    # right to left check
    for col in ['G', 'F', 'E', 'D', 'C', 'B', 'A']:
        for row in range(7):
            if row < len(board[col]):
                piece = board[col][row]
                if piece == 'X':
                    count = 1
                    for i in range(1, 4):
                        nextCol = chr(ord(col) - i)
                        nextRow = row + i
                        if nextCol in board and nextRow < len(board[nextCol]) and board[nextCol][nextRow] == 'X':
                            count += 1
                            if count == 4:
                                return True
                        else:
                            break
