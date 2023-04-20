from random import randint

def create_board(b_size):
    """
    Creates two dimensional list that represents the game board of the battleship game.
    """
    board = []
    for i in range(b_size):
        board.append([0] * b_size)
    return board

def print_board(board):
    """
    Prints game board to the terminal
    """
    for row in board:
        print(" ".join(row))