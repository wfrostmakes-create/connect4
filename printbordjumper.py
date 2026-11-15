import printbord
def print_start():
    printbord.print_start()
def addnames():
    printbord.addnames()
    # player1 = (config.player1)
    # player2 = (config.player2)
def print_bord(board):
    printbord.print_bord(board)
def player_move(player, retry):
    move, retry = printbord.player_move(player, retry)
    return move, retry