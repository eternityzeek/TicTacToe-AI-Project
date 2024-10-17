import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master, mode):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.buttons = []
        self.create_board()
        self.ai_player = 'O'
        self.mode = mode

        if self.mode == 'Human vs AI' and self.ai_player == 'X':
            self.ai_move()
        elif self.mode == 'AI vs AI':
            self.ai_vs_ai_move()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text='', font=('Arial', 30), width=8, height=3,
                                   command=lambda i=i, j=j: self.click(i, j), bg="#00ccff")
                button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
                self.buttons.append(button)

    def click(self, i, j):
        index = 3 * i + j
        if self.board[index] == ' ':
            self.buttons[index].config(text=self.current_player, state='disabled', disabledforeground='black', bg="#ffffff")
            self.board[index] = self.current_player
            self.print_state()  # Print the current state of the board
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                self.reset_board()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                if self.mode == 'Human vs AI' and self.current_player == self.ai_player:
                    self.ai_move()

    def ai_move(self):
        if ' ' in self.board:
            index = self.minimax(self.board, 0, True)[1]
            self.buttons[index].config(text=self.ai_player, state='disabled', disabledforeground='black', bg="#ffffff")
            self.board[index] = self.ai_player
            self.print_state()  # Print the current state of the board
            if self.check_winner(self.ai_player):
                messagebox.showinfo("Tic Tac Toe", f"{self.ai_player} wins!")
                self.reset_board()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
    
    def ai_vs_ai_move(self):
        if ' ' in self.board:
            index = self.minimax(self.board, 0, True)[1]
            self.buttons[index].config(text=self.current_player, state='disabled', disabledforeground='black', bg="#ffffff")
            self.board[index] = self.current_player
            self.print_state()  # Print the current state of the board
            if self.check_winner(self.current_player):
                messagebox.showinfo("Tic Tac Toe", f"{self.current_player} wins!")
                self.reset_board()
            elif ' ' not in self.board:
                messagebox.showinfo("Tic Tac Toe", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.ai_vs_ai_move()

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(self.ai_player):
            return 10 - depth, None
        elif self.check_winner('X'):
            return depth - 10, None
        elif ' ' not in board:
            return 0, None

        if is_maximizing:
            best_score = float('-inf')
            best_move = None
            for i in range(9):
                if board[i] == ' ':
                    board[i] = self.ai_player
                    score, _ = self.minimax(board, depth + 1, False)
                    board[i] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move
        else:
            best_score = float('inf')
            best_move = None
            for i in range(9):
                if board[i] == ' ':
                    board[i] = 'X'
                    score, _ = self.minimax(board, depth + 1, True)
                    board[i] = ' '
                    if score < best_score:
                        best_score = score
                        best_move = i
            return best_score, best_move

    def check_winner(self, player):
        win_states = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                      [0, 3, 6], [1, 4, 7], [2, 5, 8],
                      [0, 4, 8], [2, 4, 6]]

        for state in win_states:
            if all(self.board[i] == player for i in state):
                return True
        return False
    
    def print_state(self):
        for i in range(0, 9, 3):
            print(self.board[i], self.board[i+1], self.board[i+2])
        print()

    def reset_board(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        for button in self.buttons:
            button.config(text='', state='normal', bg="#00ccff")

def start_game(mode):
    root = tk.Tk()
    game = TicTacToe(root, mode)
    root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.configure(bg="#f0f0f0")
    
    def start_human_vs_ai():
        start_game('Human vs AI')

    def start_ai_vs_ai():
        start_game('AI vs AI')

    human_vs_ai_button = tk.Button(root, text="Human vs AI", command=start_human_vs_ai, font=('Arial', 20), width=20, height=4, bg="#008CBA", fg="white")
    human_vs_ai_button.pack(pady=15)

    ai_vs_ai_button = tk.Button(root, text="AI vs AI", command=start_ai_vs_ai, font=('Arial', 20), width=20, height=4, bg="#cc3300", fg="white")
    ai_vs_ai_button.pack(pady=15)

    root.mainloop()
