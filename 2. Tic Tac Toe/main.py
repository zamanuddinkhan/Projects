import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")

        self.player = "X"
        self.board = [""] * 9
        self.buttons = []

        for i in range(9):
            b = tk.Button(self.root, text="", font=("Arial", 20),
                          width=5, height=2,
                          command=lambda i=i: self.play(i))
            b.grid(row=i//3, column=i%3)
            self.buttons.append(b)

        tk.Button(self.root, text="Reset",
                  command=self.reset).grid(row=3, column=0, columnspan=3)

        self.root.mainloop()

    def play(self, i):
        if self.board[i] == "":
            self.board[i] = self.player
            self.buttons[i]["text"] = self.player

            if self.check():
                messagebox.showinfo("Winner", self.player + " Wins!")
                self.reset()
            elif "" not in self.board:
                messagebox.showinfo("Draw", "It's a Draw!")
                self.reset()
            else:
                self.player = "O" if self.player == "X" else "X"

    def check(self):
        win = [(0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6)]

        for a, b, c in win:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def reset(self):
        self.player = "X"
        self.board = [""] * 9
        for b in self.buttons:
            b.config(text="")

TicTacToe()