import tkinter as tk

class ChessGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Chess Game")
        self.board = [
            ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
            ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
        ]
        self.current_player = "white"
        self.draw_board()

    def draw_board(self):
        for i in range(8):
            for j in range(8):
                color = "white" if (i + j) % 2 == 0 else "grey"
                button = tk.Button(self.master, text=self.board[i][j], bg=color)
                button.grid(row=i, column=j)

    def move(self, start_pos, end_pos):
        pass  

root = tk.Tk()
game = ChessGame(root)
root.mainloop()
