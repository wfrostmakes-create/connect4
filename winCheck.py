# win check code
def check_win(board):
    # vertical check
    for column in board:
        pieces = board[column]
        for i in range(len(pieces) - 3):
            if pieces[i:i + 4] == ['X', 'X', 'X', 'X']:
                return True
            elif pieces[i:i + 4] == ['O', 'O', 'O', 'O']:
                return True
    # horizontal check
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
    # for col in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    #     for row in range(7):
    #         if row < len(board[col]):
    #             piece = board[col][row]
    #             if piece == 'X':
    #                 count = 1