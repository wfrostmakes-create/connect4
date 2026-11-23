def check_win(board):
    columns = list(board)
    for column_index, column in enumerate(columns):
        for row, piece in enumerate(board[column]):
            if piece not in ("X", "O"):
                continue
            for column_step, row_step in ((1, 0), (0, 1), (1, 1), (1, -1)):
                for step in range(1, 4):
                    next_column = column_index + column_step * step
                    next_row = row + row_step * step
                    if (
                        next_column >= len(columns)
                        or next_row < 0
                        or next_row >= len(board[columns[next_column]])
                        or board[columns[next_column]][next_row] != piece
                    ):
                        break
                else:
                    return True
    return False
