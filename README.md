This is a simple command-line implementation of the classic Tic-Tac-Toe game in Python. Two players can play the game, taking turns to mark the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

How to Run
Ensure you have Python installed on your machine.
Copy the code into a Python file, e.g., tic_tac_toe.py.
Open your terminal or command prompt.
Navigate to the directory where your tic_tac_toe.py file is located.
Run the game by typing:
sh
Copy code
python tic_tac_toe.py
Game Instructions
When prompted, enter the names of the two players.
The game will alternate turns between the players, starting with the player who entered their name first.
On your turn, input the number of the cell (1-9) where you want to place your mark.
If the chosen cell is already occupied, you will be asked to enter a different cell number.
The game will print the current state of the board after each turn.
The game ends when one player gets three of their marks in a row (horizontal, vertical, or diagonal) or when all cells are filled resulting in a draw.
Example Gameplay
diff
Copy code
Please enter X's player name: Alice
Please enter O's player name: Bob
1 | 2 | 3
--|---|--
4 | 5 | 6
--|---|--
7 | 8 | 9
Alice's chance, please enter a value: 1
X | 2 | 3
--|---|--
4 | 5 | 6
--|---|--
7 | 8 | 9
Bob's chance, please enter a value: 5
X | 2 | 3
--|---|--
4 | O | 6
--|---|--
7 | 8 | 9
And so on...

Code Explanation
Functions
printBoard(): Displays the current state of the game board.
checkWin(Xstate, Ostate): Checks if there is a winner or if the game is a draw.
Game Logic
The game alternates turns between the two players.
Each player inputs the cell number where they want to place their mark.
The game checks if the chosen cell is valid (not already occupied).
After each move, the game checks if there is a winner or if the game is a draw.
The game ends when there is a winner or when all cells are occupied resulting in a draw.
