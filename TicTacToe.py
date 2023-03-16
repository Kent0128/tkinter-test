import tkinter as tk

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("井字棋")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
        
    def create_board(self):
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.master, text="", font=("Arial", 30), width=4, height=2,
                                   command=lambda row=i, col=j: self.click(row, col))
                button.grid(row=i, column=j)
                self.buttons[i][j] = button
        
    def click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col]["text"] = self.current_player
            if self.check_win():
                self.disable_buttons()
                self.master.title(f"{self.current_player} wins!")
            elif self.check_tie():
                self.disable_buttons()
                self.master.title("Tie!")
            else:
                self.switch_players()
    
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != " ":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True
        return False
    
    def check_tie(self):
        for row in self.board:
            for col in row:
                if col == " ":
                    return False
        return True
    
    def switch_players(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.master.title(f"{self.current_player}'s turn")
        
    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
