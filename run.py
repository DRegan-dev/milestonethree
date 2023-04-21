from random import randint

def create_board(b_size):
    """
    Creates two dimensional list that represents the game board of the battleship game.
    """
    board = []
    for i in range(b_size):
        board.append([0] * b_size)
    return board

print( "Welcome to Battleship!! \n")
print("Please input your guess using numbers only. Press enter to submit your guess.")



def print_board(board):
    """
    Prints game board to the terminal
    """
    for row in board:
        print(" ".join(row))
    
def get_input(prompt, minimum = None):
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print("Input must be at least {}".format(minimum))
                continue
            return value
        except ValueError:
            print("You must enter a number.")

size = int(input("Enter board size: (Minimum size requirement: 5) "))
if size < 5:
    size = 5

board = create_board(size)
battleship_row = randint(0, size - 1)
battleship_col = randint(0, size - 1)

for turn in range(0, 5):
    print("Turn", turn + 1)
    guess_row = get_input("Guess Row(O-" + str(size -1) + "): ")
    guess_col = get_input("Guess Col(O-" + str(size -1) + "): ")

    if guess_row < 0 or guess_row >= size or guess_col < 0 or guess_col >= size:
        print("Oops, you hit land")
        continue
    else:
        print("Missed me!!")
    
    if board[guess_row][guess_col] == "X":
        print(board(board))

        if board[battleship_row][balttleship_col] !=0:
            print("You're getting warmer")
        elif board[battleship_row + 1][balttleship_col] !=0 or board[battleship_row - 1][balttleship_col] !=0 or \
             board[battleship_row + 1][balttleship_col + 1] !=0 or board[battleship_row + 1][balttleship_col -1] !=0:
             print("You're getting colder")  
        board[guess_row][guess_col] = "X"    

if guess_row == battleship_row and guess_col == battleship_col:
    print("Bullseye!! You sank my battleship")
    
elif turn == 4:
    print("Game Over. You have been Destroyed")
    
