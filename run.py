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

size = int(input("Enter board size: (Minimum size requirement:5) "))
if size < 5:
    size == 5

board = create_board(size)
battleship_row = randint(0, size - 1)
battleship_col = randint(0, size - 1)

for turn in range(6):
    print("Turn", turn + 1)
    guess_row = int(input("Guess Row(O-" + str(size -1) + "): ))
    guess_col = int(input("Guess Col(O-" + str(size -1) + "): ))

