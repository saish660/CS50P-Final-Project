# Tic Tac Toe with Tkinter
#### Video Demo: <https://youtu.be/AK3XruIdmb8?si=yMR1NXzWwYP-UebL>
![Screenshot of startup screen of the application](/images/home_screen.png)
![Screenshot of x winning a 3x3 board in the application](/images/x_wins_game.png)
![Screenshot of a 5x5 board in the application](/images/5x5_board.png)

## Description:
This is a python desktop application made with [Tkinter](https://docs.python.org/3/library/tkinter.html), to play the game of [Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe).
The user inputs the size of the board to play on, starting from 3 to maximum 5. The board will then be displayed of the 
specified size and the user can start playing.

## Project Structure:

### Files:
 - [`project.py`](project.py): Contains all the code for the application.
 - [`test_project.py`](test_project.py): Contains tests for the functions in project.py.

### Usage:
#### 1. Setup:
  - Install `Python` version `3.x`.
  - Use `python -m tkinter` to make sure you have `tkinter` standard library included with your Python installation.
  if not, checkout [tkinter installation tutorial](https://tkdocs.com/tutorial/install.html).
   
#### 2. Using the application:
  - `cd` into the application directory on your computer and run `python project.py`.
  - Enter a valid size as input, or click "Go with default 3x3" button to play classic size 3 game.
    > A valid size is an integer from 3 to 5.
  - Play your move by left-clicking on the tiles.
  - The title will change at the end of the game to reflect the outcomes:
    - `'ACTUAL_WINNER' Wins!!`, where ACTUAL_WINNER is the either `X` or `O`, if a player wins.
    - `It's a draw ._.` if the game is a draw.
  - After the end of the game or even in between the game, a clean new board can be created from the same menu at the bottom of the board.
  - If during a game, there is no possible chance left for anyone winning, but there are still playable moves left, the spaces between the tiles will turn light orange

## Code Description:
### `project.py`
  - #### `class Game`: 
    when object of `Game` is created, all the important variables are initialised and the home screen layout with the input fields is displayed.
    The class contains 2 methods:

    ##### 1. `create_board(self, default=False)`: 
    This method is called when the user clicks on either of the two buttons to create the board.
    The `default` parameter is to inform if it was the `Go with default` button or not. if default is not True, the method tries to get the input from the Entry field.
    if the input is not valid, it shows a popup message informing the user about the same. and if it is valid, it checks if there is a board on the screen to replace it with a new one.
    
    ##### 2. `play_move(self, row, column)`:
    This method is called when the user clicks on any of the available tiles on the board. the two parameters row and column are used to determine which tile was clicked on the board.
    It then updates the text of the tile to current player. ('X' or 'O') and disables the button/tile and also updates the `moves_left`, `board_state` variable that keeps track of which positions are taken by whom.
    It then checks if there is a chance of anyone winning, if there is then it checks if there is a winner or not and if winner is found, it disables all the tiles, and updates the title.
    If there are no chances of winning the game, it changes the background color of the tiles to orange.
    > Background color of the buttons/tiles, in this case changes the color of the space behind the button, hence the color is visible through the gaps between the buttons. 

  - #### `check_win(board_size, win_positions, board_state)`:
    This function is called after playing every move to check if there is any winner. it takes 3 parameters:
      - `board_size`: size of the board that the user is playing on.
      - `win_positions`: list of all possible arrangement of tiles which will result in a win.
      - `board_state`: current state of the board.
        
    All the positions in `win_positions` are checked in `board_state` and if any of the positions have same player on all tiles, the function returns True, if none found at the end of `win_positions` it returns False.

  - #### `game_is_winnable(win_positions, board_state, board_size)`:
    This function is called before checking for a win, just to see if there is any possible chance left of a player winning, if not it returns False, if there is at least one chance, it returns True.
    It takes in 3 arguments which are the same as for `check_win()`
    
  - ### `get_win_positions(board_size)`:
    The function takes board size as an argument and returns a list of all possible combination of tiles that will result in a win for that board size.
    E.g. `[[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]` for a 3x3 board where all the tiles are indexed sequentially from `0` to `board_size - 1`
    
Finally, the main function creates a tkinter window, sets the state of window to "zoomed" to make it full screen when the application is run.
It then creates an instance of `Game` class, and then starts the `mainloop` for tkinter.