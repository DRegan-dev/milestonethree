# BattleShips
This is a Python implementation of the classic Battleships game. It creates a square game board of user-defined size and places a battleship on that board. 
The user then has 5 attempts to hit the battleship by input the row and column at which they would like to shoot. The program then provides feedback on each shot as to whether it was a hit or a miss and whether the guess is getting warmer or colder if it is near the battleship location. 

The code makes use of functions tocreate a game board and get input from the user. It also uses a loop to allow the user to make multiple guesses as to the location of the battleship and includes conditional statements to check if the user has sunk the battelship or used up all of their turns. The code could be further improved by add error handling to handle unexpected user input and providing addition feedback to help the user better locate the battleship.

## Features

1. create_board() creates a two-dimensional list to represent the game board.
2. print_board() prints the game board to the terminal.
3. get_input() prompts the user to enter input and checks if it is a valid number.
4. The user is prompted to input the size of the board and the game starts.
5. A battleship is placed randomly on the board.
6. The player has 5 turns to guess the location of the battleship.
7. The program checks if the guess is a hit or a miss and gives appropriate feedback.
8. If the guess is a hit, the program provides additional feedback about the proximity of the battleship.
9. The game ends after 5 turns or when the battleship is sunk.

## Testing

I have conducted tests through python tutor as well as manual testing and while some features work as intened there are a few that dont and have been identified as:
  
          Firstly, the game board's creation and display appear to work correctly, as the create_board() and print_board() functions are defined and called in the code.

However, there are several issues with the game's logic. For instance, the game should end once the user sinks the battleship or exhausts their turns, but there is no explicit check for this condition in the code. Additionally, the code that checks whether the user is getting closer or farther from the battleship seems to have some typos and formatting errors. Finally, there is no explicit check to prevent the user from guessing the same position twice.

Overall, while some features of the project appear to work as intended, there are some issues with the game's logic that could impact the game's behavior.

## Unfixed bugs

The issue with the logic of the game not checking to see if the battleship has been sunk and then ending the game if it was, has not been fixed but will be in a future iteration. 

## Deployment

This project was deployed using heroku. I linked GitHub to heroku added the relevent config vars and build packs. I enabled automatic deploys and deployed the project. 

# Credits

The inspiration for this project as a whole in the format it is in came from https://coderspacket.com/battleship-game-in-python

Additional information on loops came from stack overflow. 
