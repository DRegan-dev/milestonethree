from random import randint

def create_board(b_size):
    """
    Creates two dimensional list that represents the game board of the battleship game.
    """
    board = []
    for i in range(b_size):
        board.append([0] * b_size)
    return board
