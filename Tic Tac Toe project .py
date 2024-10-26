import tkinter as tk
from tkinter import messagebox

# Class representing the Tic Tac Toe game
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board = [''] * 9  # Initialize the board
        self.player = 'X'  # Start with player 'X'
        self.buttons = []
        self.create_board()

    # Create the game board with buttons
    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 20), width=5, height=2,
                               command=lambda i=i: self.click_button(i))
            button.grid(row=i//3, column=i%3)  # Arrange buttons in a grid
            self.buttons.append(button)
    
    # Handle button clicks
    def click_button(self, index):
        if self.buttons[index]['text'] == "" and self.check_winner() is False:
            self.buttons[index]['text'] = self.player
            self.board[index] = self.player
            if not self.check_winner():
                # Switch player after a valid move
                self.player = 'O' if self.player == 'X' else 'X'
        
    # Check for a winner or a tie
    def check_winner(self):
        # Check rows and columns
        for row in range(0, 9, 3):
            if self.board[row] == self.board[row+1] == self.board[row+2] != '':
                self.win(row)
                return True

        for col in range(3):
            if self.board[col] == self.board[col+3] == self.board[col+6] != '':
                self.win(col)
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != '' or self.board[2] == self.board[4] == self.board[6] != '':
            self.win(0 if self.board[0] != '' else 2)
            return True

        # Check for a tie
        if all(self.board):
            self.tie()
            return True

        return False

    # Handle a win scenario
    def win(self, index):
        messagebox.showinfo("Game Over", f"Player {self.board[index]} wins!")
        self.reset_board()
        
    # Handle a tie scenario
    def tie(self):
        messagebox.showinfo("Game Over", "It's a tie!")
        self.reset_board()
        
    # Reset the game board
    def reset_board(self):
        self.board = [''] * 9
        for button in self.buttons:
            button['text'] = ""
        self.player = 'X'  # Reset player to 'X'

# Create and start the game
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()
