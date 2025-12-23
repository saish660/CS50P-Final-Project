import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Game:
    def __init__(self, window):
        self.moves_left = 0
        self.board_state = []
        self.buttons_list = []
        self.win_positions = []
        self.board_size = 3
        self.previous_player = ""
        self.board_frame = None
        self.style = ttk.Style(window)

        self.mainframe = ttk.Frame(master=window, width=100, height=200)
        window.title("Tic Tac Toe with Tkinter")
        window.rowconfigure(0, minsize=100, weight=1)
        window.columnconfigure(0, minsize=100, weight=1)

        self.heading = ttk.Label(master=self.mainframe, text="Tic Tac Toe", font=("consolas", 30, 'bold'),
                                 anchor='center')
        self.heading.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        user_input_frame = ttk.Frame(master=self.mainframe,
                                     borderwidth=1,
                                     relief=tk.SOLID,
                                     style='userInput.TFrame',
                                     padding='15 20 15 20'
                                     )
        size_label = ttk.Label(master=user_input_frame, text="Enter board size:", font='consolas, 11')
        size_label.grid(row=0, column=0)
        self.style.configure('sizeInput.TEntry', padding='10 5')
        self.size_input = ttk.Entry(master=user_input_frame, style='sizeInput.TEntry')
        self.size_input.grid(row=0, column=1, padx=10)
        button = ttk.Button(master=user_input_frame, text="Draw Board", padding=5, command=lambda: self.create_board())
        button.grid(row=0, column=2)
        default_board_btn = ttk.Button(master=user_input_frame,
                                       text="Go with default 3x3",
                                       padding=5,
                                       command=lambda: self.create_board(default=True)
                                       )
        self.mainframe.grid()
        user_input_frame.grid(padx=30, pady=20)
        user_input_frame.grid(row=3, column=0)
        default_board_btn.grid(row=1, column=1, pady=20)

    def create_board(self, default=False):
        if not default:
            try:
                board_size = int(self.size_input.get())
                if board_size < 3 or board_size > 5:
                    raise ValueError
                self.board_size = board_size
            except ValueError:
                messagebox.showinfo(title="Invalid Input",
                                    message="Enter an INTEGER value between 3 and 5 (inclusive) as size"
                                    )
                return
        else:
            self.board_size = 3

        self.size_input.delete(0, tk.END)
        self.buttons_list = []
        self.previous_player = ""
        self.win_positions = get_win_positions(self.board_size)

        self.heading.config(text="Tic Tac Toe")

        self.moves_left = self.board_size * self.board_size
        self.board_state = ["" for _ in range(self.board_size * self.board_size)]

        row_list = []

        # initializes row_list to [0, 1, 2] for board_size = 3
        for i in range(self.board_size):
            row_list.append(i)

        if self.board_frame:
            self.board_frame.destroy()

        self.board_frame = ttk.Frame(master=self.mainframe, padding='70 0')
        self.board_frame.rowconfigure(row_list, minsize=100, weight=1)
        self.board_frame.columnconfigure(row_list, minsize=100, weight=1)

        for i in range(self.board_size):
            for j in range(self.board_size):
                button = ttk.Button(master=self.board_frame,
                                    text=f"",
                                    style="tiles.TButton",
                                    command=lambda row=i, column=j: self.play_move(row, column)
                                    )
                self.style.configure('tiles.TButton', font='Helvetica 20', padding=10, width=5)
                self.buttons_list.append(button)
                button.grid(row=i, column=j, sticky="nsew")

        self.board_frame.grid(row=1, column=0, sticky="nsew")

    def play_move(self, row, column):
        self.moves_left -= 1
        # position is the index of the clicked button in board_state
        position = self.board_size * row + column
        clicked_button = self.buttons_list[position]

        player = "O" if self.previous_player == "X" else "X"
        self.previous_player = player
        self.board_state[position] = player
        clicked_button['text'] = player
        clicked_button['state'] = 'disabled'

        self.style.configure('orangeTiles.tiles.TButton', background="#ffc289")
        if game_is_winnable(self.win_positions, self.board_state, self.board_size):
            if winner := check_win(self.board_size, self.win_positions, self.board_state):
                self.heading['text'] = f"{winner} Wins!!"
                for play_button in self.buttons_list:
                    play_button.state(['disabled'])
        elif self.moves_left == 0:
            self.heading['text'] = "It's a draw ._."
        else:
            for button in self.buttons_list:
                button.configure(style='orangeTiles.tiles.TButton')


def main():
    window = tk.Tk()
    window.state('normal')
    Game(window)
    window.mainloop()


def check_win(board_size, win_positions, board_state):
    for position in win_positions:
        first_value = board_state[position[0]]
        for i in range(board_size):
            if board_state[position[i]] != first_value or first_value == "":
                break
            elif i == board_size - 1:
                return board_state[position[i]]

    return None


def game_is_winnable(win_positions, board_state, board_size):
    for position in win_positions:
        x_in_position = False
        o_in_position = False
        for i in range(board_size):
            if board_state[position[i]] == 'X':
                x_in_position = True
            elif board_state[position[i]] == 'O':
                o_in_position = True
            if i == board_size-1 and not (x_in_position and o_in_position):
                return True
    return False


def get_win_positions(board_size):
    win_positions = []

    for i in range(board_size):
        row_combination = []
        column_combination = []

        for j in range(board_size):
            row_combination.append((i * board_size) + j)
            column_combination.append(i + (board_size * j))

        win_positions.append(row_combination)
        win_positions.append(column_combination)

    diagonal_combination_1 = []
    diagonal_combination_2 = []
    for i in range(board_size):
        diagonal_combination_1.append(i + (board_size*i))
        diagonal_combination_2.append((board_size-i) + ((board_size*i)-1))

    win_positions.append(diagonal_combination_1)
    win_positions.append(diagonal_combination_2)

    return win_positions


if __name__ == "__main__":
    main()
